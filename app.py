from flask import Flask, request, jsonify, make_response, session
from flask_migrate import Migrate
from flask_restful import Resource, Api
from flask_cors import CORS

from config import ApplicationConfig
from models import db, User, Agent, Message

app = Flask(__name__)

app.config.from_object(ApplicationConfig)

migrate = Migrate(app=app, db=db)

db.init_app(app=app)

CORS(app=app)
api = Api(app=app)


class Login(Resource):
    def post(self):
        email = request.get_json()['email']

        retrieved_agent = Agent.query.filter_by(email=email).first()

        print(retrieved_agent)

        if retrieved_agent:
            session['agent_id'] = retrieved_agent.id
            
            return retrieved_agent.to_dict(), 200
        
        return {}, 404
    

class Logout(Resource):
    def delete(self):
        session["agent_id"] = None

        return {}, 204
    
class CheckSession(Resource):
    def get(self):

        agent = Agent.query.filter(Agent.id == session.get('agent_id')).first()

        if agent:
            return (agent.to_dict()), 200
        else:
            return {}, 401
        

class Users(Resource):

    def post(self):
        first_name = request.get_json()["first_name"]
        last_name = request.get_json()["last_name"]
        email = request.get_json()["email"]
        phone_number = request.get_json()["phone_number"]


        if first_name and last_name and email and phone_number:

            new_user = User(first_name=first_name,last_name=last_name,email_address=email,phone_number=phone_number)

            db.session.add(new_user)
            db.session.commit()

            session["user_id"] = new_user.id

            response = make_response(jsonify(new_user.to_dict()), 201)

            return response
        else:
            response = make_response(jsonify({"error": "email already exists"}), 401)
            return response
        

class Messages(Resource):
    def get(self):
        messages = [message.to_dict() for message in Message.query.all()]

        response = make_response(jsonify(messages), 200)

        return response
    
    def post(self):
        category = request.get_json()["category"]
        body = request.get_json()["body"]
        user_id = request.get_json()["user_id"]
        agent_id = request.get_json()["agent_id"]

        message = Message(category=category, body=body, user_id=user_id,agent_id=agent_id)

        db.session.add(message)
        db.session.commit()

        response = make_response(jsonify(message.to_dict()), 201)
        
        return response


api.add_resource(Login, "/api/agents/login", endpoint="agent_login")
api.add_resource(Logout, "/api/agents/logout", endpoint="agent_logout")
api.add_resource(CheckSession, "/api/check_session", endpoint="check_session")
api.add_resource(Users, "/api/users", endpoint="users")
api.add_resource(Messages, "/api/messages", endpoint="messages")

if __name__ == "__main__":
    app.run(port=5555, debug=True)