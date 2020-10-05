import React, { useState } from 'react';
import './App.css';
import Home from './compenents/Home';
import s, {initialState} from './store';

function App() {
  const [storage, setStorage] = useState(initialState);
  const store = s(storage, setStorage);
  return (
    <div>
      <Home store={store} />
      <p>count global: {store.state.count}</p>
    </div>
  );
};

export default App;
