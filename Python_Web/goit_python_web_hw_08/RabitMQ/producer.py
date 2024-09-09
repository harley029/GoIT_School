from random import choice

import faker
import pika

from mongoengine import connect
from models import Contact

fake = faker.Faker("uk-UA")

# Підключення до бази даних
connect(
    "book_db",
    host="mongodb+srv://harley029:8lyrMibko@cluster0.b6lozo9.mongodb.net/Rabbit_MQ_DB?retryWrites=true&w=majority",
)

# Підключення до RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

# Створення черг
channel.queue_declare(queue="sms_queue")
channel.queue_declare(queue="email_queue")

# Створення фейкових контактів
for _ in range(10):
    contact = Contact(
        full_name=fake.name(),
        email=fake.email(),
        phone_number=fake.phone_number(),
        preferred_contact_method=choice(["SMS", "Email"]),
        message_sent=False
    )
    contact.save()

# Відправлення повідомлення в чергу
contacts = Contact.objects()
for contact in contacts:
    if contact.preferred_contact_method == "SMS":
        queue_name = "sms_queue"
    else:
        queue_name = "email_queue"

    message = str(contact.id)
    channel.basic_publish(exchange="", routing_key=queue_name, body=message)
    # contact.update(set__message_sent=True)

print("Kонтакти створено, повідомлення відправлені.")