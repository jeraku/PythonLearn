### PG_BOUNCEr > PG_BOuncer Flow
PG server > 
Connection - I/O operation > 
Connection -> Open will cause failure - So close is reuqired.

Pooling
> connections will be stored in bucket like a bucket and next process will pull and use the object.> like thread will be used for connection pooling.

pgbouncer controls the number of connection to connect into the DB.

Commands
sudo apt install pgbouncer
pgbouncer -v
ls /etc/pgbouncer/

pgbouncer/pgbouncer.ini > initialising files are getting stored in it.

update the below line in pgbouncer.ini file.
refname = host=127.0.0.1 post=6432 dbname = dvdrental

add below contnet in userlist file
/etc/pgbouncer/userlist.txt

echo -n "password" | md5sum

systemctl restart postgresql

systemctl status postgresql

systemctl restart pgbouncer
systemctl enable pgbouncer

psql -h 127.0.0.1 -p 6432 -U jeganraj -d dbname -W




