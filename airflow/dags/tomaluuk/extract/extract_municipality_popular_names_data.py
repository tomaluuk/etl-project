"""
  Data ingestion
"""

__author__ = "Topi Luukkanen"

import os
import logging
from fastparquet import ParquetFile
import pandas as pd
from sqlalchemy.types import Integer, VARCHAR
from tomaluuk.extract.utils import get_engine, load_config

logging.basicConfig(level=logging.INFO)
engine = get_engine()

DATA_FILES_PATH = "/opt/airflow/dags/tomaluuk/data/"
DATA_FILES = os.listdir(DATA_FILES_PATH)


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


def set_data_types(dtypes: str):
    """Sets SQL Alchemy data types from strings"""
    res = []
    dtypes.rep


def write_to_db(data, table_name, schema, db_engine):
    """writes data to tables"""
    #sqlalc_dtypes = set_data_types(dtypes)

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
    config = load_config()
    db_tables = config['db_tables']
    db_engine = get_engine()

    for table, specs in zip(db_tables.keys(), db_tables.values()):
        df = load_data_to_df(
            os.path.join(DATA_FILES_PATH, specs['filename'])
        )

        write_to_db(
            data=df[specs['columns']],
            table_name=table,
            schema=specs['schema'],
            db_engine=db_engine
        )
    # municipalities = load_data_to_df(
    #    os.path.join(DATA_FILES_PATH, "most-popular-first-names-by-municipality.jsonl.gz"))
    # print(municipalities.head())


# write_to_db(data=municipality_data, table_name='municipality',
#     db_engine=engine, schema='population', dtype=municipality_dtypes)


if __name__ == "__main__":
    main()
