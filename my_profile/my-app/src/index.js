import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import Nav from './components/Nav';
import App from './components/App';
import reportWebVitals from './reportWebVitals';


const root = ReactDOM.createRoot(document.getElementById('profile'));
root.render(
  <React.StrictMode>
    <App />

  </React.StrictMode>
);


const Nav_ = ReactDOM.createRoot(document.getElementById('Nav_bar'));
Nav_.render(
  <React.StrictMode>
    <Nav />

  </React.StrictMode>
);




// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
