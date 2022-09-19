import React from "react";
import "./Form.css";
import { useState } from "react";
const Form = () => {
  const [title, settitle] = useState("");
  const [genre, setgenre] = useState("");
  const [plataforma, setplataforma] = useState("");
  const [dev, setdev] = useState("");
  const submitHandler =(e)=>{
    e.preventDefault()
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
