/*import { useState } from "react";*/
import c  from '../../helpers/cookies';
import { get } from 'js-cookie';
import React from 'react';


export default ({store}) => {

    /*<input className="ProfilRadio" type="radio"></input>*/
    console.log('Test ' + c.getCookie('User'));
    if(!(c.getCookie('User'))) {
        return (
            <div id='modalProfil'>
                <div className="modal-content">
                    <div className="divJoli">
                        <p className='TitreSection' id="titreModal"> Création de l'utilisateur  </p>
                    </div>
                    <form>
                        <label for="fname">Nom</label>
                        <input type="text" id="fname" name="nom" />

                        <label for="lname">Prénom</label>
                        <input type="text" id="lname" name="prenom"/>

                        <label for="lname">Lieu où vous habitez</label>
                        <input type="text" id="lieu" name="ville"/>
                    
                        <input type="submit" value="Submit"/>
                    </form>
                </div>
            </div>
        );
    }
    else {
        return(<></>);
    }
};