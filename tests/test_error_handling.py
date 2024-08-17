import json
import pytest

def test_chat_route_invalid_json(client):
    response = client.post('/chat', 
                           data='invalid json',
                           content_type='application/json')
    assert response.status_code == 400

def test_chat_route_missing_fields(client):
    data = {
        'message': 'Hello'
        # 'language' field is missing
    }
    response = client.post('/chat', 
                           data=json.dumps(data),
                           content_type='application/json')
    assert response.status_code == 200