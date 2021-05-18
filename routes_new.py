from flask import current_app
from flask_restx import Resource

from src.api.api_def import api, responses
#from src.api.models import enrichment_response_model
from src.db.dynamo_client import DynamoClient

enrichment = api.namespace('enrichment')

@enrichment.route('/<string:pk>/<string:sk>')
@api.doc(responses=responses)
class Enrichment(Resource):
    """ API enrichment class to mock out an enrichment with namespace """

    def __init__(self, api=None, *args, **kwargs):
        self.api = api
        self.client = DynamoClient()

#@api.response(200, 'Success', enrichment_response_model)
    #@api.marshal_with(enrichment_response_model)
    def get(self,pk,sk):
        """ Enrichment GET """
        current_app.logger.info("Enrichment pinged.")
        get_resp = self.client.get_activetags(pk,sk)
        return get_resp

    def post(self):
        """ Enrichment POST """
        current_app.logger.info("Enrichment pinged.")
        return {"message": "This is a POST enrichment."}

@enrichment.route('/<string:pk>/<string:tagName>')
@api.doc(responses=responses)
class Enrichment_getTagVersionHistory(Resource):
    """ API enrichment class to mock out an enrichment with namespace """

    def __init__(self, api=None, *args, **kwargs):
        self.api = api
        self.client = DynamoClient()

#@api.response(200, 'Success', enrichment_response_model)
    #@api.marshal_with(enrichment_response_model)
    def get(self,pk,tagName):
        """ Enrichment GET """
        current_app.logger.info("Enrichment pinged.")
        get_resp = self.client.get_tagVersionHistory(pk,tagName)
        return get_resp

    def post(self):
        """ Enrichment POST """
        current_app.logger.info("Enrichment pinged.")
        return {"message": "This is a POST enrichment."}

@enrichment.route('/<string:pk>/<string:createdBy>')
@api.doc(responses=responses)
class Enrichment_getTagBySpecificUser(Resource):
    """ API enrichment class to mock out an enrichment with namespace """

    def __init__(self, api=None, *args, **kwargs):
        self.api = api
        self.client = DynamoClient()

#@api.response(200, 'Success', enrichment_response_model)
    #@api.marshal_with(enrichment_response_model)
    def get(self,pk,createdBy):
        """ Enrichment GET """
        current_app.logger.info("Enrichment pinged.")
        get_resp = self.client.get_tagBySpecificUser(pk,createdBy)
        return get_resp

    def post(self):
        """ Enrichment POST """
        current_app.logger.info("Enrichment pinged.")
        return {"message": "This is a POST enrichment."}

@enrichment.route('/<string:pk>/<string:sk>')
@api.doc(responses=responses)
class Enrichment_deleteTag(Resource):
    """ API enrichment class to mock out an enrichment with namespace """

    def __init__(self, api=None, *args, **kwargs):
        self.api = api
        self.client = DynamoClient()

#@api.response(200, 'Success', enrichment_response_model)
    #@api.marshal_with(enrichment_response_model)
    def get(self,pk,sk):
        """ Enrichment GET """
        current_app.logger.info("Enrichment pinged.")
        return {"message": "This is a GET enrichment."}

    def post(self):
        """ Enrichment POST """
        current_app.logger.info("Enrichment pinged.")
        get_resp = self.client.delete_tag(pk,sk)
        return get_resp