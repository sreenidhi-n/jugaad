import React, { useState, useEffect , useContext} from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';
import './Folder.css';
import { unclassified_images } from "../pages/Landing";

function FolderList() {
  const [folders, setFolders] = useState({});
  const [loading, setLoading] = useState(true);
  const [sockdata, setscokdata] = useContext(unclassified_images)
  console.log(folders);
  useEffect(() => {
    setFolders(sockdata)
    setLoading(false)
  },[sockdata])
  // useEffect(() => {
  //   const fetchFolders = async () => {
  //     try {
  //       const response = await axios.get('http://localhost:3001/folders');
  //       setFolders(response.data);
  //       setLoading(false);
  //     } catch (error) {
  //       console.error('Error fetching folders:', error);
  //       setLoading(false);
  //     }
  //   };

  //   fetchFolders();
  // }, []);

  if (loading) {
    return <div>Loading...</div>;
  }

  return (
    <div className="folder-list">
      {Object.keys(folders).map((folder, index) => (
        <Link to={`folder/${index}`} key={index} className="folder-item" state={{data:folders[folder]}}>
          <div className="folder-thumbnail">
            {(
              // <img src={`data:image/jpeg;base64,${folders[folder]}`} alt={folder} />
              <img src={ folders[folder][0]} />
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