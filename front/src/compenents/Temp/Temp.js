/*import { useState } from "react";*/
import TempEvolution from './TempEvolution';
import TempGestion from './TempGestion';
import React from 'react';


export default ({store}) => {

    return (
        <div id='temp'>
            <TempEvolution />
            <TempGestion />
        </div>
    );
};