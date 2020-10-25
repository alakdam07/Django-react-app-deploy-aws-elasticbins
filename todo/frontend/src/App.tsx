import React, { useEffect } from 'react';


import './App.css';

function App() {

  useEffect(() => {
    fetchData();
  }, [])


  const fetchData = async () => {

    try {
      const response = await fetch(
        "http://todo-deploy.eba-9nb6wjcm.us-east-1.elasticbeanstalk.com/api"
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
