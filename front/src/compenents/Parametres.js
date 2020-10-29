/*import { useState } from "react";*/
import React, {useState} from 'react';


export default ({store}) => {

    function getHour() {
        const h = new Date();
        return ` ${zero(h.getHours())}:${zero(h.getMinutes())}`;
    }

    const [hour, setHour] = useState(getHour());

    function zero(nombre) {
        return nombre < 10 ? '0' + nombre : nombre;
    }


    function updateHeure(){
        setHour(getHour());
    }

    setInterval(updateHeure, 1000);

    if(store.state.boolNavBar) {
        return (
            <div id='param'>
                <i onClick={() => store.merge({boolNavBar: !store.state.boolNavBar})} id='icon' className="fas fa-arrow-left"></i>
                <p id='heure'>{hour}</p>
            </div>
        );
    } else {
        return (
            <div id='param'>
                <i onClick={() => store.merge({boolNavBar: !store.state.boolNavBar})} id='icon' className="fas fa-bars fa-lg"></i>
                <p id='heure'>{hour}</p>
            </div>
        );
    }
};