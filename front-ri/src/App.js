import Form from './Form';
import './App.css';
import Results from './Results';
import { useState } from 'react';
function App() {
  const [modoResultado, setmodoResultado] = useState(false)
  return (
    <div className="App">
      {!modoResultado && <Form setmodoResultado={setmodoResultado}></Form>}
      {modoResultado &&<Results setmodoResultado={setmodoResultado}></Results>}
    </div>
  );
}

export default App;
