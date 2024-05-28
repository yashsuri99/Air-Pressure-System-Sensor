import sys
from sensor.exception import SensorException
from sensor.logger import logging
from sensor.utils import dump_csv_file_mongo

# def test_exception():
#   try:
#     logging.info("failed case")
#     a = 1/0
#   except Exception as e:
#     logging.info("error occurred")
#     raise SensorException(e,sys)



if __name__ == "__main__":
  # try:
  #   test_exception()
  # except Exception as e:
  #   print(e)
  
  file_path = "aps_failure_training_set1.csv"
  database_name = "air_pressure_system"
  collection_name= "sensor"
  
  dump_csv_file_mongo(file_path, database_name, collection_name)