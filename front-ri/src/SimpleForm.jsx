import React from "react";
import { useState } from "react";
import axios from 'axios'
const SimpleForm = (props) => {
  console.log(props)
  const [simple, setSimple] = useState("");
  const submitHandler =(e)=>{
    e.preventDefault()
    //localhost ta 7777 pois tenho processos rodando na 8000
    axios.post('http://localhost:7777', {'simple':simple})
    //POST
    //chama funcao externa para esconder submithandler e
    //Gerar entradas apartir da payload
    props.setmodoResultado(true)

  }
  return (
    <form className="Forms" action="" onSubmit={submitHandler}>
      <h2>Gaming Google</h2>
      <input
        id="simple"
        type="text"
        value={simple}
        onChange={(e) => setSimple(e.target.value)}
      />
      <button>Game Search</button>
    </form>
  );
};

export default SimpleForm;
