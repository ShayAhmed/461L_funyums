from flask import Flask
from flask_restplus import Api
from werkzeug.contrib.fixers import ProxyFix
from resources.addnamespaces import add_all_namespaces
from .blueprint import all_blueprints
from importlib import import_module



app = Flask(__name__)
add_all_namespaces()



@app.route('/') #basic function to make sure app is running
def hello_world():
        return 'App is running, got to URL/v1 or http://127.0.0.1:5000/v1'


def create_app(): #creates flask app
    print("inside create_app")
    app.wsgi_app = ProxyFix(app.wsgi_app)#setup thing, dont worry about it
    retgister_blueprints(app) #adds blueprint to app
    return app



#blueprint - a set of operations which can be registered on an application
def retgister_blueprints(app): #adds blueprint to app
    print("inside register blueprint")
    import_module(all_blueprints.import_name)
    app.register_blueprint(all_blueprints)
    """
    for bp in all_blueprints:
        import_module(bp.import_name)
        app.register_blueprint(bp)
    """
