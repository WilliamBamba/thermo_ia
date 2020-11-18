/*import { useState } from "react";*/
import Meteo from './Meteo';
import TempActuel from './TempActuel';
import React from 'react';


export default ({store}) => {

    return (
        <div id='info'>
            <Meteo store={store} />
            <TempActuel store={store}/>
        </div>
    );
};