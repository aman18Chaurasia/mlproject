import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object
from pathlib import Path
from dataclasses import dataclass
from src.logger import logger

ARTIFACTS_DIR = Path("artifacts")

class PredictPipeline:
    def __init__(self):
        pass
    
    def predict(self,features):
        try:
            logger.info(f"Received features for prediction:\n{features}")
            
            model_path=ARTIFACTS_DIR / "model.pkl"
            preprocessor_path=ARTIFACTS_DIR / "preprocessor.pkl"
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled)
            
            logger.info(f"Prediction output: {preds.tolist()}")
            
            return preds
        except Exception as e:
            raise CustomException(e,sys)
    
    
@dataclass
class CustomData:
    gender: str
    race_ethnicity: str
    parental_level_of_education: str
    lunch: str
    test_preparation_course: str
    reading_score: int
    writing_score: int
        
    def get_data_as_data_frame(self):
        try:
            data = pd.DataFrame([self.__dict__])
            # Ensure correct column order
            return data[[
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course",
                "reading_score",
                "writing_score",
            ]]
        except Exception as e:
            raise CustomException(e, sys)   
            
               