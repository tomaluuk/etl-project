import psycopg2
import json

with open('config.json', encoding='utf-8') as f:
    config = json.load(f)
dbconfig = config['dbconfig']

conn = psycopg2.connect(
    host=dbconfig['host'],
    dbname=dbconfig['dbname'],
    user=dbconfig['user'],
    password=dbconfig['password']
)
conn.close()
