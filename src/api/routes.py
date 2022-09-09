"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token

api = Blueprint('api', __name__)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200




@api.route('/signup', methods=['POST'])
def signup():
    data = request.get_json() 
    user = User.query.filter_by(email = data.get("email")).first()
    if user is not None:
        return "Usuario registrado", 404
    new_user = User(
        email = data.get("email"),
        password = data.get("password"),
        is_active = True
    )
    db.session.add(new_user)
    db.session.commit()

    return jsonify(new_user.serialize()), 200

    
@api.route('/login', methods=['POST'])
def login():
    data = request.get_json() 
    user = User.query.filter_by(email = data["email"], password = data["password"]).first()
    # user = User.query.filter_by(email = data.get("email"), password = data.get("password")).first()
    # las 2 lineas anteriores significan lo mismo
    if user is None:
        return "Usuario incorrecto", 401
    access_token = create_access_token(identity=user.id)
    return jsonify({ "token": access_token, "user_id": user.id, "result": "Usuario registrado correctamente"}), 200


@api.route('/private', methods=['GET'])
@jwt_required()
def private():
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)
    if user:
        return jsonify({"resultado": "acceso permitido"}), 200
    else:
        return jsonify({ "resultado": "usuario no autenticado"}), 400