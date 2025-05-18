import redis

r = redis.Redis(host='localhost', port=6379, decode_responses=True)
pubsub1 = r.pubsub()
pubsub1.subscribe('notifications')

print("Subscribed12313 to 'notifications' channel...")

for message in pubsub1.listen():
    if message['type'] == 'message':
        print(f"📨 New Notification23423421231: {message['data']}")