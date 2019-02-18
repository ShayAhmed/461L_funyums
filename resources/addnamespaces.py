from flask_restplus import Api
from setup.blueprint import funyums_blueprint_v1
from .hello_resource.hello import ns as hello_ns




api = Api(funyums_blueprint_v1, version='1.0',
        title='FunYums API',
        description='description for api of Funyums') #creates api 


#namespace - Group resources together
def add_all_namespaces():
    api.add_namespace(hello_ns) #adds all namespaces (operations related to specific task) to api
   

add_all_namespaces()