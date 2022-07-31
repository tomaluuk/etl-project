"""Utility functions to help keeping code clean."""
import os
import json
import logging
import pandas as pd
from fastparquet import ParquetFile
from sqlalchemy import create_engine


def load_config(name=None):
    """'Loads configuration from local file"""

    with open('/opt/airflow/dags/tomaluuk/config.json', encoding='utf-8') as f:
        config = json.load(f)

    if name is not None:
        return config[name]

    return config


def get_engine():
    """Returns the database engine"""
    db_config = load_config('db_connection')
    engine = create_engine(
        f"postgresql+psycopg2://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['dbname']}")
    return engine


def load_jsonl_gz_data(file: str):
    """
    Load gzip-compressed jsonl data.
    :param str path: Path to file
    :return: DataFrame object of the data
    """
    logging.info(f'Reading file: {file}')
    return pd.read_json(file, lines=True, compression='gzip')


def load_parquet_data(file: str):
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
    logging.error(
        f'Function {load_data_to_df.__name__} encountered unknown file type in file {filepath}')

    return None
