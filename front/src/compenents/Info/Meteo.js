/*import { useState } from "react";*/
import React, { useState, useEffect } from 'react';

import config from '../../config';
import fetch from '../../helpers/fetch';
import offline_weather from '../../data/weather';
import cookie from '../../helpers/cookies';



function fetchMeteo(setWeather, city) {
    
    try {
        fetch.getData(config.server + config.routes.weather.get + city)
             .then(r => r.json())
             .then(w => setWeather(w));
    } catch (error) {
        alert('database connection error');
        setWeather(offline_weather);
    }
}


export default ({store}) => {


    let [weather, setWeather] = useState(offline_weather);
    let defaultCity = 'lyon';
    let profile = cookie.getProfile();
    if (profile) defaultCity = profile.city;
    let [city] = useState(defaultCity);

    useEffect(() => fetchMeteo(setWeather, city), [city]);


    // on prend un jour c'est le premier jour
    const forcast_day = weather.forecast.forecastday[0];
    const forcast_by_hours = forcast_day.hour.filter((v, i, arr) => i % 3 === 0 || i === arr.length - 1);
    let len = forcast_by_hours.length + 1;

    // regardes le format

    function getName(store) {
        let name = 'No Name'
        try {
            name = store.state.profile.name
        } catch (error) {
            name = 'Name Err'
        }
        return name;
    }

    return (
        <div id='meteo'>
            <p className='TitreSection'>Bonjour {getName(store)}</p>
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