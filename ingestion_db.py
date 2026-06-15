import pandas as pd
import os
from sqlalchemy import create_engine
from urllib.parse import quote_plus
import logging
import time

logging.basicConfig(
    filename = "logs/ingestion_db.log",
    level = logging.DEBUG,
    format = "%(asctime)s - %(levelname)s - %(message)s",
    filemode = 'a'
)

username = 'postgres'
password = quote_plus('Mohith@23')
host = 'localhost'
port = '5432'
database = 'inventory'
engine = create_engine(f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}')

def ingest_db(df, table_name, engine):
    '''this function ingests the dataframe in to the database'''
    df.to_sql(table_name, con = engine, if_exists='replace', index=False) 

def load_raw_data():
    '''This function will load CSV in dataframe and ingest into db'''
    start_time = time.time()
    for file in os.listdir('data'):
        if '.csv' in file:
            df = pd.read_csv('data/' + file)
            logging.info(f'Ingesting {file} in db')
            ingest_db(df, file[:-4], engine)
    end_time = time.time()
    total_time = (end_time - start_time)/60
    logging.info("Ingestion Complete")
    logging.info(f"\n Total Time Taken: {total_time} minutes")

if __name__ == '__main__':
    load_raw_data()