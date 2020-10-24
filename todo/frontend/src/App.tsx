import React, { useEffect } from 'react';


import './App.css';

function App() {

  useEffect(() => {
    fetchData();
  }, [])


  const fetchData = async () => {

    try {
      const response = await fetch(
        " http://127.0.0.1:8000/api/article-lists/"
      );
      const data = await response.json();
      console.log(data);

    } catch (error) {
      console.log(error, "FAILED TO FETCH");
    }

  };

  return (
    <div className="App">

    </div>
  );
}

export default App;
