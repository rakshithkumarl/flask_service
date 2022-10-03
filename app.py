from flask import Flask
import flask.scaffold
flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func
from flask_restful import Api
from views.extractor import Extract
from views.translator import Translate


# Initialize Flask
app = Flask(__name__)
api = Api(app)


# Assign routes
api.add_resource(Extract, "/extract")
api.add_resource(Translate, "/translate")


if __name__ == "__main__":
    app.run(debug=True)