import React from "react";
import { useState } from "react";
import axios from "axios";
import { Button, Form } from "react-bootstrap";
const SimpleForm = (props) => {
  const [simple, setSimple] = useState("");
  const submitHandler = (e) => {
    e.preventDefault();
    //localhost ta 7777 pois tenho processos rodando na 8000
    axios.post("http://localhost:7777", { simple: simple }).then((resp) => {
      props.setmodoResultado(true);
      props.setresultados(JSON.parse(resp.data));
    });
    //POST
    //chama funcao externa para esconder submithandler e
    //Gerar entradas apartir da payload
    props.setmodoResultado(true);
  };
  return (
    <Form className="Forms" action="" onSubmit={submitHandler}>
      <h2>Gaming Google</h2>
      <Form.Control
        id="simple"
        type="text"
        value={simple}
        onChange={(e) => setSimple(e.target.value)}
      />
      <Button id="button">Game Search</Button>
    </Form>
  );
};

export default SimpleForm;
