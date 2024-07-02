import React from 'react'
import Navigation from '../components/Navigation'
import FileUpload from '../components/FileUpload'; 
import ImageUpload from '../components/PicUpload';
import "./Home.css"
function DumpUpload() {
  return (
		<div class="float-container">
			<Navigation />
      <FileUpload />
		</div>
    )
}

export default DumpUpload;