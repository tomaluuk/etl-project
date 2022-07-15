import json
from sqlalchemy import create_engine


def load_config(name=None):
    """'Loads configuration from local file"""

    f = open("./config.json", encoding='utf-8')
    config = json.load(f)

    if name != None:
        return config[name]

    return config


def get_engine():
    """Returns the database engine"""
    db_config = load_config('db')
    engine = create_engine(
        f"postgresql://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['dbname']}")
    return engine
