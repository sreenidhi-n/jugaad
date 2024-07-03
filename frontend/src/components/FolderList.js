import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';
import './Folder.css';

function FolderList() {
  const [folders, setFolders] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchFolders = async () => {
      try {
        const response = await axios.get('http://localhost:3001/folders');
        setFolders(response.data);
        setLoading(false);
      } catch (error) {
        console.error('Error fetching folders:', error);
        setLoading(false);
      }
    };

    fetchFolders();
  }, []);

  if (loading) {
    return <div>Loading...</div>;
  }

  return (
    <div className="folder-list">
      {folders.map((folder, index) => (
        <Link to={`/folder/${index}`} key={index} className="folder-item" state={{ folder }}>
          <div className="folder-thumbnail">
            {folder.File_Array.length > 0 && (
              <img src={`data:image/jpeg;base64,${folder.File_Array[0]}`} alt={folder.Folder_name} />
            )}
          </div>
          <div className="folder-name">{folder.Folder_name}</div>
          <div className="file-count">{folder.Number_of_files} files</div>
        </Link>
      ))}
    </div>
  );
}

export default FolderList;