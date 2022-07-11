"""
  Data ingestion
"""

import pandas as pd
from fastparquet import ParquetFile


def load_jsonl_gz_data(path: str):
    """
    Load gzip-compressed jsonl data.
    :param str path: Path to file
    :return: DataFrame object of the data
    """

    return pd.read_json(path, lines=True, compression='gzip')


def load_parquet_data(path: str):
    """
    Load parquet data
    :param str path: Path to file
    :return DataFrame object of the data: 
    """

    return ParquetFile(path).to_pandas()


df_first_names = load_jsonl_gz_data(
    'data/most-popular-first-names-by-municipality.jsonl.gz')

print(df_first_names.head)

df_municipalities = load_parquet_data(
    'data/municipality-listing-2020-10-21.parquet')

print(df_municipalities.head())
