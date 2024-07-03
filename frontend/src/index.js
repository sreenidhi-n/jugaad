import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import DumpUpload from "./pages/DumpUpload";
import PhotoUpload from "./pages/PhotoUpload";
import Dirs from "./pages/Dirs"
import Landing from './pages/Landing';
import reportWebVitals from './reportWebVitals';
import 'bootstrap/dist/css/bootstrap.css';
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import Loading from './pages/Loading';

const router = createBrowserRouter([
	{ path: "/", element: <Landing /> },
	{
		path: "/directory",
		loader: () => {
			// Check if the user is authorized to access the /dir route
			// You can implement your own logic here, such as checking a session token or user role
			const isAuthorized = true; // Replace with your own logic

			if (isAuthorized) {
				return null; // Allow access to the /dir route
			} else {
				return <DumpUpload />;
			}
		},
		element: <Dirs />,
	},
	{ path: "/forensic-image", element: <DumpUpload /> },
	{ path: "/only-image", element: <PhotoUpload /> },
	{ path: "/loading", element: <Loading /> },
]);

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <RouterProvider router= {router}/>
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
