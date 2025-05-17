import redis
r = redis.Redis()

key = "names"

r.rpush(key, "test1")
r.rpush(key, "test2")
r.rpush(key, "test3")

r.lrange(key, start=0, end=-1)