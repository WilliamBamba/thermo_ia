/*import { useState } from "react";*/
import React from 'react';


export default ({store}) => {

    /*<input className="ProfilRadio" type="radio"></input>*/
    if(store.state.modalProfil) {
        console.log('Modal Profil : ' + store.state.modalProfil );
        return (
            <div id='modalProfil'>
                <div class="modal-content">
                    <span onClick={() => store.merge({modalProfil: !store.state.modalProfil})} className="close">&times;</span>
                    <p className='TitreSection'> Petit Poney  </p>
                </div>
            </div>
        );
    }
    else {
        return(<></>);
    }
};