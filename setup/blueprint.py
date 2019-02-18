from flask import Blueprint

#blueprint - a set of operations which can be registered on an application
def _factory(partial_module_string, url_prefix): #creates blueprint (summation of all namespaces) to add to app
    print("actually creating blueprint")
    name = partial_module_string
    import_name = 'resources.{}'.format(partial_module_string)
    blueprint = Blueprint(name, import_name, url_prefix=url_prefix)
    return blueprint


funyums_blueprint_v1 = _factory('addnamespaces', url_prefix='/v1')


all_blueprints = (funyums_blueprint_v1 )