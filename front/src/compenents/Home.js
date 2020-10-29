/*import { useState } from "react";*/

import React from 'react';
import Navbar from './Navbar';
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
    if(store.state.boolNavBar) {
        return (
            <div id="maisonRelou">
            <div className='prettyBar' />
            <div id="maison">
                <Navbar />
                <div id='home'>
                    <Parametres store={store}/>
                    <Info />
                    <Temp store={store}/>
                </div>
            </div>
            <div className='prettyBar' />
        </div>
        );
    } else {
        return (
            <div id='home'>
                <div className='prettyBar' />
                <Parametres store={store}/>
                <Info />
                <Temp store={store}/>
                <div className='prettyBar' />
            </div>
              
        );
    }
}