import { useState } from "react";
import React from 'react';


export default ({store}) => {

    return (
        <div id='tempGestion'>
            <p className='TitreSection'> Température Souhaitée </p>
            <div className='containerGestion'>
                <i onClick={() => store.merge({count: store.state.count-1})} className="fas fa-minus fa-8x"></i>
                <p id='compteur'>{store.state.count }</p>
                <i onClick={() => store.merge({count: store.state.count+1})} className="fas fa-plus fa-8x"></i>
            </div>
        </div>
    );
};