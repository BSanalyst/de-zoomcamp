# Table of contents
1. [Installation](#install-section)
2. [Docker](#docker-section) \
    2.1. [Docker Run](#docker-run)

## Install Section
### Apt Store
- sudo apt update
- sudo apt upgrade
- sudo apt-get install docker.io
- sudo apt-get install python3
- sudo apt-get install python3-pip


## Docker Section
### Commands
### Docker Run
> We use docker run to pull an image and create the container.

We have options when we run the container like ```-d``` or ```-it```
- Using ```-d``` means running the container in detached mode. This means we can still interactive with the terminal we're in after running this container.
- Using ```-it``` means we're running an interactive terminal. This means we're in the container in the terminal. If we've declared an entry point or parameter we'll enter that straight from the terminal.

If we have many containers using ```-d``` mode, we can simply use ```docker exec -it {container_id} bash``` if we wanted to step into the terminal of that container. 

#### Examples
1. docker run -it ubuntu bash
    > This will create an ubuntu image in a container with the parameter passed as bash which is executed in the terminal.
    > The container will not be persistent. For instance, if we use docker run -it ubuntu bash again, another container will be created. <ins>To access the same container again</ins> we'll need to use ```docker start {container#}``` and if we want to get back into the ```docker exec -it {container#} bash```
2. docker run -it