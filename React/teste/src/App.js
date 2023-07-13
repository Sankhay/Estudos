import logo from './logo.svg';
import './App.css';
import  Voyage2  from './componentes/teste.js'
import React, { useState } from 'react'

function App() {


  
  var [time2, setTime] = useState([
    {
      Nome: "Davi",
      Cor: "blue"
    }, {
      Nome: "João",
      Cor: "red"
    }
  ])
  const changeColor = (cor, Nome) => {
    setTime(time2.map(time => {
      if (time.Nome === Nome) {
        time.Cor = cor
      }
      return time;
    }))
  }
  return (
    <div>
      <h1 style={{ textAlign: "center" }}>ola</h1>
      <Voyage2 changeColor={changeColor}  time={time2}></Voyage2>
    </div>
    
  );
}

export default App;
