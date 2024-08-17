from app.rag import get_rag_response, knowledge_base
import pytest

def test_get_rag_response():
    query = "What is Python?"
    response = get_rag_response(query)
    assert response == "Python is a programming language."

def test_get_rag_response_no_match():
    query = "What is the population of Tokyo?"
    response = get_rag_response(query)
    assert response in knowledge_base
