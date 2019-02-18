#this file does the actual work and is called from hello.py

class service_layer:
    @staticmethod
    def get_hello():
        return {"hello":"world"}