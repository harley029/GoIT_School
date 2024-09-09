# import redis

# # Підключення до Redis-сервера
# redis_client = redis.StrictRedis(host="localhost", port=6379, db=0)

# # Отримання значення за певним ключем
# key_name = "tag"
# value = redis_client.get(key_name)

# print(f"Value for key '{key_name}': {value}")


# ________________________________________________________________

import redis
import sys

redis_client = redis.StrictRedis(host="localhost", port=6379, db=0)
sys.stdin.reconfigure(encoding="latin1")

# Сканування всіх ключів та їх значень
for key in redis_client.scan_iter("*"):
    print(key.decode())

# redis_client.set('ho','hohoho')
# redis_client.set("bo", "boBobo")
# print(redis_client.get('ho').decode())
# print(redis_client.keys())
# print(b"ho" in redis_client.keys())
