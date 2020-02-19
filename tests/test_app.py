from app.user import app
from flask import json


def test_add_users():
    response = app.test_client().post('/api/v1/users', data=json.dumps({'name': 'pytest'}), content_type='application/json')
    assert response.status_code == 201

    data = json.loads(response.get_data())
    assert data['name'] == 'pytest'


def test_delete_users():
    response = app.test_client().get('/api/v1/users')
    assert response.status_code == 200

    data = json.loads(response.get_data())
    ids = [d['id'] for d in data if d['name'] == 'pytest']
    id = ids[0]
    response = app.test_client().delete(f'/api/v1/users/{id}')
    assert response.status_code == 204
