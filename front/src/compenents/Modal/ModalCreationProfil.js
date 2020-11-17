/*import { useState } from "react";*/
import React from 'react';


export default ({store}) => {

    /*<input className="ProfilRadio" type="radio"></input>*/
    if(store.state.modalCreationProfil) {
        console.log('Modal Creation : ' + store.state.modalCreationProfil );
        return (
            <div id='modalProfil'>
                <div className="modal-content">
                    <div className="divJoli">
                        <p className='TitreSection' id="titreModal"> Création Programme </p>
                        <span onClick={() => store.merge({modalCreationProfil: !store.state.modalCreationProfil})} className="close">&times;</span>
                    </div>
                    <form>
                        <label for="fname">Nom du Programme</label>
                        <input type="text" id="fname" name="nom" />

                        <label for="lname">URL de votre Agenda</label>
                        <input type="text" id="agenda" name="agenda"/>
                    
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