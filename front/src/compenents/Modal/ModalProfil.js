/*import { useState } from "react";*/
import React from 'react';


export default ({store}) => {

    /*<input className="ProfilRadio" type="radio"></input>*/
    if(store.state.modalProfil) {
        console.log('Modal Profil : ' + store.state.modalProfil );
        return (
            <div id='modalProfil'>
                <div className="modal-content">
                    <div className="divJoli">
                        <p className='TitreSection' id="titreModal"> Programme  </p>
                        <span onClick={() => store.merge({modalProfil: !store.state.modalProfil})} className="close">&times;</span>
                    </div>
                </div>
            </div>
        );
    }
    else {
        return(<></>);
    }
};