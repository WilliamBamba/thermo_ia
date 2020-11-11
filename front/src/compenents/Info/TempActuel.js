import { useState } from "react";
import React from 'react';
import fetch from '../../helpers/fetch';
import config from '../../config';

import GradiantCircle from './GradiantCircle';


async function fetchCurrentTemperature(store) {

    let data = await fetch.getData(config.server + config.routes.sensor.get)
        .then(res => res.json())

    store.merge({ temp: data.temp });
}



export default ({ store }) => {

    store.once(() => fetchCurrentTemperature(store));

    return (
        <div id='tempActuel'>
            <p className='TitreSection'> Température Intérieure </p>
            <div id="cercle-container" >
                <div id='cercle'>
                    <GradiantCircle store={store} />
                </div>
            </div>
        </div>
    );
};