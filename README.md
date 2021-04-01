<img src="icon.png" align="right" />

# Wordpress-monitoring-docker
This repository provides an easy way to install and configure WordPress in conjunction with a database and nginx.



clone repository: ``` git clone https://github.com/justknife/wordpress_monitoring_docker.git ```

You must install python before use it 

   ## Using:

    1. cd wordpress_monitoring_docker

    2. run *** python python3 main.py ***
    wait until the script finishes

    3.  run docker-compose up -d (if you want to start it on daemon mode)
        Ready
        

go to https://blog.example.com to start work on wordpress


go to https://grafana.example.com to start work on grafana monitoring


go to https://prometheus.example.com to start work on prometheus

## Configuring

to change the domain name of a resource:
1. Go to the directory with the site configuration files
  ```cd nginx/sites-available/ ```
2. Open the required file with a text editor convenient for you.
example: ```vim blog.example.com```
3. Replace the value of the domain_name variable with the one you need
all config data is in ```.env``` file
   Enviroment on env file 
```MYSQL_ROOT_PASSWORD  
   MYSQL_DATABASE
   MYSQL_DB_USER
   MYSQL_DB_PASSWORD```





Contact me via twitter: @fa1se_promises
