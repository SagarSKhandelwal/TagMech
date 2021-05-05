from flask import Flask
from flask_restful import Resource, Api, reqparse, abort, marshal, fields, request
import boto3
from boto3.dynamodb.conditions import Key
import json

# Initalize flask
app = Flask(__name__)
api = Api(app)

dynamodb = boto3.resource("dynamodb", endpoint_url="http://localhost:8000", region_name='localhost')

table = dynamodb.Table('TagsLibrary') 

print("table connected", table)     

PORT = 5000
HOST = '0.0.0.0'

# GET Method calls

# 0.0.0.0:5000/getActiveTag - with json data ({"PK":"COAF#SOURCE#1234" })

class GetActiveTag(Resource):
    def __init__(self):
        pass

    def get(self):
        pass

    def post(self):
        print("inside post")
        content = request.get_json()
        pk = content['PK']
        value = {"sk":[]}

        resp = table.query(
            KeyConditionExpression=Key('PK').eq(pk) & Key('state').eq('active')
        )

        print(resp)

        for i in range(len(resp['Items'])):
            print("inside for")
            if resp['Items'][i]['state'] == 'active':
                getTags = resp['Items'][i]['SK']
                value['sk'].append(getTags)
            else:
                print("data not exist")
        
        return value

api.add_resource(GetActiveTag, "/getActiveTag")

if __name__ == "__main__":
	print("server running in port %s" %(PORT))
	app.run(host=HOST, port=PORT)