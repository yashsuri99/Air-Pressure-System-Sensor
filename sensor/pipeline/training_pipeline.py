from sensor.entity.config_entity import TrainingPipelineConfig, DataIngestionConfig
from sensor.exception import SensorException
from sensor.entity.artifact_entity import DataIngestionArtifact
from sensor.logger import logging
from datetime import datetime
import sys
import os
from sensor.components.data_ingestion import DataIngestion

class TrainingPipeline:
  
  def __init__(self):
    self.training_pipeline_config = TrainingPipelineConfig(timestamp=datetime.now())
    
  def start_data_ingestion(self) -> DataIngestionArtifact:
    try:
      
      self.data_ingestion_config = DataIngestionConfig(
        training_pipeline_config=self.training_pipeline_config
      )
      
      logging.info("Starting Data Ingestion")
      
      data_ingestion = DataIngestion(data_ingestion_config=self.data_ingestion_config)
      
      data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
      
      logging.info("Data Ingestion Completed and Artifact: {}".format(data_ingestion_artifact))
      
      return data_ingestion_artifact
    
    except Exception as e:
      raise SensorException(e,sys)
    
  def run_pipeline(self):
    try:
      data_ingestion_artifact: DataIngestionArtifact = self.start_data_ingestion()
    except Exception as e:
        raise SensorException(e,sys)