import { useState } from "react";
import React from 'react';
import fetch from '../../helpers/fetch';
import config from '../../config';

import GradiantCircle from './GradiantCircle';

let frist = true;


// (ch, cl)
// action => [(0, 0), (0, 1), (1, 0)]

// tmpV = 23
// tmpCI = 18
// tmpD = 25

function recomponse(t_moins1, t) {
    let diif = t_moins1.tmpV - 'tmpCI t-1';
    let diif2 = t.tmpV - 'tmpCI t';

    if (diif < diif2) return 'OK';

}


// tmpV > tmpCI 
// tmpV < tmpCI 
// tmpV == tmpCI 

// tmpV < tmpD 
// tmpV > tmpD 
// tmpV == tmpD


// CIP DP
// CIN DN
// CIP DN
// CIN DP



// 5, 10 => 0, 0
// 5, 10 => 0, 1
// 5, 10 => 1, 0

// 23, 18, 25 => 

// -5, 2 => parmis(action)


function fetchCurrentTemperature(store) {

    if (!frist) return;
    frist = false;

    (async () => {
        let data = await fetch.getData(config.server + config.routes.sensor.get)
            .then(res => res.json())

        store.merge({ temp: data.temp });
    })();
}



export default ({ store }) => {

    fetchCurrentTemperature(store);

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