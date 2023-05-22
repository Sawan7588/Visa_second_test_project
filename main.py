import os, sys
import pandas as pd
import numpy as np
from Visa.constant import *
from Visa.logger import logging
from Visa.exception import CustomException
from Visa.pipeline.pipeline import Pipeline

def main():
    try:
        pipeline = Pipeline()
        pipeline.run_pipeline()

    except Exception as e:
        logging.error(f"{e}")
        

if __name__=="__main__":
    main()