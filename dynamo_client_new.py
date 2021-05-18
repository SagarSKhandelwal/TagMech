import os

import boto3
from boto3.dynamodb.conditions import Key
from boto3.exceptions import Boto3Error
from botocore.exceptions import ClientError
from flask import current_app
from src.helpers.error_handling import InvalidUsage


class DynamoClient:
    """
    Database client for Dynamo
    """

    def __init__(self, client=None):
        try:
            self.region = current_app.config['REGION']
            self.table_name = current_app.config['DYNAMODB_TABLE']
            self.env = os.environ.get('FLASK_ENV') or 'testing'
            if self.env in ['DEV', 'testing'] and not client:
                self.url = current_app.config['DYNAMODB_ENDPOINT']
                current_app.logger.info(self.url)
                self.client = boto3.client("dynamodb", region_name='localhost',
                    endpoint_url=self.url,aws_access_key_id =current_app.config['ACCESS_KEY_ID'] , 
                    aws_secret_access_key=current_app.config['ACCESS_KEY'])
            elif client:
                self.client = client
            else:
                self.client = boto3.client("dynamodb", region_name=self.region,
                    endpoint_url=self.url)
        except Exception as err:
            msg = 'Local dynamo failed to initialize.'
            raise InvalidUsage(msg, 400, err)

        # TODO methods to grab data from dynamo and methods to put data in dynamo

    def get_activetags(self, pk,sk):
        current_app.logger.info(f'Querying dynamo table...')
        try:
           input = { "TableName": self.table_name,
            "KeyConditionExpression": "#e14e0 = :e14e0",
            "ExpressionAttributeNames": {"#e14e0":"PK"},
            "ExpressionAttributeValues": {":e14e0": {"S":pk}}}
           response = self.client.query(**input)
           current_app.logger.info("Query successful.")
           current_app.logger.info(response)
           return response
        except ClientError as err:
            msg = 'failed to retrieve data %s', pk, sk
            raise InvalidUsage(msg, 400, err)

    def get_tagVersionHistory(self, pk,tagName):
        current_app.logger.info(f'Querying get_tagVersionHistory table...')
        try:
           input = { "TableName": self.table_name,
            "KeyConditionExpression": "#e14e0 = :e14e0" & "tagName = :tagName",
            "ExpressionAttributeNames": {"#e14e0":"PK"},
            "ExpressionAttributeValues": {":e14e0": {"S":pk}, ":tagName": tagName}}
           response = self.client.query(**input)
           current_app.logger.info("Query successful.")
           current_app.logger.info(response)
           return response
        except ClientError as err:
            msg = 'failed to retrieve data %s', pk, tagName
            raise InvalidUsage(msg, 400, err)

    def get_tagBySpecificUser(self, pk,createdBy):
        current_app.logger.info(f'Querying get_tagBySpecificUser table...')
        try:
           input = { "TableName": self.table_name,
            "KeyConditionExpression": "#e14e0 = :e14e0" & "createdBy = :createdBy",
            "ExpressionAttributeNames": {"#e14e0":"PK"},
            "ExpressionAttributeValues": {":e14e0": {"S":pk}, ":createdBy": createdBy}}
           response = self.client.query(**input)
           current_app.logger.info("Query successful.")
           current_app.logger.info(response)
           return response
        except ClientError as err:
            msg = 'failed to retrieve data %s', pk, createdBy
            raise InvalidUsage(msg, 400, err)

    def delete_tag(self, pk,sk):
        current_app.logger.info(f'Querying delete_tag table...')
        try:
           input = { "TableName": self.table_name,
            "UpdateExpression":"set #s = :value",
            "KeyConditionExpression": "#e14e0 = :e14e0" & "skvalue = :skvalue",
            "ExpressionAttributeNames": {"#e14e0":"PK", "#skvalue": "SK", "#s": "state"},
            "ExpressionAttributeValues": {":e14e0": {"S":pk}, ":skvalue": {"S":sk}, ":value": 'delete'},
            "ReturnValues":"UPDATED_NEW"}
           response = self.client.query(**input)
           current_app.logger.info("Query successful.")
           current_app.logger.info(response)
           return response
        except ClientError as err:
            msg = 'failed to update data %s', pk, sk
            raise InvalidUsage(msg, 400, err)

