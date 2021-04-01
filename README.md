<img src="icon.png" align="right" />

# Wordpress-monitoring-docker
This repository provides an easy way to install and configure WordPress in conjunction with a database and nginx.



clone repository: ``` git clone https://github.com/justknife/wordpress_monitoring_docker.git ```

You must install python before use it 

   ## Using:

    1. cd wordpress_monitoring_docker
    
    2. mv .env_example .env 
    (or create your .env)
    
    3. run  python python3 main.py 
    wait until the script finishes

    4.  run docker-compose up -d (if you want to start it on daemon mode)
        Ready
        

go to https://blog.example.com to start work on wordpress


go to https://grafana.example.com to start work on grafana monitoring


go to https://prometheus.example.com to start work on prometheus

## Configuring

### To change the domain name of a resource:
   1. Go to the directory with the site configuration files
      ```cd nginx/sites-available/ ```
   2. Open the required file with a text editor convenient for you.
      example: ```vim blog.example.com```
### To configure manual enviroment of containers:

   Replace the value of the domain_name variable with the one you need
      all config data is in ```.env``` file
   Enviroment on env file 

```   MYSQL_ROOT_PASSWORD```  
```   MYSQL_DATABASE```
```   MYSQL_DB_USER```
```   MYSQL_DB_PASSWORD```
### To configure prometheus:
   a. Go to directory prometheus
   ```cd data/prometheus/```
   b. Open ```prometheus.yml``` and add who you need
   ``` vim primetheus.yml```
5. From configure grafana go to grafana.example.com



## License

This project is licensed under the MIT open source license.


### Contact me via twitter: @fa1se_promises
