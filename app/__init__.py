from flask import Flask
import logging

# set up logging
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)
app.config.from_object('config')

app.logger.info('App started')


from app import routes