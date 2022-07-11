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


df_first_names = load_jsonl_gz_data(
    'data/most-popular-first-names-by-municipality.jsonl.gz')

print(df_first_names.head)

pf_municipalities = ParquetFile('data/municipality-listing-2020-10-21.parquet')
df_municipalities = pf_municipalities.to_pandas()

print(df_municipalities.head())
