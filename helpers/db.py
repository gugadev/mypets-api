import json
import records
# import config.db as config

def connect():
  config = None
  with open("src/config/db.json", encoding="UTF-8") as data:
    config = json.loads(data.read())
  host = config["host"]
  dbname = config["db"]
  user = config["user"]
  pwd = config["pwd"]
  port = config["port"]
  return records.Database(f"postgres://{user}:{pwd}@{host}:{port}/{dbname}")

def local_connect():
  return records.Database("sqlite:///pets.db")
