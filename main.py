from flask import Flask
from flask_restplus import Api
from setup.application import create_app

app = create_app()


if __name__ == '__main__':
    app.run(debug=True)