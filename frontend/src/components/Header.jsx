import React from 'react';
import { Link } from 'react-router-dom';
import './Header.css';

const Header = () => {
  return (
    <header className="header">
      <div className="header-left">
        <h1>
          <Link to="/" className="nav-button">
            Course_Friend
          </Link>
        </h1>
        <div className="divider"></div>
        <nav className="header-nav">
          <Link to="/assistant" className="nav-button">AI ассистент</Link>
          <Link to="/materials" className="nav-button">Поиск материалов</Link>
          <Link to="/instructions" className="nav-button">Инструкция</Link>
        </nav>
      </div>
      <div className="header-right">
        <button className="auth-button">Войти</button>
      </div>
    </header>
  );
};

export default Header;
