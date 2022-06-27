FROM postgres:latest
ENV POSTGRES_PASSWORD=apps7
ENV POSTGRES_USER=apps7_user
ENV POSTGRES_DB=apps7_db
COPY create_fixtures.sql /docker-entrypoint-initdb.d/create_fixtures.sql