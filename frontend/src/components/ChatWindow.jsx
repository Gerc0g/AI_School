import React, { useState } from 'react';
import './ChatWindow.css';
import { sendMessage } from '../services/api_chat';
import 'bootstrap/dist/css/bootstrap.min.css';
import Message from './Message';

const ChatWindow = () => {
  const [messages, setMessages] = useState([
    { sender: 'ai', text: 'Здравствуйте! Как я могу помочь вам сегодня?' },
  ]);
  const [input, setInput] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleSend = async (e) => {
    e.preventDefault();
    if (input.trim() === '') return;

    const userMessage = { sender: 'human', text: input };
    setMessages((prev) => [...prev, userMessage]);
    setInput('');
    setIsLoading(true);
    setError(null);

    try {
      const aiResponse = await sendMessage(input);
      const aiMessage = { sender: 'ai', text: JSON.stringify(aiResponse) };
      setMessages((prev) => [...prev, aiMessage]);
    } catch (err) {
      console.error(err);
      setError('Не удалось отправить сообщение. Попробуйте снова.');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <section className="chat-window">
      <h2>Чат</h2>
      <div className="chat-placeholder">
        <div className="messages">
          {messages.map((msg, index) => (
            <Message key={index} sender={msg.sender} text={msg.text} />
          ))}
          {isLoading && (
            <div className="message ai">
              <div className="message-content">
                <p>Печатает...</p>
              </div>
            </div>
          )}
        </div>
        {error && <div className="error">{error}</div>}
      </div>
      <form className="chat-form" onSubmit={handleSend}>
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Введите ваше сообщение..."
          disabled={isLoading}
        />
        <button type="submit" disabled={isLoading}>
          Отправить
        </button>
      </form>
    </section>
  );
};

export default ChatWindow;
