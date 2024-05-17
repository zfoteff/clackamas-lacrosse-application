import os

from dotenv import load_dotenv
from players import COACHES_TABLE_NAME, PLAYERS_TABLE_NAME, TEAMS_TABLE_NAME

load_dotenv()


PLAYER_TABLE_DB_CONFIG = {
    "user": os.environ["MYSQL_USER"],
    "password": os.environ["MYSQL_PASSWORD"],
    "host": os.environ["MYSQL_HOST"],
    "table": PLAYERS_TABLE_NAME,
}

TEAMS_TABLE_DB_CONFIG = {
    "user": os.environ["MYSQL_USER"],
    "password": os.environ["MYSQL_PASSWORD"],
    "host": os.environ["MYSQL_HOST"],
    "table": TEAMS_TABLE_NAME,
}
COACHES_TABLE_DB_CONFIG = {
    "user": os.environ["MYSQL_USER"],
    "password": os.environ["MYSQL_PASSWORD"],
    "host": os.environ["MYSQL_HOST"],
    "table": COACHES_TABLE_NAME,
}
STATISTICS_TABLE_DB_CONFIG = {
    "user": os.environ["MYSQL_USER"],
    "password": os.environ["MYSQL_PASSWORD"],
    "host": os.environ["MYSQL_HOST"],
    "table": "players",
}
