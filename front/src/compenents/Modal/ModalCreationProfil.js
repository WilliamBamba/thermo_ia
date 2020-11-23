/*import { useState } from "react";*/
import React from 'react';
import c  from '../../helpers/cookies';
import fetch from '../../helpers/fetch';
import config from '../../config';


export default ({store}) => {

    /*<input className="ProfilRadio" type="radio"></input>*/
    if(store.state.modalCreationProfil) {
        console.log(c.getProfile());

        const prenom = React.createRef();
        const city   = React.createRef();
        const url_agenda   = React.createRef();
    

        function updateProfil(profile, store) {
            // TODO: fetch.put update profile dans la db
            fetch.putData(config.server + config.routes.profile.post + profile.id, profile)
                 .then(r => r.json())
                 .then(profile_db => {
                    c.setCookie('profile', JSON.stringify(profile_db), 1);
                    store.merge({'profile': profile_db})
                    window.location.href = '/'
                 })
        }
    
        async function submitProfileModification(e, store) {
            e.preventDefault();

            let profile = c.getProfile();
            profile.name = prenom.current.value;
            profile.city = city.current.value;
            profile.url_agenda = url_agenda.current.value;

            updateProfil(profile, store);
        }
        return (
            <div id='modalProfil'>
                <div className="modal-content">
                    <div className="divJoli">
                        <p className='TitreSection' id="titreModal"> Création Programme </p>
                        <span onClick={() => store.merge({modalCreationProfil: !store.state.modalCreationProfil})} className="close">&times;</span>
                    </div>
                    <form onSubmit={(e) => submitProfileModification(e, store)}>
                        <label htmlFor="fname">Nom</label>
                        <input type="text" ref={prenom} id="fname" name="nom" placeholder={c.getProfile().name}/>

                        <label htmlFor="lname">Lieu où vous habitez</label>
                        <input type="text" ref={city} id="lieu" name="ville" placeholder={c.getProfile().city} required />

                        <label htmlFor="lname">URL de votre Agenda</label>
                        <input type="text" ref={url_agenda} id="agenda" name="agenda" placeholder={c.getProfile().url_agenda}/>
                    
                        <input type="submit" value="Modifier"/>
                    </form>
                </div>
            </div>
        );
    }
    else {
        return(<></>);
    }
};