from flask import render_template, request, jsonify, redirect, url_for, flash
from app import app
from app.rag import get_rag_response

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']
    language = request.json['language']
    
    # log the user request
    app.logger.info(f'User ({language}) asked: {user_message}')
    
    if not user_message:
        app.logger.info('User did not enter a message')
        return jsonify({'response': 'Please enter a message.'})
    
    bot_response = get_rag_response(user_message)
    app.logger.info(f'Bot responded: {bot_response}')
    
    return jsonify({'response': bot_response})
