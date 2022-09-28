import React from "react";

const Results = (props) => {
  return (
    <div>
      <button onClick={()=>props.setmodoResultado(false)}>Realizar outra busca</button>
      {/* //map do objeto recebido do back end com titulo sendo um hyperlink da url */}
      <h1>
        <a href="amazon.com">Amazon</a>
      </h1>
    </div>
  );
};

export default Results;
