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
            KeyConditionExpression=Key('PK').eq(pk)
        )

        for i in range(len(resp['Items'])):
            print("inside for")
            if resp['Items'][i]['state'] == 'active':
                getTags = resp['Items'][i]['SK']
                value['sk'].append(getTags)
            else:
                print("data not exist")
        
        return value

# 0.0.0.0:5000/getTagVersionHistory - with json data ({"PK":"COAF#SOURCE#1234","tagName": "1234_BU_Enrichment"})

class GetTagVersionHistory(Resource):
    def __init__(self):
        pass

    def get(self, tag):
        pass

    def post(self):
        print("inside post")
        content = request.get_json()
        pk = content['PK']
        tagName = content['tagName']
        value = {"versionHistory":[]}

        resp = table.query(
            KeyConditionExpression=Key('PK').eq(pk)
        )

        for i in range(len(resp['Items'])):
            if resp['Items'][i]['tagName'] == tagName:
                # getVersion = {"sk":resp['Items'][i]['SK'], "version":resp['Items'][i]['version']}
                getVersion = {"version":resp['Items'][i]['version']}
                value['versionHistory'].append(getVersion)
            else:
                print("data not exist")

        return value


# 0.0.0.0:5000/getTagBySpecificUser - with json data ({"PK":"COAF#SOURCE#1234","createdBy": "TFE641" })

class GetTagBySpecificUser(Resource):
    def __init__(self):
        pass

    def get(self, createdBy):
        pass

    def post(self):
        print("inside post")
        content = request.get_json()
        pk = content['PK']
        createdBy = content['createdBy']
        value = {"tagBySpecificUser":[]}

        resp = table.query(
            KeyConditionExpression=Key('PK').eq(pk)
        )

        for i in range(len(resp['Items'])):
            if resp['Items'][i]['createdBy'] == createdBy:
                getTags = resp['Items'][i]['SK']
                value['tagBySpecificUser'].append(getTags)
            else:
                print("data not exist")
        
        return value

# 0.0.0.0:5000/getTagByApprovalStatus/approved - call api using this url

class GetTagByApprovalStatus(Resource):
    def __init__(self):
        pass

    def get(self, approvedStatus):
        print("inside taglist get")
        value = {"approvedStatus": []}

        resp = table.query(
            KeyConditionExpression=Key('PK').eq('COAF#SOURCE#1234')
        )

        for i in range(len(resp['Items'])):
            if resp['Items'][i]['approvedStatus'] == approvedStatus:
                getTags = resp['Items'][i]['SK']
                value['approvedStatus'].append(getTags)
            else:
                print("data not exist")
        
        return value

api.add_resource(GetActiveTag, "/getActiveTag")
api.add_resource(GetTagVersionHistory, "/getTagVersionHistory")
api.add_resource(GetTagBySpecificUser, "/getTagBySpecificUser")
api.add_resource(GetTagByApprovalStatus, "/getTagByApprovalStatus")


if __name__ == "__main__":
	print("server running in port %s" %(PORT))
	app.run(host=HOST, port=PORT)