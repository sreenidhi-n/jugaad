// Loading.js
import {React,createContext,useState} from "react";

function Loading() {
	
	return (
		
			<div
				style={{
					height: "100vh",
					display: "flex",
					justifyContent: "center",
					alignItems: "center",
				}}
			>
				<p>Loading...</p>
			</div>
	);
}

export default Loading;
