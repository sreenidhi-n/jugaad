import React, {useState,createContext} from "react";
import Navbar from "../components/Navigation";
import LandingRect from "../components/LandingRect";
import Dump from "../Images/upload-dump.gif";
import Photo from "../Images/upload-folder.gif";
import { Link } from "react-router-dom";

export const unclassified_images = createContext();

function Landing() {
	const [unclimg, setunclimg] = useState({});
	return (
		<unclassified_images.Provider value={[unclimg, setunclimg]}>
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
		</unclassified_images.Provider>
	);
}

export default Landing;

export const UnclassifiedImagesProvider = (Params) => {
	const [images, setImages] = useState([]);

	return (
		<unclassified_images.Provider value={[images, setImages]}>
			{Params.children}
		</unclassified_images.Provider>
	);
};