import React from "react";

const Results = (props) => {
  console.log(props.resultados);
  console.log(typeof props.resultados);
  const falsear = ()=>{
    props.setmodoResultado(false)
    props.setresultados('')
  }
  return (
    <div>
      <button onClick={falsear}>
        Search something else
      </button>
      {props.resultados == '' && <h2>Loading....</h2>}
      {props.resultados != '' && <h3>You would also like: Sonic , Zelda</h3>}
      {props.resultados != '' &&
        props.resultados.map((url) => (
          <h2>
            <a href={url}>{url}</a>
          </h2>
        ))}
    </div>
  );
};

export default Results;
