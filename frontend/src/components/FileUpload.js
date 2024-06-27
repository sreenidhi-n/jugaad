import React, { useState, useRef, useEffect } from "react";
import axios from "axios";
import "./FileUpload.css";
import Image from "./Image";
import { useNavigate } from "react-router-dom";
import socketIOClient from "socket.io-client";

const FileUpload = () => {
	const [files, setFiles] = useState([]);
	const [message, setMessage] = useState("");
	const dropRef = useRef(null);
	const [presence, setPresence] = useState(false);
	const [result, setResult] = useState([]);
	const navigate = useNavigate();

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
		const supportedExtensions = Array.from({ length: 100 }, (_, i) => {
			const num = (i + 1).toString().padStart(2, "0");
			return `.E${num}`;
		});
		const filteredFiles = fileList.filter((file) =>
			supportedExtensions.some((ext) => file.name.endsWith(ext))
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
						extension: "E01",
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

	const sendFilesToServer = () => {
		console.log("Data that will be sent:", result);
		const startTime = new Date().getTime();
		axios
			.post("https://servercid.run-us-west2.goorm.site/", { result })
			.then((response) => {
				setMessage(response.data.message);
				const endTime = new Date().getTime(); // End time
				const responseTime = endTime - startTime; // Calculate response time
				console.log(`Response received in ${responseTime} ms`);
				navigate("/directory");
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

	useEffect(() => {
		const socket = socketIOClient("https://servercid.run-us-west2.goorm.site"); // Replace with your Flask server URL

		socket.on("connect", () => {
			console.log("Connected to server");
		});

		socket.on("file_processed", (data) => {
			console.log("Received file_processed event:", data);
			// Process the received data here
			const { message, files } = data;
			// Update your component's state or perform other actions
		});

		return () => {
			socket.disconnect();
		};
	}, []);

	return (
		<div>
			<div
				ref={dropRef}
				onDragOver={handleDragOver}
				onDragLeave={handleDragLeave}
				onDrop={handleDrop}
				className="drop-zone"
			>
				<div id="contents">
					<Image />
					<h5>Drag & drop .E01 - .E100 files here, or click to select files</h5>
					<input
						type="file"
						onChange={handleFileChange}
						multiple
						hidden={presence}
					/>
					<center id="submit_button">
						<button
							type="submit"
							className="btn btn-primary"
							disabled={!presence}
							onClick={sendFilesToServer}
						>
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

export default FileUpload;
