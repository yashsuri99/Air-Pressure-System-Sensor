from dataclasses import dataclass
import os
import pymongo


@dataclass
class EnviormentVariable:
    mongo_db_url: str = os.getenv("MONGO_DB_URL")


env_var = EnviormentVariable()

mongo_client = pymongo.MongoClient(env_var.mongo_db_url)
