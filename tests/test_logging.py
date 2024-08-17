import logging
import json
import pytest
from app import app


def test_logging(caplog):
    caplog.set_level(logging.INFO)
    
    with app.test_client() as client:
        with client.session_transaction() as session:
            data = {
                'message': 'Test message',
                'language': 'en'
            }
            response = client.post('/chat', 
                        data=json.dumps(data),
                        content_type='application/json')
    
    assert 'User (en) asked: Test message' in caplog.text
    assert 'Bot responded:' in caplog.text
    print(caplog.text)  # This will help us see what's actually in the logs
