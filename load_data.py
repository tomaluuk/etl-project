import pandas as pd
from fastparquet import ParquetFile

df_first_names = pd.read_json(
    path_or_buf='data/most-popular-first-names-by-municipality.jsonl.gz',
    lines=True,
    compression='gzip'
)

print(df_first_names.head)

pf_municipalities = ParquetFile('data/municipality-listing-2020-10-21.parquet')
df_municipalities = pf_municipalities.to_pandas()

print(df_municipalities.head())
