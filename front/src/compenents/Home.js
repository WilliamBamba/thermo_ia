/*import { useState } from "react";*/

import React from 'react';
import Navbar from './Navbar';
import Parametres from './Parametres';
import Info from './Info/Info';
import Temp from './Temp/Temp';
import ModalCreationProfil from './Modal/ModalCreationProfil';
import ModalProfil from './Modal/ModalProfil';
import ModalUser from './Modal/ModalUser';

export default({store}) => {
    return (
        <div id="maisonRelou">
        <div className='prettyBar' />
        <div id="maison">
            <Navbar store={store} />
            <div id='home'>
                <Parametres store={store}/>
                <Info store={store}/>
                <Temp store={store}/>
                <ModalCreationProfil store={store} />
                <ModalProfil store={store} />
                <ModalUser store={store} />
            </div>
        </div>
        <div className='prettyBar' />
    </div>
    );
       
}