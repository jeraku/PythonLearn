Initial Steps to run mongodb in my windows machine via docker

>> docker pull mongo

>> docker run -d --name mongodb -p 27017:27017 mongo

>> docker volume create mongodb_data
>> docker run -d --name mongodb -p 27017:27017 -v C:\jegan\automation\mongodb\mongodbdata:/data/db mongo

>> docker exec -it mongodb mongosh

Clean docker space options.
>> docker container prune
>> docker image prune -a
>> docker volume prune
>> docker network prune
>> docker system prune -a --volumes