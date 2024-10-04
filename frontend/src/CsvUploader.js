import React, { useState } from 'react';

function CsvUploader() {
    const [file, setFile] = useState(null);

    const handleFileChange = (e) => {
        setFile(e.target.files[0]);
    };

    const handleUpload = async () => {
        const formData = new FormData();
        formData.append('csv_file', file);

        await fetch('http://localhost:8000/uploader/upload/', {
            method: 'POST',
            body: formData,
        });
    };

    return (
        <div>
            <input type="file" onChange={handleFileChange} />
            <button onClick={handleUpload}>Upload</button>
        </div>
    );
}

export default CsvUploader;
