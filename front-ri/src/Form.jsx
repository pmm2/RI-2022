import React from "react";
import "./Form.css";
import { useState } from "react";
import axios from "axios";
const Form = (props) => {
  const [title, settitle] = useState("");
  const [price, setprice] = useState();
  const [genre, setgenre] = useState("");
  const [plataforma, setplataforma] = useState("");
  const [dev, setdev] = useState("");
  const submitHandler = (e) => {
    e.preventDefault();
    //localhost ta 7777 pois tenho processos rodando na 8000
    axios
      .post("http://localhost:7777", {
        title: title,
        price: price,
        genre: genre,
        plataforma: plataforma,
        dev: dev,
      }).then((resp) => {
        props.setmodoResultado(true);
        props.setresultados(JSON.parse(resp.data));
      });
      props.setmodoResultado(true);
    //POST
    //chama funcao externa para esconder submithandler e
    //Gerar entradas apartir da payload

    // settitle("");
    // setprice("");
    // setgenre("");
    // setplataforma("");
    // setdev("");
  };
  return (
    <form className="Forms" action="" onSubmit={submitHandler}>
      <label htmlFor="title">Título</label>
      <input
        id="title"
        type="text"
        value={title}
        onChange={(e) => settitle(e.target.value)}
      />
      <label htmlFor="title">Preço</label>
      <input
        id="price"
        type="number"
        value={price}
        onChange={(e) => setprice(e.target.value)}
      />
      <label htmlFor="genre">Gênero</label>
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
