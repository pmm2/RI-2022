import React from "react";
import { useState } from "react";
import axios from "axios";
import { Button, Form } from "react-bootstrap";
const SearchForm = (props) => {
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
      })
      .then((resp) => {
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
    <Form className="Forms" action="" onSubmit={submitHandler}>
      <Form.Label htmlFor="title">Título</Form.Label>
      <Form.Control
        id="title"
        type="text"
        value={title}
        onChange={(e) => settitle(e.target.value)}
      />
      <Form.Label htmlFor="title">Preço</Form.Label>
      <Form.Control
        id="price"
        type="number"
        value={price}
        onChange={(e) => setprice(e.target.value)}
      />
      <Form.Label htmlFor="genre">Gênero</Form.Label>
      <Form.Control
        id="genre"
        type="text"
        value={genre}
        onChange={(e) => setgenre(e.target.value)}
      />
      <Form.Label htmlFor="plataforma">Plataforma</Form.Label>
      <Form.Control
        id="plataforma"
        type="text"
        value={plataforma}
        onChange={(e) => setplataforma(e.target.value)}
      />
      <Form.Label htmlFor="dev">Desenvolvedor</Form.Label>
      <Form.Control
        id="dev"
        type="text"
        value={dev}
        onChange={(e) => setdev(e.target.value)}
      />
      <Button id="button">Game Search</Button>
    </Form>
  );
};

export default SearchForm;
