from idna import decode
import redis

r = redis.Redis(host = "localhost" , port=6379, db=2)

r.hset("user:1000", mapping={"k1": "v1", "k2": "v2", "k3": "v3"})
print(r.hget("user:1000", "k1"))

r.hset("user:1000", "k1", "vv1")
a= (r.hget("user:1000", "k1"))
print(decode(a))

data_items = r.hgetall("user:1000")
a= { k.decode():v.decode() for k,v in data_items.items()}
print(a)

exist= r.hexists("user:1000", "k1")
print("exists => ", exist)

# r.hincrby("user:1000", "k1" 1)