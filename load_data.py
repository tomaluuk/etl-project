"""
  Data ingestion
"""

__author__ = "Topi Luukkanen"

import os
import logging
from fastparquet import ParquetFile
import pandas as pd

logging.basicConfig(level=logging.INFO)

DATA_FILES_PATH = "./data/"
DATA_FILES = os.listdir(DATA_FILES_PATH)


def load_jsonl_gz_data(file: str):
    """
    Load gzip-compressed jsonl data.
    :param str path: Path to file
    :return: DataFrame object of the data
    """
    logging.info(f'Reading file: {path}')
    return pd.read_json(file, lines=True, compression='gzip')


def load_parquet_data(file: str):
    """
    Load parquet data
    :param str path: Path to file
    :return DataFrame object of the data:
    """
    logging.info(f'Reading file: {path}')
    return ParquetFile(file).to_pandas()


def load_data(filepath: str):
    """"Load data from list of files. Infer filetypes."""

    if filepath.endswith('.jsonl.gz'):
        load_jsonl_gz_data(filepath)
    elif filepath.endswith('.parquet'):
        load_parquet_data(filepath)
    else:
        logging.info(
            f'Function {load_data.__name__} encountered unknown file type in file {filepath}')

    return


def main():
    """"docstring"""
    load_data(DATA_FILES_PATH)


if __name__ == "__main__":
    main()
