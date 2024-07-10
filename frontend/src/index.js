import React from "react";
import ReactDOM from "react-dom/client";
import "./index.css";
import DumpUpload from "./pages/DumpUpload";
import PhotoUpload from "./pages/PhotoUpload";
import Dirs from "./pages/Dirs";
import FolderView from "./components/FolderView";
import Landing, { UnclassifiedImagesProvider } from "./pages/Landing";
import reportWebVitals from "./reportWebVitals";
import "bootstrap/dist/css/bootstrap.css";
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import Loading from "./pages/Loading";

const router = createBrowserRouter([
	{ path: "/", element: <Landing /> },
	{
		path: "/directory",
		element: <Dirs />,
	},
	{ path: "/forensic-image", element: <DumpUpload /> },
	{ path: "/only-image", element: <PhotoUpload /> },
	{ path: "/loading", element: <Loading /> },
	{ path: "/directory/folder/:id", element: <FolderView /> },
]);

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
	<React.StrictMode>
		<UnclassifiedImagesProvider>
			<RouterProvider router={router} />
		</UnclassifiedImagesProvider>
	</React.StrictMode>
);
