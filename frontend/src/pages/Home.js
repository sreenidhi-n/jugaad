import React from 'react'
import Navigation from '../components/Navigation'
import FileUpload from '../components/FileUpload'; 
import Image from '../components/Image';
import "./Home.css"
function Home() {
  return (
		<div>
			<Navigation />
            <Image />
            <FileUpload />
		</div>
    )
}

export default Home