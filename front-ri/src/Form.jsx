import React from "react";
import "./Form.css";
import { useState } from "react";
import axios from 'axios'
const Form = (props) => {
  const [title, settitle] = useState("");
  const [genre, setgenre] = useState("");
  const [plataforma, setplataforma] = useState("");
  const [dev, setdev] = useState("");
  const submitHandler =(e)=>{
    e.preventDefault()
    axios({
        method:'post',
        url:'http://127.0.0.1:8000'
    });
    //POST
    //chama funcao externa para esconder submithandler e
    //Gerar entradas apartir da payload
    props.setmodoResultado(true)
    settitle('')
    setgenre('')
    setplataforma('')
    setdev('')
  }
  return (
    <form className="Forms" action="" onSubmit={submitHandler}>
      <label htmlFor="title">Titulo</label>
      <input
        id="title"
        type="text"
        value={title}
        onChange={(e) => settitle(e.target.value)}
      />
      <label htmlFor="genre">Genero</label>
      <input
        id="genre"
        type="text"
        value={genre}
        onChange={(e) => setgenre(e.target.value)}
      />
      <label htmlFor="plataforma">Plataforma</label>
      <input
        id="plataforma"
        type="text"
        value={plataforma}
        onChange={(e) => setplataforma(e.target.value)}
      />
      <label htmlFor="dev">Desenvolvedor</label>
      <input
        id="dev"
        type="text"
        value={dev}
        onChange={(e) => setdev(e.target.value)}
      />
      <button>Game Search</button>
    </form>
  );
};

export default Form;
