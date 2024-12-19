import React from 'react';
import Header from '../components/Header';
import ChatList from '../components/ChatList';
import ChatWindow from '../components/ChatWindow';
import '../App.css';

const AiAssistantPage = () => {
  return (
    <div className="app-container">
      <Header />
      <div className="main-content">
        <ChatList />
        <ChatWindow />
      </div>
    </div>
  );
};

export default AiAssistantPage;
