import pika

from mongoengine import connect
from models import Contact

# Підключення до бази даних
connect(
    "Rabbit_MQ_DB",
    host="mongodb+srv://harley029:8lyrMibko@cluster0.b6lozo9.mongodb.net/?retryWrites=true&w=majority",
)

# Підключення до RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

# Створення черги
channel.queue_declare(queue="sms_queue")


# Функція обробки повідомлення
def callback(ch, method, properties, body):
    # Отримання ObjectID контакту
    contact_id = body.decode("utf-8")
    # Пошук контакту за ObjectID
    contact = Contact.objects(id=contact_id).first()
    # Імітація надсилання SMS
    print(f"Надсилання SMS контакту: {contact.full_name}, {contact.phone_number}")
    # Оновлення статусу надсилання
    contact.update(set__message_sent=True)

# Споживання повідомлень з черги
channel.basic_consume(queue="sms_queue", on_message_callback=callback, auto_ack=True)
channel.start_consuming()