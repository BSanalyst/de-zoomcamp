# Table of contents
1. [GIT](#git-section)
2. [Docker](#docker-section)

## GIT Section
> This is used to allow GITHUB transactions. Need to be used in the terminal prior to committing:

```git config user.name "github_user"```\
```git config user.email "github_email"```
## Docker Section
### Talking to a container that's not part of the docker network. 
Here, we use the docker container's IP address rather than the machine's name. \
We can invoke this by using: \
```docker network inspect {network name}``` <br> 
if it's on a network, or we can manually drill into the container using: \
```docker container inspect {container id}``` \
Postgres engine connection in Jupyter Notebook, for example.
```eng = sqlalchemy.engine.create_engine("postgresql://USER:PASS@IP_or_HOST:PORT/DB")```
