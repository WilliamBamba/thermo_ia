import { useState } from "react";
import React from 'react';
import c  from '../../helpers/cookies';
import fetch from '../../helpers/fetch';
import config from '../../config';


export default ({store}) => {

    function updateTemp(store, by) {
        let profile = store.state.profile;
        profile.wtemp += by;
        // TODO: fetch.put update profile dans la db
        fetch.putData(config.server + config.routes.profile.post + profile.id, profile)
             .then(r => r.json())
             .then(profile_db => {
                c.setCookie('profile', JSON.stringify(profile_db), 1);
                store.merge({'profile': profile_db})
             })
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