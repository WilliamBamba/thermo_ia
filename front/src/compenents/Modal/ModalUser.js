/*import { useState } from "react";*/
import c  from '../../helpers/cookies';
import React, { useState } from 'react';
import fetch from '../../helpers/fetch';
import config from '../../config';

export default ({store}) => {

    /*<input className="ProfilRadio" type="radio"></input>*/
    // const [nom, setNom] = useState();
    const prenom = React.createRef();
    const city   = React.createRef();
    const temp   = React.createRef();

    console.log('Test ' + c.getCookie('User'));

    async function submitProfileCreation(e, store) {
        e.preventDefault();
        let profile = {
                        'name': prenom.current.value,
                        'city': city.current.value,
                        'wtemp': temp.current.value
                    };
        fetch.postData(config.server + config.routes.profile.post, profile)
             .then(r => r.json())
             .then(profile_db => {
                c.setCookie('profile', JSON.stringify(profile_db), 1);
                console.log(profile_db);
                store.merge({'profile': profile_db});
             });
    }

    // c.setCookie('profile', null, 0);

    if((!c.getCookie('profile'))) {
        return (
            <div id='modalProfil'>
                <div className="modal-content">
                    <div className="divJoli">
                        <p className='TitreSection' id="titreModal"> Création de l'utilisateur  </p>
                    </div>
                    <form onSubmit={(e) => submitProfileCreation(e, store)}>

                        <label htmlFor="lname">Prénom</label>
                        <input type="text" ref={prenom} id="lname" name="prenom" required/>

                        <label htmlFor="lname">Temperature</label>
                        <input type="number" ref={temp} id="lname" name="temp" required/>

                        <label htmlFor="lname">Lieu où vous habitez</label>
                        <input type="text" ref={city} id="lieu" name="ville" placeholder="lyon.." required />

                        <input type="submit" value="Demarrer"/>
                    </form>
                </div>
            </div>
        );
    }
    else {
        store.once(() => {
            let profile = c.getProfile();
            fetch.getData(config.server + config.routes.profile.get +  profile.id)
                 .then(r => r.json())
                 .then(profile_db => {
                    c.setCookie('profile', JSON.stringify(profile_db), 1);
                    store.merge({'profile': c.getProfile()});
                 })
            // store.merge({'temp': c.getProfile().ctemp});
            console.log(c.getProfile());
        });
        return(<></>);
    }
};