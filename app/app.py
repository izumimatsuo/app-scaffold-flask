from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object('app.config.DevelopmentConfig')
db = SQLAlchemy(app)
Migrate(app, db)


# Models
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)

    def to_dict(self):
        return dict(
            id=self.id,
            name=self.name
        )

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<User {}>'.format(self.name)


# views
@app.route("/api/v1/users", methods=['GET', 'POST'])
def api_v1_users():
    if request.method == 'POST':
        name = request.json['name']
        d = User(name)
        db.session.add(d)
        db.session.commit()
        return jsonify(d.to_dict()), 201
    if request.method == 'GET':
        ls = User.query.all()
        ls = [l.to_dict() for l in ls]
        return jsonify(ls), 200


@app.route("/api/v1/users/<id>", methods=['DELETE'])
def api_v1_users_by_id(id):
    if request.method == 'DELETE':
        d = User.query.get(id)
        db.session.delete(d)
        db.session.commit()
        return '', 204
