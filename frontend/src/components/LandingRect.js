import React from 'react'
import "./LandingRect.css"
function LandingRect(Params) {
  return (
		<div id="rounded-rectangle">
			<h3>{Params.text}</h3>
			<img
				src={Params.image}
				alt="Landing"
				style={{ width: "80%", borderRadius: "25px" }}
			/>
		</div>
	);
}



export default LandingRect