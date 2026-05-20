Types of DB:
Postgres - Relational DB
Redis - In memory DB
NEO4J - Graph DB

Graph
- Consider a graph you will have the nodes and edges then that will represent the GRAPH
Ex: In social media, if you have friends then you can fetch like Friends of friends. you can build the graphical structure.

properties - Metdata will contains the user details ex: in Json file {personname ["email": "", "number", ""]}

To query the data Cypher language will be used. its similar to SQL query but its easy to query.

Ex: 
CREATE(p:Person {name "Alice", age :30})
node is full set 
person is label
p - node identifier.
data in key value pair is   properties.

we can run this using docker as a best option.

you can follow the below link for the normal installation
https://neo4j.com/docs/operations-manual/current/installation/

for Docker installation
Follow this page: https://neo4j.com/docs/operations-manual/current/docker/introduction/
Below command is more than enough for docker installation.

docker run \
    --restart always \
    --publish=7474:7474 --publish=7687:7687 \
    neo4j:2026.04.0