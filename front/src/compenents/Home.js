import { useState } from "react";
import React from 'react';


export default ({}) => {

    const [count, setCount] = useState(0);

    return (
        <div>
            <p>lorem ipsum</p>
            <p>{count}</p>
            <button onClick={() => setCount(count+1)}>+</button>
        </div>
    );
};