from dotenv import load_dotenv
import pymongo
from sensor.constants.database import DATABASE_NAME
import certifi
ca = certifi.where()
from sensor.constants.env_variable import MONGODB_URL_KEY
import os
import logging

load_dotenv()

class MongoDBClient:
  client = None
  
  def __init__(self, database_name = DATABASE_NAME) -> None:
    
    try:
      
      if MongoDBClient.client is None:
        mongodb_url = os.getenv(MONGODB_URL_KEY)
        logging.info("Retrieved MongoDB URL: {}".format(mongodb_url))
        
        if "localhost" in mongodb_url:
          MongoDBClient.client = pymongo.MongoClient(mongodb_url)
          
        else:
          MongoDBClient.client = pymongo.MongoClient(mongodb_url, tlsCAFile=ca) 
      
      self.client = MongoDBClient.client
      self.database = self.client[database_name]
      self.database_name = database_name
      
    except Exception as e:
      logging.error("Error initializing MongoDB Client: {}".format(e))
      raise