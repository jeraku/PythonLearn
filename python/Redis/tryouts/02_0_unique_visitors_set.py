import redis
from datetime import datetime
import sys
r = redis.Redis(host="localhost", port="6379", db=0)

def get_key(date=None):
    # print(date)
    if not date:
        date = datetime.today().strftime("%Y-%m-%d")
    return  f"visitors:{date}"

def track_visit(user_id, ttl_sec=26000):
    key= get_key()
    print(f"{key} and {user_id}" )
    added=r.sadd(key, user_id)
    if added:
        if r.ttl(key)==-1:
            r.expire(key,ttl_sec)
    print(f"user id is {user_id}, time expiration is {ttl_sec}")

def get_today_count():
    count= r.scard(get_key())
    print(get_key())
    print(f"unique vistors count for {get_key()} = {count}")

def get_count_by_date(date):
    count = r.scard(date)
    print(f"Unique vistors count for {date} = {count}")
def keys_list():
    print(r.keys("*"))
def keys_value(keyVal):
    print(r.smembers(keyVal))
def print_help():
    help= f"""
    python visitor_tracker.py visit <user_id>
    python visitor_tracker.py today
    python visitor_tracker.py count <YYYY-MM-DD>
    python visitor_tracker.py intersect <date1> <date2>
    python visitor_tracker.py union <date1> [<date2> ...]
    python visitor_tracker.py diff <date1> <date2>
    python visitor_tracker.py keys_list
    python visitor_tracker.py key_name
    
    """

    print(help)

if(__name__ == "__main__"):
    # print(len(sys.argv))
    if(len(sys.argv)<2):
        print_help()
        sys.exit()
    print(sys.argv[1])
    if (sys.argv[1] == "visit"):
        track_visit(sys.argv[2])
        print("test")
    if (sys.argv[1] == "today"):
        get_today_count()
    if (sys.argv[1] == "keys_list"):
        keys_list()
    if (sys.argv[1] == "key_name"):
        keys_value(sys.argv[2])
    else:
        print("rerun again")
