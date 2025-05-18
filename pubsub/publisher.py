import redis
import time

r = redis.Redis(host='localhost', port=6379, decode_responses=True)

messages = [
    "New comment on your post!345465",
    "You have 2 new followers.345",
    "System maintenance at 12AM.345645",
]

for msg in messages:
    r.publish('notifications', msg)
    print(f"✅ Sent: {msg}")
    time.sleep(2)