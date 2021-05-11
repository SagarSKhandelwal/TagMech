from flask import Flask
from app import app
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

# HOST = config['flask_app']['host']
# PORT = config['flask_app']['port']

if __name__ == "__main__":
	print("server running in port %s" %(config['flask_app']['PORT']))
	app.run(host=config['flask_app']['HOST'], port=config['flask_app']['PORT'])
