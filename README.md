This repository provides an easy way to install and configure WordPress in conjunction with a database and nginx.



clone repository: https://github.com/justknife/wordpress_monitoring_docker.git

You must install python before use it 

   Using:

    1. cd wordpress_monitoring_docker

    2. run ```python python3 main.py ```
    wait until the script finishes

    3.  run docker-compose up -d (if you want to start it on daemon mode)
        Ready
        

go to blog.example.com to start work on wordpress


go to grafana.example.com to start work on grafana monitoring


go to prometheus.example.com to start work on prometheus

CONFIGURING


all config data is in .env file 
