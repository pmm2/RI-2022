import SearchForm from './Form';
import './App.css';
import Results from './Results';
import { useState } from 'react';
import Header from './Header';
import SimpleForm from './SimpleForm';
import { Container } from 'react-bootstrap';
function App() {
  const [modoResultado, setmodoResultado] = useState(false)
  const [modoAdvanced, setmodoAdvanced] = useState(false)
  const [resultados, setresultados] = useState('')
  return (
    <div className="App">
      {!modoResultado &&<Header setmodoAdvanced={setmodoAdvanced}></Header>}
      {!modoResultado && modoAdvanced && <SearchForm setresultados={setresultados} setmodoResultado={setmodoResultado}></SearchForm>}
      {modoResultado && <Results setresultados={setresultados} resultados={resultados} setmodoResultado={setmodoResultado}></Results>}
      {!modoResultado && !modoAdvanced && <SimpleForm setresultados={setresultados} setmodoResultado={setmodoResultado}></SimpleForm>}
    </div>
  );
}

export default App;
