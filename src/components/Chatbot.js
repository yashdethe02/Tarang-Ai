import React, { useState } from 'react';

const Chatbot = () => {
    const [messages, setMessages] = useState([]);
    const [input, setInput] = useState('');

    const handleSend = async () => {
        if (input.trim()) {
            setMessages([...messages, { text: input, sender: 'user' }]);
            const userMessage = input;
            setInput('');

            // Simulate bot typing animation
            setMessages(prevMessages => [...prevMessages, { text: 'Bot is typing...', sender: 'bot' }]);

            try {
                const response = await fetch('/chat', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ message: userMessage })
                });
                const data = await response.json();
                setMessages(prevMessages => prevMessages.slice(0, -1)); // Remove 'Bot is typing...'
                setMessages(prevMessages => [...prevMessages, { text: data.response, sender: 'bot' }]);
            } catch (error) {
                console.error('Error:', error);
                setMessages(prevMessages => prevMessages.slice(0, -1)); // Remove 'Bot is typing...'
                setMessages(prevMessages => [...prevMessages, { text: 'Error: Could not get response', sender: 'bot' }]);
            }
        }
    };

    return (
        <div className="chatbot">
            <div className="chatbot-messages">
                {messages.map((msg, index) => (
                    <div key={index} className={`message ${msg.sender}`}>
                        {msg.text}
                    </div>
                ))}
            </div>
            <div className="chatbot-input">
                <input
                    type="text"
                    value={input}
                    onChange={(e) => setInput(e.target.value)}
                    onKeyPress={(e) => e.key === 'Enter' && handleSend()}
                />
                <button onClick={handleSend}>Send</button>
            </div>
        </div>
    );
};

export default Chatbot;
