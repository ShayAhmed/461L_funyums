from flask import request, abort
from flask_restplus import Resource, Namespace
from .service_layer import service_layer

#namespace - Group resources together
#resource - whatever thing is accessed by the URL you supply ex. someones account data
#JSON - how resource is represented
ns = Namespace('hello', description='Operations related to hello') #add hello namespace, which is all operations related to hello activity


@ns.route('/')
class HelloWorld(Resource):

    def get(self): # http get method, returns hello world
        print("get method from class HelloWorld")
        return service_layer.get_hello()
        