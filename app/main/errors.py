from flask import Flask
from config import config_options

#Initializing app
def app(config_name):
  app = Flask(__name__)


  # creating  the app configurations
  app.config.from_object(config_options[config_name])
