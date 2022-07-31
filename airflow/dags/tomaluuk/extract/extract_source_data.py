"""
  Source data ingestion
"""

__author__ = "Topi Luukkanen"

import os
import logging
from fastparquet import ParquetFile
import pandas as pd
from sqlalchemy.types import Integer, VARCHAR
from sqlalchemy.schema import CreateSchema
from tomaluuk.extract.utils import get_engine, load_config

logging.basicConfig(level=logging.INFO)

DATA_FILES_PATH = "/opt/airflow/dags/tomaluuk/data/"
DATA_FILES = os.listdir(DATA_FILES_PATH)
SOURCE_SCHEMA = 'sources'


def create_schema(name: str, db_engine):
    try:
        if not db_engine.dialect.has_schema(db_engine, name):
            db_engine.execute(CreateSchema(name))
    except Exception as e:
        logging.error(f'Unable to create schema "{name}"')
        logging.error(str(e))


def load_jsonl_gz_data(file: str) -> pd.DataFrame:
    """
    Load gzip-compressed jsonl data.
    :param str path: Path to file
    :return: DataFrame object of the data
    """
    logging.info(f'Reading file: {file}')
    return pd.read_json(file, lines=True, compression='gzip')


def load_parquet_data(file: str) -> pd.DataFrame:
    """
    Load parquet data
    :param str path: Path to file
    :return DataFrame object of the data:
    """
    logging.info(f'Reading file: {file}')
    return ParquetFile(file).to_pandas()


def load_data_to_df(filepath: str):
    """"Load data from list of files. Infer filetypes."""

    if filepath.endswith('.jsonl.gz'):
        return load_jsonl_gz_data(filepath)
    if filepath.endswith('.parquet'):
        return load_parquet_data(filepath)
    logging.info(
        f'Function {load_data_to_df.__name__} encountered unknown file type in file {filepath}')
    return


def write_to_db(data, table_name, schema, db_engine):
    """Write data to tables"""

    logging.info(f"Writing table to db: {schema}.{table_name}")

    data.to_sql(
        name=table_name,
        schema=schema,
        con=db_engine,
        method='multi',
        if_exists='replace',
        chunksize=10000,
        index=False
    )
    return


def main():
    """"docstring"""
    source_data_config = load_config('source_data')
    # db_tables = config['source_data']
    # data_files = config['files'].keys()
    db_engine = get_engine()

    create_schema(SOURCE_SCHEMA, db_engine)

    for key in source_data_config['data']:
        specs = source_data_config['data'][key]
        df = load_data_to_df(
            os.path.join(source_data_config['path'], specs['file_name'])
        )

        write_to_db(
            data=df,
            table_name=specs["table_name"],
            schema=SOURCE_SCHEMA,
            db_engine=db_engine
        )
    # municipalities = load_data_to_df(
    #    os.path.join(DATA_FILES_PATH, "most-popular-first-names-by-municipality.jsonl.gz"))
    # print(municipalities.head())


# write_to_db(data=municipality_data, table_name='municipality',
#     db_engine=engine, schema='population', dtype=municipality_dtypes)


if __name__ == "__main__":
    main()
