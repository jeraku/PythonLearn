import redis

r = redis.Redis()
print(r.ping())
chat_key="chat:room1"
# r.delete(chat_key)

def post_message(user, message):
    text = f"{user}: {message}"
    r.lpush(chat_key,text)
    r.ltrim(chat_key,-4, -1)
    # r.set(user,message)
    # pass
def get_message():
    messages=r.lrange(chat_key,0,-1)
    return messages


# Demo usage
post_message("jafer", "Hello room!")
post_message("alice", "Hi everyone!")

print("Recent messages:")
messages=get_message()
for m in messages:
    print(m.decode())

# Before:
# chat_key → ["msg1", "msg2", "msg3", "msg4", "msg5", "msg6", "msg7"]

# Command:
# r.ltrim(chat_key, -4, -1)
