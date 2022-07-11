import pandas as pd
from fastparquet import ParquetFile
import json

# first_names =

pf_municipalities = ParquetFile("data/municipality-listing-2020-10-21.parquet")
# print(pf_municipalities.columns)

df_municipalities = pf_municipalities.to_pandas()

print(df_municipalities.head())
