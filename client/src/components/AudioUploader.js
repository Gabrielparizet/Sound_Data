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
      <body class="px-16 py-6">
        <div id="drop-zone" class="border-2 border-dashed border-gray-300 p-4 rounded-lg shadow-inner text-center">
          <form class="font-bold mt-12 pb-2" onSubmit={handleSubmit}>
            <label class="mb-2 ">
              Drag and drop audio file here:
              <input type="file" onChange={handleFileChange}/>
            </label>
            <button class="bg-gray-300 hover:bg-gray-400 text-gray-800 font-bold py-2 px-4 rounded inline-flex items-center" type="submit" disabled={!selectedFile}>
              <svg class="fill-current w-4 h-4 mr-2" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20"><path d="M13 8V2H7v6H2l8 8 8-8h-5zM0 18h20v2H0v-2z"/></svg>
              <span>Upload</span>
            </button>
          </form>
        </div>
      </body>
    </div>
  );
}

