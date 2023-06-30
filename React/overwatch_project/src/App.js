import logo from './logo.svg';
import './App.css';
import Header2 from './components/headerr'
import { useState } from 'react'

function App() {

  const [nome, setNome] = useState('')

  return (
    <div className="App">
      <Header2 valor={nome} aoAlterar = {valor => setNome(valor)}></Header2>
    </div>
  );
}

export default App;
