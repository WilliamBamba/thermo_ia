/*import { useState } from "react";*/
import React from 'react';

import weather from '../../data/weather';
// ça juste un échatillon le serveur il repond ce type de donné

export default ({store}) => {

    // TODO: il faut convertir en AM PM à 0-24h

    console.log(weather);
    // on prend un jour c'est le premier jour
    const forcast_day = weather.forecast.forecastday[0];
    const forcast_by_hours = forcast_day.hour;

    // regardes le format

    return (
        <div id='meteo'>
            <p className='TitreSection'>Météo Aujourd'hui</p>
            <p>location: {weather.location.name}</p>
            <p>sunrise: {forcast_day.astro.sunrise} sunset: {forcast_day.astro.sunset}</p>
            <p>{forcast_by_hours.map(hour => {
                return (<p>
                            {hour.temp_c}C à {hour.time.split(' ')[1]}h
                            <img src={hour.condition.icon} alt="condition" />
                    </p>) 
            })}</p>
        </div>
    );
};