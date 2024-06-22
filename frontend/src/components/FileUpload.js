import React, { useState, useRef } from "react";
import axios from "axios";
import "./FileUpload.css";
import Image from "./Image";
const FileUpload = () => {
	const [files, setFiles] = useState([]);
	const [message, setMessage] = useState("");
	const dropRef = useRef(null);

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
		handleFiles(droppedFiles);
	};

	const handleFileChange = (event) => {
		const selectedFiles = Array.from(event.target.files);
		handleFiles(selectedFiles);
	};

	const handleFiles = (fileList) => {
		const e01Files = fileList.filter((file) => file.name.endsWith(".E01"));
		setFiles((prevFiles) => [...prevFiles, ...e01Files]);
		readAndSendFiles(e01Files);
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
				results.forEach((file) => {
					sendFileToServer(file);
				});
			})
			.catch((error) => console.error("Error reading files:", error));
	};

	const sendFileToServer = (file) => {
		axios
			.post("http://localhost:5000/upload", file)
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
					<h5>Drag & drop .E01 files here, or click to select files</h5>
					<input
						type="file"
						onChange={handleFileChange}
						multiple
						// accept=".E01"
					/>
				</div>
				<div className="file-list">
					{files.map((file, index) => (
						<div key={index}>{file.name}</div>
					))}
				</div>
			</div>
			{message && <div className="message">{message}</div>}
		</div>
	);
};

export default FileUpload;
