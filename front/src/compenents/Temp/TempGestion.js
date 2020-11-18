import { useState } from "react";
import React from 'react';
import fetch from '../../helpers/fetch';


export default ({store}) => {

    function updateTemp(store, by) {
        let profile = store.state.profile;
        profile.wtemp += by;
        // TODO: fetch.put update profile dans la db
        store.merge({'profile': profile});
        console.log(profile);
    }

    function getWtemp(store) {
        let wtemp = 23;
        try {
            wtemp = store.state.profile.wtemp;
            if (!wtemp) wtemp = 0;
        } catch (error) {
            console.log('err getWtemp');
        }
        return wtemp;
    }


    return (
        <div id='tempGestion'>
            <p className='TitreSection'> Température Souhaitée </p>
            <div className='containerGestion'>
                <i onClick={() => updateTemp(store, -1)} className="fas fa-minus fa-8x"></i>
                <p id='compteur'>{getWtemp(store)} °C</p>
                <i onClick={() => updateTemp(store, 1)} className="fas fa-plus fa-8x"></i>
            </div>
        </div>
    );
};