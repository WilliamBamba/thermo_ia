import React, { useState } from 'react';
import './App.css';
import Home from './compenents/Home';
import s, {initialState} from './store';

function App() {
  const [storage, setStorage] = useState(initialState);
  const store = s(storage, setStorage);
  /* <p>count global: {store.state.count}</p> */
  
  return (
    <Home store={store} />
  );
};

export default App;
