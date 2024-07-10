import React from 'react';
import { useParams, Link, useLocation } from 'react-router-dom';
import './Folder.css';

function FolderView() {
  const { id } = useParams();
  const location = useLocation();
  const folder = location.state.data;
console.log(folder);
  return (
    <div className="folder-view">
      <Link to="../.." className="back-button" relative='path' >← Back to Folders</Link>
      <h2>{folder.Folder_name}</h2>
      <div className="image-grid">
        {folder.map((image, index) => (
          <div key={index} className="image-item">
            {/* <img src={`data:image/jpeg;base64,${image}`} alt={`Image ${index + 1}`} /> */}
            <img src={image} alt={`Image ${index + 1}`} />
          </div>
        ))}
      </div>
    </div>
  );
}

export default FolderView;