import React from "react";
import Navigation from "../components/Navigation";
import ImageUpload from "../components/PicUpload";
import "./Home.css";
function PhotoUpload() {
	return (
		<div class="float-container">
			<Navigation />
			<ImageUpload />
		</div>
	);
}

export default PhotoUpload;
