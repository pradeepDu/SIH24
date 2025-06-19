import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Login from './components/Login';      
import Welcome from './components/Welcome'; 
import Instabot from './components/Instabot'; 
import Complaint from './components/Complaint'; 
function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/welcome" element={<Welcome />} />
        <Route path="/instabot" element={<Instabot />} />
        <Route path="/complaint" element={<Complaint />} />
      </Routes>
    </Router>
  );
}

export default App;
