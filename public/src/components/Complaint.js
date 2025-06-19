import React, { useState } from "react";
import { storage, db } from "../firebase"; // Import storage and db from your firebase config
import { ref, uploadBytes, getDownloadURL } from "firebase/storage";
import { collection, addDoc } from "firebase/firestore";
import "./Complaint.css";

function Complaint() {
  const [photo, setPhoto] = useState(null);
  const [name, setName] = useState("");
  const [phone, setPhone] = useState("");
  const [description, setDescription] = useState("");
  const [error, setError] = useState("");
  const [success, setSuccess] = useState("");

  const handlePhotoChange = (e) => {
    setPhoto(e.target.files[0]);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!photo) {
      setError("Please upload a photo.");
      return;
    }

    const photoRef = ref(storage, `complaints/${Date.now()}`);

    try {
      // Upload file
      const uploadResult = await uploadBytes(photoRef, photo);
      // Get download URL
      const downloadURL = await getDownloadURL(uploadResult.ref);
      console.log(downloadURL);
      //save into MA

      setSuccess("Complaint submitted successfully!");
      setName(""); // Clear the form fields after submission
      setPhone("");
      setDescription("");
      setPhoto(null);
    } catch (error) {
      setError("Submission failed: " + error.message);
    }
  };

  return (
    <div className="complaint-container">
      <h2>Complaint Form</h2>
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label htmlFor="photo">Upload Photo:</label>
          <input type="file" id="photo" onChange={handlePhotoChange} />
        </div>
        <div className="form-group">
          <label htmlFor="name">Name: (Optional)</label>
          <input
            type="text"
            id="name"
            value={name}
            onChange={(e) => setName(e.target.value)}
          />
        </div>
        <div className="form-group">
          <label htmlFor="phone">Phone Number: (Optional)</label>
          <input
            type="tel"
            id="phone"
            value={phone}
            onChange={(e) => setPhone(e.target.value)}
          />
        </div>
        <div className="form-group">
          <label htmlFor="description">Description: (Optional)</label>
          <textarea
            id="description"
            value={description}
            onChange={(e) => setDescription(e.target.value)}
          ></textarea>
        </div>
        <button type="submit">Submit</button>
        {error && <p className="error">{error}</p>}
        {success && <p className="success">{success}</p>}
      </form>
    </div>
  );
}

export default Complaint;
