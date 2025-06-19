import React, { useState } from "react";
import { Link } from "react-router-dom";
import "./welcome.css";
import MapComponent from "./MapComponent";
function Instabot() {
  const [activeForm, setActiveForm] = useState("username");

  const handleFormToggle = (form) => {
    setActiveForm(form);
  };

  return (
    <div>
      <nav className="navbar">
        <div className="navbar-left">
          <h1 className="brand">Vimarsha</h1>
        </div>
        <div className="navbar-right">
          <ul className="nav-links">
            <li>
              <Link to="/welcome">Home</Link>
            </li>
            <li>
              <Link to="/about">About</Link>
            </li>
            <li>
              <Link to="/complaint">Complaint</Link>
            </li>
            <li>
              <Link to="/instabot">Instabot</Link>
            </li>
          </ul>
        </div>
      </nav>

      <div
        style={{
          padding: "20px",
          maxWidth: "600px",
          margin: "20px auto",
          backgroundColor: "#ecf0f1",
          borderRadius: "10px",
          boxShadow: "0 0 10px rgba(0, 0, 0, 0.1)",
        }}
      >
        <h2>Instagram Bot</h2>

        <div
          style={{
            display: "flex",
            justifyContent: "center",
            marginBottom: "20px",
          }}
        >
          <button
            style={{
              flex: "1",
              padding: "10px",
              marginRight: "10px",
              cursor: "pointer",
              backgroundColor:
                activeForm === "username" ? "#007bff" : "#f4f4f4",
              color: activeForm === "username" ? "white" : "black",
              border: "1px solid #ddd",
              borderRadius: "5px",
              textAlign: "center",
            }}
            onClick={() => handleFormToggle("username")}
          >
            By Username
          </button>
          <button
            style={{
              flex: "1",
              padding: "10px",
              cursor: "pointer",
              backgroundColor:
                activeForm === "hashtags" ? "#007bff" : "#f4f4f4",
              color: activeForm === "hashtags" ? "white" : "black",
              border: "1px solid #ddd",
              borderRadius: "5px",
              textAlign: "center",
            }}
            onClick={() => handleFormToggle("hashtags")}
          >
            By Hashtags
          </button>
        </div>

        <div
          style={{
            backgroundColor: "#fff",
            padding: "20px",
            borderRadius: "10px",
            boxShadow: "0 0 10px rgba(0, 0, 0, 0.1)",
          }}
        >
          {activeForm === "username" && (
            <>
              <input
                type="text"
                style={{
                  width: "100%",
                  padding: "10px",
                  marginBottom: "10px",
                  border: "1px solid #ddd",
                  borderRadius: "5px",
                }}
                placeholder="Enter Instagram Username"
              />
              <button
                style={{
                  padding: "10px 20px",
                  backgroundColor: "#007bff",
                  color: "white",
                  border: "none",
                  cursor: "pointer",
                  borderRadius: "5px",
                }}
              >
                Submit
              </button>
            </>
          )}

          {activeForm === "hashtags" && (
            <>
              <input
                type="text"
                style={{
                  width: "100%",
                  padding: "10px",
                  marginBottom: "10px",
                  border: "1px solid #ddd",
                  borderRadius: "5px",
                }}
                placeholder="Enter Hashtags"
              />
              <button
                style={{
                  padding: "10px 20px",
                  backgroundColor: "#007bff",
                  color: "white",
                  border: "none",
                  cursor: "pointer",
                  borderRadius: "5px",
                }}
              >
                Submit
              </button>
            </>
          )}
        </div>
      </div>
      {/* <MapComponent /> */}
    </div>
  );
}

export default Instabot;
