// Importing React and axios
import React, { useState } from "react";
import axios from "axios";

export default function AudioUploader() {

  //Creating selectedFile constant using useState to create a state for when audiofile has been selected by the user.
  const [selectedFile, setSelectedFile] = useState(null);

  // handleFileChange sets the state of selectedFile to an object corresponding to file the user has selected.
  const handleFileChange = (event) => {
    setSelectedFile(event.target.files[0]);
  };

  // handleSubmit prevents the default form submission behavior
  // It checks if a file has been selected.
  // Creates a FormData object and makes a POST request to the "/upload" endpoint.
  const handleSubmit = (event) => {
    event.preventDefault();
    console.log(selectedFile)

    if (selectedFile) {
      const formData = new FormData();
      formData.append("audioFile", selectedFile);

      axios.post("http://localhost:5000/upload", formData, {
        headers:{
          "Content-Type": "multipart/form-data",
        },
      })
      .then((response) => {
        console.log(response)
      })
      .catch((error) => {
        console.log(error)
      });
    }
  }


  return (
    <div>
      <form onSubmit={handleSubmit}>
        <label>
          Upload Audio File:
          <input type="file" onChange={handleFileChange}/>
        </label>
        <button type="submit" disabled={!selectedFile}>
          Upload
        </button>
      </form>
    </div>
  );
}

