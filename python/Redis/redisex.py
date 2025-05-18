import redis
r = redis.Redis(host='localhost', port=6379, db=0)

key = "names"


r.set('name', 'Jegan')

print(r.get('name').decode('utf-8'))  # Output: Jegan

r.rpush(key, "test1")
r.rpush(key, "test2")
r.rpush(key, "test3")

r.lrange(key, start=0, end=-1)
print(r.lrange(key, start=0, end=-1))  # Output: Jegan
