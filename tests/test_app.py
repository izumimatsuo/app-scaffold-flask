from app.app import app, db
from flask import json


def test_get_users():
    response = app.test_client().get('/api/v1/users')
    assert response.status_code == 200
