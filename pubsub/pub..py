import redis

r =redis.Redis(http="localhost", port=6379,decode_response =True )

pub = r.pubsub()

message = ["test", "test1", "test2"]
for msg in message:
    r.publish("test notificaiton" , msg)
    print("message published successfully")
    time.sleep(2)
