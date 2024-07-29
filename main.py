import sys, os
from sensor.exception import SensorException
from sensor.logger import logging
# from sensor.utils import dump_csv_file_mongo
from sensor.pipeline.training_pipeline import TrainingPipeline


def main():
    try:
        training_pipeline = TrainingPipeline()
        training_pipeline.run_pipeline()
    except Exception as e:
        print(e)
        SensorException(e, sys)


if __name__ == "__main__":
    # file_path = "aps_failure_training_set1.csv"
    # database_name = "air_pressure_system"
    # collection_name= "sensor"

    # dump_csv_file_mongo(file_path, database_name, collection_name)
    main()
