from flask import Flask
import logging

# set up logging
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)
app.config.from_object('config')

# Ensure that Flask's logger is also set to INFO level
app.logger.setLevel(logging.INFO)

app.logger.info('App started')

from app import routes