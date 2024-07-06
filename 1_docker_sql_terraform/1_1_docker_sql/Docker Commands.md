- [Install Section](#install-section)
  - [Apt Store](#apt-store)
- [Docker Section](#docker-section)
  - [Commands](#commands)
  - [Docker Run](#docker-run)
    - [Examples](#examples)
  - [Docker build](#docker-build)
    - [command examples](#command-examples)
      - [Breakdown](#breakdown)
    - [docker file examples](#docker-file-examples)
      - [Breakdown](#breakdown-1)
    - [passing arguments from CMD to the python file.](#passing-arguments-from-cmd-to-the-python-file)
  - [Docker assets interacting](#docker-assets-interacting)
    - [Interaction between elements](#interaction-between-elements)

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
    > The container will not be persistent, in that, all changes to the container from creation can be lost. Whilst in the stopped state, we can restart them. However, once they've been deleted, we can't return to the last known cache. For instance, if we use docker run -it ubuntu bash again, another container will be created. <ins>To access the same container again</ins> we'll need to use ```docker start {container#}``` and if we want to get back into the ```docker exec -it {container#} bash```
2. docker run -it --entrypoint=BASH python:3.9
    Allows us to enter a container at a specific point, similar to the command above but we may pass many parameters after the image. This can keep it tidy.

If we do create a docker container like this ```docker run -it --entrypoint=BASH python:3.9```, we wouldn't retain any python libraries using pip. If we did want to initialise the container each time with that set of commands. We'd want to leverage a docker file for reproducibility.

This gets us onto **Docker Files** and the **Build** command. This allows us to build an image with a set of instructions. Essentially, extending the run -it container command:

### Docker build
#### command examples
1) ```docker build -t test:pandas .```

##### Breakdown

```docker build```: This is the Docker command to build an image from a Dockerfile.

```-t test:pandas```: This option tags the image with a name and optionally a version.
    test: This is the repository name of the image.
    pandas: This is the tag or version of the image. Tags are often used to version images or differentiate between different builds of the same image.

Together, test:pandas is the full name of the image. If you omit the tag, it defaults to latest.

```.```: This specifies the build context, which is the directory containing the Dockerfile. The . represents the current directory.

#### docker file examples
```FROM python:3.9

RUN pip install pandas

WORKDIR /app

COPY pipeline.py pipeline.py

ENTRYPOINT ["bash"] 

CMD ["-c", "echo 'hello world'",]

```

##### Breakdown
FROM (image we're pulling)
RUN (commands to execute when running the container)
WORKDIR (where we land inside the container)
COPY (source file to copy; dest file to copy )
ENTRYPOINT (similar to cmd but we can't overwrite the argument and \
these are passed to the container once it's run). Note, they look for an exec file i.e. bash; python; and all the other commands are concatenated and passed along to exec. For more control, consider using a .sh script and running this. When we run a container:
```run -it container# cmd_param1 cmd_param2``` we can use these parameters to overwrite the current dockerfile's cmd values or pass extras through for execution. Most importantly ```-c``` tells bash it's going to pass a string to it and to execute it as a string. Otherwise, it'll think it's being directed towards a file.

#### passing arguments from CMD to the python file.
We can leverage this:
>Command-line Arguments: sys.argv is a list in Python that contains these command-line arguments. It is populated automatically by the Python interpreter when the script is executed. The elements of sys.argv are: \
    sys.argv[0]: This is the script name itself.\
    sys.argv[1] to sys.argv[n]: These are the command-line arguments passed to the script.

**Example**
```ENTRYPOINT ["python"]

CMD ["pipeline.py","argument here", "another here"]
```
We could put pipeline.py into the entrypoint aswell. Tomato/Tomatoe type situation. This then passes these two arguments into it so we can leverage them in the python file.

### Docker assets interacting
#### Interaction between elements
When we want docker containers to interact, we have a couple of options.
1. Create a docker network and associate this network to each docker container upon container creation.
2. Create a docker.yml file which uses the command docker-compose. It will build the network automatically and it will also build all the resources we need automatically. 

