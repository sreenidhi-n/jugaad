import React from 'react'
import Navigation from '../components/Navigation'
import FileUpload from '../components/FileUpload'; 
import "./Home.css"
function Home() {
  return (
		<div>
			<Navigation />
      <FileUpload />
		</div>
    )
}

export default Home