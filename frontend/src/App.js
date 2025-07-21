import './App.css';
import React, { useState } from 'react';
import MovieGallery from './MovieGallery';
import Login from './Login';

function App() {
  const [token, setToken] = useState(null);

  return (
    <div className="App">
      {!token ? (
        <Login setToken={setToken} />
      ) : (
        <MovieGallery token={token} />
      )}
    </div>
  );
}

export default App;
