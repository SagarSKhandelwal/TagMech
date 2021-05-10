from flask import Flask
from app import app
from config import HOST, PORT

if __name__ == "__main__":
	print("server running in port %s" %(PORT))
	app.run(host=HOST, port=PORT)
