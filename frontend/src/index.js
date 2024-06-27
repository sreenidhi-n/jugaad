import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import Home from './pages/Home';
import Dirs from "./pages/Dirs"
import reportWebVitals from './reportWebVitals';
import 'bootstrap/dist/css/bootstrap.css';
import { createBrowserRouter, RouterProvider } from "react-router-dom";

const router = createBrowserRouter([
	{ path: "/", element: <Home /> },
	{
		path: "/directory",
		loader: () => {
			// Check if the user is authorized to access the /dir route
			// You can implement your own logic here, such as checking a session token or user role
			const isAuthorized = true; // Replace with your own logic

			if (isAuthorized) {
				return null; // Allow access to the /dir route
			} else {
				return <Home/>;
			}
		},
		element: <Dirs />,
	},
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
