/*import { useState } from "react";*/
import React from 'react';


export default ({store}) => {

    return (
        <div id='navbar'>
            <p> Paramètres </p>
            <ul className="menu">
                <li><a href="#"> Page d'accueil</a></li>
                <li><a href="#"> Agenda </a></li>
                <li><a href="#"> Keur Keur </a></li>
                <li><a href="#"> Licorne Volante </a></li>
            </ul>
        </div>
    );
};