import pandas as pd
import sqlalchemy
import psycopg2
import requests, os, sys
import argparse


def main(params):
    username=params.username
    password=params.password
    container_ip=params.container_ip
    port=params.port
    database=params.database
    url=params.url_to_download
    url_lookup=params.url_to_download_lookup

    eng = sqlalchemy.engine.create_engine(f"postgresql://{username}:{password}@{container_ip}:{port}/{database}")

    #eng = sqlalchemy.engine.create_engine("postgresql://hwk1_user:hwk1_password@172.18.0.2:5432/hwk1_db")
    # url = "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-09.csv.gz"

    #Download Data File
    os.system(f"wget {url} -O {os.path.basename(url)}")
    
    #Table name infered from file downloaded
    tbl_name = os.path.basename(url).split(".")[0]


    # Dropping Table
    with eng.begin() as conn:
        conn.execute(sqlalchemy.text(f'DROP TABLE IF EXISTS "{tbl_name}"'))
        print("succesful")

    i=0
    tbl_name = os.path.basename(url).split(".")[0]



    # Reading data into SQL in chunks
    df = pd.read_csv(os.path.basename(url), compression='gzip', chunksize=100000)

    for df_chunk in df:
        df_chunk["lpep_pickup_datetime"] = pd.to_datetime(df_chunk["lpep_pickup_datetime"])
        df_chunk["lpep_dropoff_datetime"] = pd.to_datetime(df_chunk["lpep_dropoff_datetime"])
        i+=len(df_chunk)
        df_chunk.to_sql(name=tbl_name, con=eng, if_exists='append', index=False)
        print(f"{i} records appended so far")


    ## Importing lookup
    # aliases
    tableNameLookup = os.path.basename(url_lookup).split(".")[0]
    fileNameLookup = os.path.basename(url_lookup)
    
    # download lookup
    os.system(f"wget {url_lookup} -O {fileNameLookup}")

    #ingest and output
    pd.read_csv(fileNameLookup).to_sql(tableNameLookup, con=eng, if_exists="replace", index=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some parameters.')
    parser.add_argument('--username', help='The username')
    parser.add_argument('--password', help='The password')
    parser.add_argument('--container_ip', help='The container IP address')
    parser.add_argument('--port', help='The port number')
    parser.add_argument('--database', help='The database name')
    parser.add_argument('--url_to_download', help='The URL to download data from')
    parser.add_argument('--url_to_download_lookup', help='The URL to download data from')
    args = parser.parse_args()
    main(args)
