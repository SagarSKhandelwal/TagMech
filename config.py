import boto3

# Connection with dynamoDB
dynamodb = boto3.resource("dynamodb", endpoint_url="http://localhost:8000", region_name='localhost')

# Table name 
table = dynamodb.Table('TagsLibrary') 

# Provide host and port on which you want to run application
PORT = 5000
HOST = '0.0.0.0'