PREREQUISITES
------------
1.Have Docker installed

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
