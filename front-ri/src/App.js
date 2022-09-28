import Form from './Form';
import './App.css';
import Results from './Results';
import { useState } from 'react';
import Header from './Header';
import SimpleForm from './SimpleForm';
function App() {
  const [modoResultado, setmodoResultado] = useState(false)
  const [modoAdvanced, setmodoAdvanced] = useState(false)
  return (
    <div className="App">
      {!modoResultado &&<Header setmodoAdvanced={setmodoAdvanced}></Header>}
      {!modoResultado && modoAdvanced && <Form setmodoResultado={setmodoResultado}></Form>}
      {modoResultado && <Results setmodoResultado={setmodoResultado}></Results>}
      {!modoResultado && !modoAdvanced && <SimpleForm setmodoResultado={setmodoResultado}></SimpleForm>}
    </div>
  );
}

export default App;
