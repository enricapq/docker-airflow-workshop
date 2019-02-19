# docker-airflow workshop

This repository is intended for demonstrating the usage of Apache Airflow.<br>
It's a fork of the [puckel/docker-airflow](https://github.com/puckel/docker-airflow) project.

It contains **Dockerfile** of [apache-airflow](https://github.com/apache/incubator-airflow) for [Docker](https://www.docker.com/)'s [automated build](https://registry.hub.docker.com/u/puckel/docker-airflow/) published to the public [Docker Hub Registry](https://registry.hub.docker.com/).

This project creates a full working Airflow environment that makes use of a Celery Executor, with Redis as the broker/backend and PostgreSQL as database.

The Docker compose will run a container for: 
* Airflow Scheduler
* Airflow Webserver
* Airflow Worker
* Flower
* PostgreSQL
* Redis


#### Prerequisites:
Having [Docker](https://www.docker.com/) installed on your computer:
1. Sign up for a Docker Hub account (go to https://www.docker.com/)
2. Download and install [Docker](https://www.docker.com/get-started) and [Docker Compose](https://docs.docker.com/compose/install/) for Developers for your OS<br>
   * For **Windows**  users
     - If your system is Windows 10 Professional or Enterprise 64-bit: install [Docker for Windows Desktop edition](https://hub.docker.com/editions/community/docker-ce-desktop-windows).
     - If your system is **Windows Home**, You won't be able to install [Docker for Windows Desktop edition](https://hub.docker.com/editions/community/docker-ce-desktop-windows) because it requires Hyper-V virtualization.
   Install instead [Docker Toolbox](https://docs.docker.com/toolbox/toolbox_install_windows/) which uses VirtualBox.
   Install also [OracleVM VirtualBox](https://www.virtualbox.org/). In VirtualBox:
       * Click the appropriate machine (check the one labeled "default")
       * Go to Settings
       * Network > Adapter 1 > Advanced > Port Forwarding
       * Click "+" to add a new Rule
       * Set Host Port 8080 and Guest Port 8080. Leave Host IP and Guest IP empty
      
     - With **Docker Toolbox** instead of localhost, you will access the IP **192.168.99.100**.

   * For **old Mac** systems
      - Install [Docker Toolbox](https://docs.docker.com/toolbox/toolbox_install_mac/) (install also [OracleVM VirtualBox](https://www.virtualbox.org/))
    
   Note: **Docker Compose** is already included with Docker Desktop and Docker Toolbox.
   In Linux, Docker Compose requires to be installed manually (see the [Installation instructions](https://docs.docker.com/compose/install/).
    
3. Login in Docker
