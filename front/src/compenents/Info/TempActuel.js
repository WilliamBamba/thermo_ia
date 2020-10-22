/*import { useState } from "react";*/
import React from 'react';


export default ({store}) => {

    return (
        <div id='tempActuel'>
            <p class='TitreSection'> Température Intérieure </p>
            <div id='cercle'>
                <svg viewBox="0 0 36 36" class="circle-svg">
                    <path class="around" stroke-dasharray="100, 100" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831"></path>
                    <path class="percent" stroke-dasharray="65, 100" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831"></path>
                    <text x="18" y="14" text-anchor="middle" dy="7" font-size="20"> 25°C</text>
                </svg>
            </div>
        </div>
    );
};