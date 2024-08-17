import json
import logging


def test_index_route(client):
    response = client.get('/')
    assert response.status_code == 200


def test_chat_route_valid_input(client):
    data = {
        'message': 'What is the capital of France?',
        'language': 'en'
    }
    response = client.post('/chat', 
                           data=json.dumps(data),
                           content_type='application/json')
    assert response.status_code == 200
    assert 'response' in response.json
    assert response.json['response'] == "The capital of France is Paris."


def test_chat_route_empty_input(client):
    data = {
        'message': '',
        'language': 'en'
    }
    response = client.post('/chat', 
                           data=json.dumps(data),
                           content_type='application/json')
    assert response.status_code == 200
    assert response.json['response'] == 'Please enter a message.'


def test_chat_route_different_language(client):
    data = {
        'message': 'Quelle est la capitale de la France?',
        'language': 'fr'
    }
    response = client.post('/chat', 
                           data=json.dumps(data),
                           content_type='application/json')
    assert response.status_code == 200
    assert 'response' in response.json
    assert response.json['response'] == "The capital of France is Paris."


def test_chat_route_long_message(client):
    long_message = "What is the capital of France? " * 100
    data = {
        'message': long_message,
        'language': 'en'
    }
    response = client.post('/chat', 
                           data=json.dumps(data),
                           content_type='application/json')
    assert response.status_code == 200
    assert 'response' in response.json


def test_chat_route_special_characters(client):
    data = {
        'message': 'What is Python? 🐍',
        'language': 'en'
    }
    response = client.post('/chat', 
                           data=json.dumps(data),
                           content_type='application/json')
    assert response.status_code == 200
    assert 'response' in response.json
    assert response.json['response'] == "Python is a programming language."