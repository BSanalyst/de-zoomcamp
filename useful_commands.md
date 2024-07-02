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

### Container configurations

```
docker run -d \
	--name postgres_hwk1 \
	-e POSTGRES_USER=hwk1_user \
	-e POSTGRES_PASSWORD=hwk1_password \
	-e POSTGRES_DB=hwk1_db \
	--network=hwk1_network \
	-p 5432:5432 \
	-v /home/bstring/hwk1/pg_data_mounting:/var/lib/postgresql/data \
	postgres


docker run -it \
	--name python_hwk1 \
	--network=hwk1_network \
	-p 8888:8888 \
	python
```

### Python ETL Noteworthy pieces
This function takes a dataframe, converts it into the appropriate SQL schema - based on the engine. However, we use ```sqlalchemy.text``` function to handle the "\n" plain text pieces. 
sqlalchemy.text(pd.io.sql.get_schema(df, "test", con=eng))
