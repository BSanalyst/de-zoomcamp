# Homework
## Setup
1) Run a container with postgres.\
   1) Docker build container
   2) Ensure ingestion is automated upon running
   3) Allow parameters to overwrite ingestion script
2) Analyse data based on hwk1.


## Building
1) Build the python script we'll need for ingestion
   1) Will need to run this in the container whilst developing
For this, spin up container. Get python and jupyter notebook. Will need to build this from dockerbuild at the end to dockerise the script with argsparse and sys.argv modules. 

Will the container be a postgres image? Then we pass installation commands?