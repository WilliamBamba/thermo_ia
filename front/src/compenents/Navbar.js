/*import { useState } from "react";*/
import React from 'react';


export default ({store}) => {

    /*<input className="ProfilRadio" type="radio"></input>*/
    if(store.state.boolNavBar) {
        return (
            <div id='navbar'>
                <p> Paramètres </p>
                <ul className="menu">
                    <li>
                        <button onClick={() => store.merge({modalCreationProfil: !store.state.modalCreationProfil})} className="buttonProfil"> Modification du Profil </button>
                    </li>
                </ul>
            </div>
        );
    }
    else {
        return(<></>);
    }
};