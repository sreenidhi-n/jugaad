import React, { useState, useRef } from "react";
import axios from "axios";
import "./PicUpload.css";
import Image from "./Image";

const ImageUpload = () => {
	const [files, setFiles] = useState([]);
	const [message, setMessage] = useState("");
	const dropRef = useRef(null);
	const [presence, setPresence] = useState(false);
	const [result, setResult] = useState();

	const handleDragOver = (event) => {
		event.preventDefault();
		event.stopPropagation();
		dropRef.current.classList.add("dragging");
	};

	const handleDragLeave = (event) => {
		event.preventDefault();
		event.stopPropagation();
		dropRef.current.classList.remove("dragging");
	};

	const handleDrop = (event) => {
		event.preventDefault();
		event.stopPropagation();
		dropRef.current.classList.remove("dragging");

		const droppedFiles = Array.from(event.dataTransfer.files);
		console.log("Dropped files:", droppedFiles); // Log dropped files
		handleFiles(droppedFiles);
	};

	const handleFileChange = (event) => {
		const selectedFiles = Array.from(event.target.files);
		console.log("Selected files:", selectedFiles); // Log selected files
		handleFiles(selectedFiles);
	};

	const handleFiles = (fileList) => {
		const supportedExtensions = [".jpg", ".jpeg", ".tiff", ".png"];
		const filteredFiles = fileList.filter((file) =>
			supportedExtensions.some((ext) => file.name.toLowerCase().endsWith(ext))
		);
		console.log("Filtered files:", filteredFiles); // Log filtered files
		setFiles(filteredFiles);
		readAndSendFiles(filteredFiles);
	};

	const readAndSendFiles = (files) => {
		const readers = files.map((file) => {
			return new Promise((resolve, reject) => {
				const reader = new FileReader();
				reader.onload = () => {
					resolve({
						name: file.name,
						content: reader.result.split(",")[1], // Extract base64 content from data URL
					});
				};
				reader.onerror = reject;
				reader.readAsDataURL(file);
			});
		});

		Promise.all(readers)
			.then((results) => {
				console.log("Files ready to be sent:", results); // Log files ready to be sent
				setResult(results);
				setPresence(true);
			})
			.catch((error) => console.error("Error reading files:", error));
	};

	const sendFilesToServer = (event) => {
		console.log("data that will be sent");
		axios
			.post("https://servercid.run-us-west2.goorm.site/", { result })
			.then((response) => {
				setMessage(response.data.message);
			})
			.catch((error) => {
				console.error("Error uploading file:", error);
				if (error.response) {
					setMessage(`Error uploading file: ${error.response.data.message}`);
				} else if (error.request) {
					setMessage("Error uploading file: No response from server");
				} else {
					setMessage(`Error uploading file: ${error.message}`);
				}
			});
	};

	return (
		<div className="float-child">
			<div
				ref={dropRef}
				onDragOver={handleDragOver}
				onDragLeave={handleDragLeave}
				onDrop={handleDrop}
				className="drop-zone"
			>
				<div id="contents">
					<Image />
					<h5>Drag & drop images files here, or click to select files</h5>
					<input type="file" onChange={handleFileChange} multiple hidden={presence} />
					<center id="submit_button">
						<button type="submit" className="btn btn-primary" disabled={!presence} onClick={sendFilesToServer}>
							Submit
						</button>
					</center>
				</div>

				<div className="file-list">
					{files.map((file, index) => (
						<p key={index}>{file.name}</p>
					))}
				</div>
			</div>
			{message && <div className="message">{message}</div>}
		</div>
	);
};

export default ImageUpload;
