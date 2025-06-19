import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

function Login() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [showPassword, setShowPassword] = useState(false);
  const [isDarkMode, setIsDarkMode] = useState(false);
  const [error, setError] = useState(''); 
  const navigate = useNavigate();

  const handleSubmit = (e) => {
    e.preventDefault();
    if (username === 'admin' && password === 'password') {
      navigate('/welcome');
    } else {
      setError('Invalid username or password');
    }
  };

  const togglePasswordVisibility = () => {
    setShowPassword(!showPassword);
  };

  const toggleDarkMode = () => {
    setIsDarkMode(!isDarkMode);
  };

  const containerStyle = {
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center',
    height: '100vh',
    backgroundColor: isDarkMode ? '#333' : '#f0f2f5',
    color: isDarkMode ? '#fff' : '#333',
    position: 'relative',
  };

  const formStyle = {
    padding: '20px',
    borderRadius: '8px',
    boxShadow: isDarkMode ? '0 0 10px rgba(255, 255, 255, 0.2)' : '0 0 10px rgba(0, 0, 0, 0.2)',
    backgroundColor: isDarkMode ? '#444' : '#fff',
    width: '90%',
    maxWidth: '400px',
    textAlign: 'center',
  };

  const inputStyle = {
    width: '100%',
    padding: '10px',
    margin: '10px 0',
    borderRadius: '4px',
    border: isDarkMode ? '1px solid #666' : '1px solid #ccc',
    fontSize: '16px',
    backgroundColor: isDarkMode ? '#555' : '#fff',
    color: isDarkMode ? '#fff' : '#000',
    boxSizing: 'border-box',
    position: 'relative',
  };

  const buttonStyle = {
    width: '100%',
    padding: '10px',
    backgroundColor: '#4CAF50',
    color: '#fff',
    border: 'none',
    borderRadius: '4px',
    fontSize: '16px',
    cursor: 'pointer',
  };

  const moonButtonStyle = {
    position: 'absolute',
    top: '10px',
    right: '10px',
    fontSize: '24px',
    cursor: 'pointer',
    backgroundColor: 'transparent',
    border: 'none',
    color: isDarkMode ? '#fff' : '#000',
  };

  const toggleButtonStyle = {
    position: 'absolute',
    right: '10px',
    top: '50%',
    transform: 'translateY(-50%)',
    backgroundColor: 'transparent',
    border: 'none',
    cursor: 'pointer',
    color: isDarkMode ? '#fff' : '#000',
    fontSize: '14px',
  };

  const errorStyle = {
    color: 'red',
    fontSize: '14px',
    marginTop: '10px',
  };

  return (
    <div style={containerStyle}>
      <button style={moonButtonStyle} onClick={toggleDarkMode}>
        {isDarkMode ? '🌕' : '🌑'}
      </button>
      <div style={formStyle}>
        <h2>Login</h2>
        <form onSubmit={handleSubmit}>
          <input
            type="text"
            placeholder="Username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            style={inputStyle}
            required
          />
          <div style={{ position: 'relative' }}>
            <input
              type={showPassword ? 'text' : 'password'}
              placeholder="Password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              style={inputStyle}
              required
            />
            <button
              type="button"
              onClick={togglePasswordVisibility}
              style={toggleButtonStyle}
              aria-label={showPassword ? 'Hide password' : 'Show password'}
            >
              {showPassword ? '👁️' : '👁️'}
            </button>
          </div>
          {error && <div style={errorStyle}>{error}</div>} {/* Display error message */}
          <button type="submit" style={buttonStyle}>Login</button>
        </form>
      </div>
    </div>
  );
}

export default Login;

