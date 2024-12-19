import React from 'react';
import './ChatList.css';

const ChatList = () => {
  return (
    <aside className="chat-list">
      <h2>История Чатов</h2>
      <div className="chat-placeholder">
        {/* Заглушка для списка чатов */}
        <p>Здесь будет список ваших чатов.</p>
      </div>
    </aside>
  );
};

export default ChatList;
