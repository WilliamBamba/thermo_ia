/*import { useState } from "react";*/
import React from 'react';


export default ({store}) => {

    /*<input className="ProfilRadio" type="radio"></input>*/
    if(store.state.modalCreationProfil) {
        console.log('Modal Creation : ' + store.state.modalCreationProfil );
        return (
            <div id='modalCreation'>
                <div class="modal-content">
                    <p className='TitreSection'> Création d'un Profil  </p>
                    <div className="form">
                        <form action="">
                            <label for="Nom">Nom : </label>
                            <input type="text" id="Nom" name="firstname" placeholder="Nom du Profil..."/>

                            <label for="Ville">Ville : </label>
                            <input type="text" id="Ville" name="lastname" placeholder="Ville où vous habitez..."/>
                        
                            <input type="submit" value="Création"/>
                        </form>
                    </div>
                    <span onClick={() => store.merge({modalCreationProfil: !store.state.modalCreationProfil})} className="close">&times;</span>
                </div>
            </div>
        );
    }
    else {
        return(<></>);
    }
};