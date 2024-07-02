import {React,useState} from "react";
import "./checklist.css";

const req_json = {};

function Checkslist(Params) {
	const [hidden, sethidden] = useState(false)
	const categories = {
		General: ["Flags", "Food", "Jewelry", "Maps"],
		Money: ["Credit cards", "Money"],
		People: ["Faces", "Gatherings", "Hand hold object", "Nudity", "Tattoos"],
		Places: ["Beach", "Hotel rooms", "Pool", "Restaurant"],
		Substance: ["Cigarettes", "Drugs"],
		Tech: ["Camera", "Smartphones"],
		Textual: [
			"Barcodes and QR codes",
			"Documents",
			"Handwriting",
			"Invoices",
			"Photo IDs",
			"Screenshots",
		],
		Transportation: [
			"Cars",
			"License plates",
			"Motorcycles",
			"Vehicle dashboards",
		],
		Violence: ["Fire and Explosion", "Weapons"],
	};

	Object.keys(categories).forEach((category) => {
		categories[category].forEach((item) => {
			req_json[item] = false;
		});
	});

	const handleCheckboxChange = (item, event) => {
		const checked = event.target.checked;
		req_json[item] = checked;
		console.log(req_json); // Log the updated req_json
	};

	const handleClose = () => {
		// Handle the close button click, possibly hiding the component
		console.log("Checklist closed");
		Params.reset()
		sethidden(true);
	};

	const handleSubmit = () => {
		// Handle the submit button click, possibly submitting the req_json
		console.log("Checklist submitted", req_json);
		//have to do a post request here 
	};

	return (
		<div id="blur_bag">
			<div className="category-container" hidden={hidden}>
				{Object.keys(categories).map((category) => (
					<div key={category} className="category-section">
						<h5>{category}</h5>
						<ul>
							{categories[category].map((item) => (
								<li key={item} className="list-group-item">
									<input
										className="form-check-input me-1"
										type="checkbox"
										onChange={(event) => handleCheckboxChange(item, event)}
									/>
									{item}
								</li>
							))}
						</ul>
					</div>
				))}

				<div className="button-container">
					<button className="close-button" onClick={handleClose}>
						Close
					</button>
					<button className="submit-button" onClick={handleSubmit}>
						Submit
					</button>
				</div>
			</div>
		</div>
	);
}

export default Checkslist;
