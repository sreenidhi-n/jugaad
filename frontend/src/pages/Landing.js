import React from "react";
import Navbar from "../components/Navigation";
import LandingRect from "../components/LandingRect";
import Dump from "../Images/upload-dump.gif";
import Photo from "../Images/upload-folder.gif";
import { Link } from "react-router-dom";

function Landing() {
	return (
		<div>
			<Navbar />
			<div
				style={{
					flex: 1,
					display: "flex",
					justifyContent: "center",
					alignItems: "center",
				}}
			>
				<Link to="/forensic-image" style={{ textDecoration: "none" }}>
					<div
						style={{
							display: "flex",
							justifyContent: "center",
							alignItems: "center",
						}}
					>
						<LandingRect
							text="Click here to Drag and drop/choose forensic dump"
							image={Dump}
						/>
					</div>
				</Link>

				<Link to="/only-image" style={{ textDecoration: "none" }}>
					<div
						style={{
							display: "flex",
							justifyContent: "center",
							alignItems: "center",
						}}
					>
						<LandingRect
							text="Click here to dump all your photos for analysis"
							image={Photo}
						/>
					</div>
				</Link>
			</div>
		</div>
	);
}

export default Landing;
