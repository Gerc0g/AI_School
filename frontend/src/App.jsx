import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import InstructionsPage from './pages/InstructionsPage';
import AiAssistantPage from './pages/AiAssistantPage';
import MaterialsPage from './pages/MaterialsPage';
import MainPage from './pages/MainPage';


const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<MainPage />} />
        <Route path="/instructions" element={<InstructionsPage />} />
        <Route path="/assistant" element={<AiAssistantPage />} />
        <Route path="/materials" element={<MaterialsPage />} />
      </Routes>
    </Router>
  );
};

export default App;
