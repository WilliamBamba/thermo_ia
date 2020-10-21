/*import { useState } from "react";*/

import React from 'react';
import Parametres from './Parametres';
import Info from './Info/Info';
import Temp from './Temp/Temp';



/*export default ({store}) => {

    const [count, setCount] = useState(0);

    return (
        <div>
            <p>count local: {count}</p>
            <button onClick={() => setCount(count+1)} >+ local</button>
            <br /><br />
            <button onClick={() => store.merge({count: store.state.count+1})}>+ global</button>
        </div>
    );
};*/

export default({store}) => {
    
    return (
        <div id='home'>
            <div className='prettyBar' />
            <Parametres />
            <Info />
            <Temp store={store}/>
            <div className='prettyBar' />
        </div>
    );

}