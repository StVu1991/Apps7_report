PREREQUISITES
------------
Have Docker installed

docker pull postgres
docker run --name postgre-container -p 5432:5432 -e POSTGRES_PASSWORD=mypassword -d postgres <----> docker start postgre-container

psql -d postgres -U postgres

CREATE DATABASE apps7_db
CREATE USER apps7_user WITH PASSWORD 'apps7'
GRANT ALL PRIVILEGES ON DATABASE apps7_db TO apps7_user;
