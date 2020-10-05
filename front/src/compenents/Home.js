import { useState } from "react";
import React from 'react';


export default ({store}) => {

    const [count, setCount] = useState(0);

    return (
        <div>
            <p>count local: {count}</p>
            <button onClick={() => setCount(count+1)} >+ local</button>
            <br /><br />
            <button onClick={() => store.merge({count: store.state.count+1})}>+ global</button>
        </div>
    );
};