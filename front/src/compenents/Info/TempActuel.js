import { useState } from "react";
import React from 'react';
import fetch from '../../helpers/fetch';
import config from '../../config';

import GradiantCircle from './GradiantCircle';



async function fetchCurrentTemperature(setTemp) {

    let data = await fetch.getData(config.server + config.routes.sensor.get + 'most_recent')
        .then(res => res.json());
        console.log('update temp');
        if (data) setTemp(data.temperature);
}

function refreshCurrentTemp(setTemp) {
    setInterval(() => fetchCurrentTemperature(setTemp), 1000 * 30);
}



export default ({ store }) => {

    const [temp, setTemp] = useState(25);
    store.once(() => fetchCurrentTemperature(setTemp));
    store.once(() => refreshCurrentTemp(setTemp));


    return (
        <div id='tempActuel'>
            <p className='TitreSection'> Température Intérieure </p>
            <div id="cercle-container" >
                <div id='cercle'>
                    <GradiantCircle temp={temp} />
                </div>
            </div>
        </div>
    );
};