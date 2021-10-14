from flask import Flask
from flask_restful import Api, Resource

# create a flask app/server
app = Flask(__name__)
# rap the app with 'Api' - initialize the fact we are using a rest api to serve data to the frontend
api = Api(app)

if __name__ == "__main__":
    app.run(debug=True)
