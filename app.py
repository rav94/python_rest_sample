from flask import Flask
from flask_restful import Api, Resource, reqparse
from user import users

app = Flask(__name__)
api = Api(app)

class Users(Resource):
    def get(self, name):
        for user in users:
            if(name == user["name"]):
                return user, 200
        return "User not found", 404

api.add_resource(Users, "/user/<string:name>")

app.run(debug=True)





