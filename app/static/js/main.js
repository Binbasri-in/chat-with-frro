document.addEventListener('DOMContentLoaded', function() {
    const chatMessages = document.querySelector('.chat-messages');
    const userInput = document.getElementById('user-input');
    const sendButton = document.getElementById('send-button');

    function formatDate(date) {
        return `${date.getHours()}:${date.getMinutes().toString().padStart(2, '0')}`;
    }

    function addMessage(message, isUser) {
        const messageElement = document.createElement('div');
        messageElement.classList.add('message', isUser ? 'user-message' : 'bot-message');

        const avatarElement = document.createElement('div');
        avatarElement.classList.add('message-avatar');

        // Use Font Awesome icons for avatars
        avatarElement.innerHTML = isUser ? '<i class="fas fa-user"></i>' : '<i class="fas fa-robot"></i>';

        const textElement = document.createElement('div');
        textElement.classList.add('message-text');
        textElement.textContent = message;

        const timestampElement = document.createElement('div');
        timestampElement.classList.add('message-timestamp');
        timestampElement.textContent = formatDate(new Date());

        messageElement.appendChild(avatarElement);
        messageElement.appendChild(textElement);
        messageElement.appendChild(timestampElement);
        chatMessages.appendChild(messageElement);
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }

    function sendMessage() {
        const message = userInput.value.trim();
        const selectedLanguage = document.querySelector('input[name="language"]:checked').value;
        const selectedOption = document.querySelector('input[name="option"]:checked').value;

        // if the language is not decided or option then set to default
        if (!selectedLanguage) {
            selectedLanguage = 'en';
        }
        if (!selectedOption) {
            selectedOption = '0';
        }

        if (message) {
            addMessage(message, true);
            userInput.value = '';

            fetch('/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ message: message, language: selectedLanguage, option: selectedOption }),
            })
            .then(response => response.json())
            .then(data => {
                addMessage(data.response, false);
            })
            .catch(error => {
                console.error('Error:', error);
                addMessage('Sorry, there was an error processing your request.', false);
            });
        }
    }

    sendButton.addEventListener('click', sendMessage);
    userInput.addEventListener('keydown', function(event) {
        if (event.key === 'Enter') {
            sendMessage();
            // Prevent the default behavior of the Enter key
            event.preventDefault();

            // Scroll to the bottom of the chat messages
            chatMessages.scrollTop = chatMessages.scrollHeight;

            // Clear the user input field
            userInput.value = '';
        }
    });
    
});
