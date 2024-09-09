import sys
from builtins import ConnectionError as MongoConnectionError

from mongoengine import connect
from mongoengine.queryset.visitor import Q

import redis
from redis_lru import RedisLRU

from models import Author, Quote


# Підключення до Mongo DB
def connect_to_mongo():
    try:
        connect(
            "book_db",
            host="mongodb+srv://harley029:8lyrMibko@cluster0.b6lozo9.mongodb.net/?retryWrites=true&w=majority",
        )
    except MongoConnectionError:
        print("Failed to connect to MongoDB. Please check your connection settings.")
        sys.exit(1)

# Підключення до Redis-сервера
def connect_to_redis():
    try:
        redis_client = redis.StrictRedis(host="localhost", port=6379, db=0)
        redis_lru = RedisLRU(
            redis_client, 100
        )  # 1000 - максимальна кількість елементів у кеші
    except redis.ConnectionError:
        print("Failed to connect to Redis server. Please check your connection settings.")
        sys.exit(1)
    return redis_lru

# Формувати унікальний ключ для кешу за типом запиту та значенням
def generate_cache_key(command, value):
    return f"{command}:{value}"

def search_quotes():
    while True:
        command = input(
            "Enter command (tag:<tag>, name:<author_name>, tags:<tag1>,<tag2>, exit): "
        ).strip()
        
        # перевірка на існування в кеші за 4-ма командами
        # "tag", "name" та іх скорочення "ta", "na"
        if (
            command.startswith("tag")
            or command.startswith("ta")
            or command.startswith("name")
            or command.startswith("na")
        ):
            tag_name = command.split(":")[1].strip()
            cache_key = generate_cache_key("tag", tag_name)
            cached_quotes = redis_lru.get(cache_key)
            if cached_quotes is not None:
                print("Retrieved from Redis Cache:")
                print_quotes(cached_quotes)
            # пошук даних в MongoDB та запис до кешу
            else:
                if command.startswith("tag:"):
                    tag_name = command.split(":")[1].strip()
                    if len(tag_name) <= 2:  # Перевірка на скорочений тег
                        quotes = Quote.objects(tags__istartswith=tag_name).all()
                    else:
                        quotes = Quote.objects(tags=tag_name).all()
                    print("Retrieved from MongoDB:")
                    print_quotes(quotes)
                    redis_lru.set(cache_key, quotes)  # Запис до кешу
                elif command.startswith("name:"):
                    author_name = command.split(":")[1].strip()
                    if len(author_name) <= 2:  # Перевірка на скорочене ім'я
                        authors = Author.objects(fullname__istartswith=author_name).all()
                    else:
                        authors = Author.objects(fullname__icontains=author_name).all()
                    if authors:
                        quotes = Quote.objects(author__in=authors).all()
                        print("Retrieved from MongoDB:")
                        print_quotes(quotes)
                        redis_lru.set(cache_key, quotes)  # Запис до кешу
                    else:
                        print("Author not found.")
                elif command.startswith("tags:"):
                    tags = command.split(":")[1].strip().split(",")
                    # Формуємо складний запит за тегами
                    query = Q()
                    for tag in tags:
                        query |= Q(tags=tag.strip())
                    quotes = Quote.objects(query).all()
                    print_quotes(quotes)
        elif command == "exit":
            print("Exiting script...")
            break
        else:
            print("Invalid command. Please try again.")

def print_quotes(quotes):
    for quote in quotes:
        print(f"{quote.author.fullname}: {quote.quote}")


if __name__ == "__main__":
    connect_to_mongo()
    redis_lru = connect_to_redis()
    sys.stdin.reconfigure(encoding="latin1")
    search_quotes()
