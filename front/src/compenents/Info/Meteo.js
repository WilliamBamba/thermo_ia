/*import { useState } from "react";*/
import React from 'react';

import weather from '../../data/weather';
// ça juste un échatillon le serveur il repond ce type de donné

export default ({store}) => {

    // TODO: il faut convertir en AM PM à 0-24h

    /* <p>sunrise: {forcast_day.astro.sunrise} sunset: {forcast_day.astro.sunset}</p>*/

    console.log(weather);
    // on prend un jour c'est le premier jour
    const name = "Machin";
    const forcast_day = weather.forecast.forecastday[0];
    const forcast_by_hours = forcast_day.hour;
    let len = forcast_by_hours.length + 1;

    // regardes le format

    return (
        <div id='meteo'>
            <p className='TitreSection'>Bonjour {name}</p>
            <p id="phrase"> Voici la température d'aujourd'hui à {weather.location.name}:</p>
            <div className='container'>
            {forcast_by_hours.map(hour => {
                    len = len - 1;
                    return (
                        <div className='card' style={{zIndex:len}} key={len}>
                            <h3 className="title">{hour.temp_c}°C</h3>
                            <div className="bar">
                                <div className="emptybar"></div>
                                <div className="filledbar"></div>
                            </div>
                            <div className='imgInfo'>
                                <img className='img' src={hour.condition.icon} alt="condition" />
                                <div className="card-content">
                                    <p>{hour.time.split(' ')[1]}h</p>
                                </div>
                            </div>
                        </div>
                    ) 
                })}
            </div>
        </div>
    );
};