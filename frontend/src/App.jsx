import { useState } from 'react'
import './App.css'

function App() {
  const [msg, setMsg] = useState("");

  const testBackend = async () => {
    const res = await fetch("http://127.0.0.1:8000/ping");
    const data = await res.json();
    setMsg(data.message);
  };

  return (
    <div className="container">
      <h1>Student Performance ML</h1>
      <button onClick={testBackend}>Test Backend</button>
      <p>{msg}</p>
    </div>
  );
}

export default App;
