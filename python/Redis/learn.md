Running redis form docker 
docker pull redis
docker run -it redis
<!-- open new cmd prompt then run below commands -->
docker exec -it <contanerid> bash
redis-cli
ping 
===================================================

https://github.com/syedjaferk/redis_for_python_parottasalna

To use redis
<!-- Open ubuntu in windows
for installation follow the commands from the below file from UBuntu command prompt -->
https://redis.io/docs/latest/operate/oss_and_stack/install/archive/install-redis/install-redis-on-windows/

sudo service redis-server status  (for windows remove sudo)

redis-cli
ping 


sudo service redis-server status 
sudo apt install redis-server
redis-server --port 6380 



docker exec -it redis filname.py

KEYWORDS

/////////////////////////////////String Commands //////////////////////////////
SET NAME jafar
GET NAME

/////////////////////////////////List command ////////////////////////////////
LPUSH/RPUSH Ex: LPUSH students 
RPOP/LPOP Ex: LPOP students
LRANGE studnets startIndex stopIndex
LRANGE students 0 -1
<!-- left trim students list  start poistion is 0 and end position is 2(FROM LAST) -->
LTRIM students 0 2
<!-- to get the length of the list  -->
LLEN students
<!-- To get the Left remove  -->
LREM names -1 Alice
LREM vs LTRIM ->> By value is LRem and Ltrim is discard the other values.
<!-- to delete the list -->
DEL students
/////////////////////////////////Set command ////////////////////////////////
sadd name jtest1 jtest2  
sismember 
sREM online_user charlie
SPOP online_user
SISMEMBER in online_user
SRANDMEMBER in online_user 2
SCARD > to get length
SMOVE


EXPIRE <setName> 100
TTL <setname>
PERSIST <setname>

==================================
PUBLISH notificiatons "hi"
SUBSCRIBE notifications

bloom filter in instagram
redis memcache, Valkey different cache mechanism during code.