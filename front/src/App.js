import React, { useState, useEffect } from 'react';
import './App.css';
import Home from './compenents/Home';
import s, {initialState} from './store';

let globalState = { frist: true };

function App() {

  const [storage, setStorage] = useState(initialState);
  const store = s(storage, setStorage, globalState);

  useEffect(() => store.start());

  return (
    <>
      <Home store={store} />
    </>
  );
};

export default App;
