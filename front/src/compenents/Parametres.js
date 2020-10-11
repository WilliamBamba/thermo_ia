/*import { useState } from "react";*/
import React from 'react';


export default ({store}) => {
    function zero(nombre) {
        return nombre < 10 ? '0' + nombre : nombre;
    }
    function heure(){
        const h = new Date();

        document.getElementById('heure').innerHTML = ' ' + zero(h.getHours()) + ':' + zero(h.getMinutes());
    }
    window.onload = function() { setInterval(heure(), 100); }

    return (
        <div id='param'>
            <i id='icon' className="fas fa-bars fa-lg"></i>
            <p id='heure'></p>
        </div>
    );
};