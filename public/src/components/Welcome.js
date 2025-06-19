import React from 'react';
import { Link } from 'react-router-dom';
import './welcome.css'; 

function Welcome() {
  return (
    <div>
     
      <nav className="navbar">
        <div className="navbar-left">
          <h1 className="brand">Vimarsha</h1>
        </div>
        <div className="navbar-right">
          <ul className="nav-links">
            <li><Link to="/welcome">Home</Link></li>
            <li><Link to="/about">About</Link></li>
            <li><Link to="/complaint">Complaint</Link></li>
            <li><Link to="/instabot">Instabot</Link></li>
          </ul>
        </div>
      </nav>

   
      <div className="search-container">
        <input type="text" className="search-bar" placeholder="Search..." />
        <button className="search-btn">Search</button>
      </div>

      
      <div className="tabs-container">
        <button className="tab-btn">Tab 1</button>
        <button className="tab-btn">Tab 2</button>
        <button className="tab-btn">Tab 3</button>
      </div>

    
      <div className="search-results">
        <h2>Data will appear here</h2>
      </div>
    </div>
  );
}

export default Welcome;
