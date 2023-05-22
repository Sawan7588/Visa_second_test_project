from flask import Flask
from Visa.logger import logging
from Visa.exception import CustomException
import os, sys
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        raise Exception("We are testing our custom exception file")
    except Exception as e:
        Visa = CustomException(e, sys)
        logging.info(Visa.error_message)
        logging.info("We are testing logging module")
        return "hello World"
    

if __name__=="__main__":
    app.run(debug=True)