PREREQUISITES
------------
1.Have Docker installed

From dabatase folder:

docker pull postgres

docker run --name postgre-container -p 5432:5432 -e POSTGRES_PASSWORD=mypassword -d postgres <----> docker start postgre-container

2. create database and user in docker 
 
psql -d postgres -U postgres

CREATE DATABASE apps7_db
CREATE USER apps7_user WITH PASSWORD 'apps7'
GRANT ALL PRIVILEGES ON DATABASE apps7_db TO apps7_user;

3. prepare code according to tutorial (app and database folder)

4.
Starting Docker container with DB and Python script (we should have Postgre container installed earlier)
docker-compose up --build -> from directory root

5. nakon što se pokrene image moraš startati db container 

>docker exec -it apps7_ad_network-db-1 bash
root@85c645c97158:/# \l
bash: l: command not found
root@85c645c97158:/# sudo -u postgres psql postgres
bash: sudo: command not found
root@85c645c97158:/# psql
psql: error: connection to server on socket "/var/run/postgresql/.s.PGSQL.5432" failed: FATAL:  role "root" does not exist
root@85c645c97158:/# sudo -u postgres
bash: sudo: command not found
root@85c645c97158:/# create database master
bash: create: command not found
root@85c645c97158:/# psql -d apps7_db -U apps7_user
psql (14.4 (Debian 14.4-1.pgdg110+1))
Type "help" for help.

apps7_db=# \l
                                    List of databases
   Name    |   Owner    | Encoding |  Collate   |   Ctype    |     Access privileges
-----------+------------+----------+------------+------------+---------------------------
 apps7_db  | apps7_user | UTF8     | en_US.utf8 | en_US.utf8 |
 postgres  | apps7_user | UTF8     | en_US.utf8 | en_US.utf8 |
 template0 | apps7_user | UTF8     | en_US.utf8 | en_US.utf8 | =c/apps7_user            +
           |            |          |            |            | apps7_user=CTc/apps7_user
 template1 | apps7_user | UTF8     | en_US.utf8 | en_US.utf8 | =c/apps7_user            +
           |            |          |            |            | apps7_user=CTc/apps7_user
(4 rows)

apps7_db=# \dt
           List of relations
 Schema |  Name   | Type  |   Owner
--------+---------+-------+------------
 public | numbers | table | apps7_user
(1 row)
