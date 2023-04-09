MySQL command line tools 

1. open up a terminal and Connect to the Docker container running MySQL using the docker exec command. For example, if your container is named my-mysql, you can connect to it using the following command:
    
      docker exec -it my-mysql bash
      
2. Run the mysql command-line tool and provide the MySQL root user credentials:

      mysql -u root -p
      
3. After you log in, you can use the SHOW DATABASES; command to list all available databases:

      SHOW DATABASES;
      SHOW TABLES;
