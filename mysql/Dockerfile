FROM mysql:latest

ENV MYSQL_ROOT_PASSWORD=password
ENV MYSQL_DATABASE=test_database
ENV MYSQL_USER=user
ENV MYSQL_PASSWORD=test_password

# Add the initialization script
COPY init.sql /docker-entrypoint-init.d/
