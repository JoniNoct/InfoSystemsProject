import flask
from flask import Blueprint,g
from flaskr.project.models import Project,TodoList,Booking
from flaskr import db
import flask_jwt_extended
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity,get_jwt
from flask_jwt_extended import jwt_required
from flaskr.auth.views import token_required
bp = Blueprint("project", __name__)



@bp.route('/',methods=["GET"])
@token_required 
def root(user):
    if user :
        
        booking =Booking.query.all()
        
        return {'data':
                    [{"number":i.number,
                    "time": i.time,
                    "phone": i.phone_number}
                    for i in booking]},\
            200
    else:
        return 401
@bp.route('/project_add', methods=["POST"])
@token_required
def put_project(user):
    print(flask.request.json)
    db.session.add(Booking(user_id=user.id,time=flask.request.json['name'],number=flask.request.json["id"],phone_number=user.phone))
    db.session.commit()
    return 'ok',200


@bp.route('/projects/delete_project', methods=["POST"])
@token_required
def delete_project(user):
    print(flask.request.json['id'])
    Booking.query.filter_by(number = flask.request.json['id']).delete()
    db.session.commit()
    return 'ok',200
