from flask import Flask
from flask_restful import Resource, Api, reqparse, abort, marshal, fields, request
import boto3
from boto3.dynamodb.conditions import Key
import json
from config import dynamodb, table
from botocore.exceptions import ClientError

# Initalize flask
app = Flask(__name__)
api = Api(app)

# Method calls

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
            try:
                if resp['Items'][i]['state'] == 'active':
                    getTags = resp['Items'][i]['SK']
                    value['sk'].append(getTags)
                else:
                    print("data not exist")
            except:
                print("key does not exist")
        
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
            try:
                if resp['Items'][i]['tagName'] == tagName:
                    # getVersion = {"sk":resp['Items'][i]['SK'], "version":resp['Items'][i]['version']}
                    getVersion = {"version":resp['Items'][i]['version']}
                    value['versionHistory'].append(getVersion)
                else:
                    print("data not exist")
            except:
                print("key does not exist")

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
            try:
                if resp['Items'][i]['createdBy'] == createdBy:
                    getTags = resp['Items'][i]['SK']
                    value['tagBySpecificUser'].append(getTags)
                else:
                    print("data not exist")
            except:
                print("key does not exist")
        
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
            try:
                if resp['Items'][i]['approvedStatus'] == approvedStatus:
                    getTags = resp['Items'][i]['SK']
                    value['approvedStatus'].append(getTags)
                else:
                    print("data not exist")
            except:
                print("key does not exist")
        
        return value

# 0.0.0.0:5000/addTagDetails - with json data ({
    # "PK": "COAF#SOURCE#1235",
    # "SK": "#TARGET#1234_enriched#REF#2456&2567#RETURN#DID#v3",
    # "type": "REF",
    # "version": "v3",
    # "tagName": "1234_DID_Enrichment",
    # "owner": "TFE641"
# })

class AddTagDetails(Resource):
    def __init__(self):
        pass

    def put(self):
        tag_data = request.get_json()

        if 'PK' in tag_data:
            pk = tag_data['PK']
        else:
            pk = ""

        if 'SK' in tag_data:
            sk = tag_data['SK']
        else:
            sk = ""

        if 'type' in tag_data:
            type_data = tag_data['type']
        else:
            type_data = ""

        if 'owner' in tag_data:
            owner = tag_data['owner']
        else:
            owner = ""

        if 'ownerContact' in tag_data:
            ownerContact = tag_data['ownerContact']
        else:
            ownerContact = ""

        if 'createDate' in tag_data:
            createDate = tag_data['createDate']
        else:
            createDate = ""

        if 'createdBy' in tag_data:
            createdBy = tag_data['createdBy']
        else:
            createdBy = ""

        if 'tagName' in tag_data:
            tagName = tag_data['tagName']
        else:
            tagName = ""

        if 'tagDescription' in tag_data:
            tagDescription = tag_data['tagDescription']
        else:
            tagDescription = ""

        if 'approveDate' in tag_data:
            approveDate = tag_data['approveDate']
        else:
            approveDate = ""

        if 'approvedBy' in tag_data:
            approvedBy = tag_data['approvedBy']
        else:
            approvedBy = ""

        if 'state' in tag_data:
            state = tag_data['state']
        else:
            state = ""

        if 'version' in tag_data:
            version = tag_data['version']
        else:
            version = ""

        if 'currVersion' in tag_data:
            currVersion = tag_data['currVersion']
        else:
            currVersion = ""

        if 'effectiveDate' in tag_data:
            effectiveDate = tag_data['effectiveDate']
        else:
            effectiveDate = ""

        if 'depenencies' in tag_data:
            depenencies = tag_data['depenencies']
        else:
            depenencies = ""

        if 'sourceDatasetMetadata' in tag_data:
            sourceDatasetMetadata = tag_data['sourceDatasetMetadata']
        else:
            sourceDatasetMetadata = ""

        if 'referenceDatasetMetadata' in tag_data:
            referenceDatasetMetadata = tag_data['referenceDatasetMetadata']
        else:
            referenceDatasetMetadata = ""

        if 'joinCriteria' in tag_data:
            joinCriteria = tag_data['joinCriteria']
        else:
            joinCriteria = ""

        if 'datasetName' in tag_data:
            datasetName = tag_data['datasetName']
        else:
            datasetName = ""

        if 'datasetID' in tag_data:
            datasetID = tag_data['datasetID']
        else:
            datasetID = ""

        if 'destination' in tag_data:
            destination = tag_data['destination']
        else:
            destination = ""

        tag = {
            "PK": pk,
            "SK": sk,
            "type": type_data,
            "owner": owner,
            "ownerContact": ownerContact,
            "createDate": createDate,
            "createdBy": createdBy,
            "tagName": tagName,
            "tagDescription": tagDescription,
            "approveDate": approveDate,
            "approvedBy": approvedBy,
            "state": state,
            "version": version,
            "currVersion": currVersion,
            "effectiveDate": effectiveDate,
            "depenencies": depenencies,
            "sourceDatasetMetadata": sourceDatasetMetadata,
            "referenceDatasetMetadata": referenceDatasetMetadata,
            "joinCriteria": joinCriteria,
            "datasetName": datasetName,
            "datasetID": datasetID,
            "destination": destination
        }

        put_response = table.put_item(Item=tag)
        response = {
            "statusCode": 200,
            "body": json.dumps(put_response)
        }

        print(response)
        return {'success': 'Tag added successfully'}


# 0.0.0.0:5000/deleteTag - with json data ({"PK": "COAF#SOURCE#1234","SK": "#TARGET#1234_enriched#REF#2345#RETURN#BU#v2"})

class DeleteTag(Resource):
    def __init__(self):
        pass

    def post(self):
        tag_data = request.get_json()
        pk = tag_data['PK']
        sk = tag_data['SK']

        try:
            table.update_item(
                Key={
                        'PK': pk,
                        'SK': sk
                    },
                UpdateExpression="set #s = :g",
                ConditionExpression="SK = :sk",
                ExpressionAttributeNames= {
                    '#s': "state"
                },
                ExpressionAttributeValues={
                    ':g': "delete",
                    ':sk': sk
                },
                ReturnValues="UPDATED_NEW"
            )
        except ClientError as e:
            if e.response['Error']['Code'] == "ConditionalCheckFailedException":
                print(e.response['Error']['Message'])
                return {'error': 'Tag does not exist'}
            else:
                raise
        else:
            return {'success': 'Tag deleted successfully'}

        # return {'success': 'Tag deleted successfully'}

api.add_resource(GetActiveTag, "/getActiveTag")
api.add_resource(GetTagVersionHistory, "/getTagVersionHistory")
api.add_resource(GetTagBySpecificUser, "/getTagBySpecificUser")
api.add_resource(GetTagByApprovalStatus, "/getTagByApprovalStatus")
api.add_resource(AddTagDetails, "/addTagDetails")
api.add_resource(DeleteTag, "/deleteTag")


