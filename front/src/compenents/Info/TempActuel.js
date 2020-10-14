/*import { useState } from "react";*/
import React from 'react';


export default ({store}) => {

    /* 
    <path class="around" stroke-dasharray="100, 100" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831"></path>
                    <path class="percent" stroke-dasharray="70, 100" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831"></path>

                    <defs>
                        <linearGradient id="gradient" x1="0%" y1="0%" x2="100%" y2="0%">
                            <stop offset="0%" id='blue' />
                            <stop offset="25%" id='jaune' />
                            <stop offset="90%" id='red' />
                        </linearGradient>
                    </defs>
                    <path class="around" stroke-dasharray="100, 100" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831"></path>
    */

    return (
        <div id='tempActuel'>
            <p class='TitreSection'> Température Intérieure </p>
            <div id='cercle'>
                <svg width='100%' height='100%' class="circle-svg">
                    <linearGradient id="linearColors1" x1="0" y1="0" x2="1" y2="1">
                        <stop offset="0%" stop-color="#ffffff"></stop>
                        <stop offset="100%" stop-color="#2cbacb"></stop>
                    </linearGradient>
                    <linearGradient id="linearColors2" x1="0.5" y1="0" x2="0.5" y2="1">
                        <stop offset="0%" stop-color="#2cbacb"></stop>
                        <stop offset="100%" stop-color="#2cbacb"></stop>
                    </linearGradient>
                    <linearGradient id="linearColors3" x1="1" y1="0" x2="0" y2="1">
                        <stop offset="0%" stop-color="#2cbacb"></stop>
                        <stop offset="100%" stop-color="#d8eb15"></stop>
                    </linearGradient>
                    <linearGradient id="linearColors4" x1="1" y1="1" x2="0" y2="0">
                        <stop offset="0%" stop-color="#d8eb15"></stop>
                        <stop offset="100%" stop-color="#eb9615"></stop>
                    </linearGradient>
                    <linearGradient id="linearColors5" x1="0.5" y1="1" x2="0.5" y2="0">
                        <stop offset="0%" stop-color="#eb9615"></stop>
                        <stop offset="100%" stop-color="#eb5915"></stop>
                    </linearGradient>
                    <linearGradient id="linearColors6" x1="0" y1="1" x2="1" y2="0">
                        <stop offset="0%" stop-color="#eb5915"></stop>
                        <stop offset="100%" stop-color="#ff0000"></stop>
                    </linearGradient>
                    <path d="M150 10 a120 120 0 0 1 103.9230 60"
                            fill="none" stroke="url(#linearColors1)" stroke-width="10" />
                    <path d="M253.9230 70 a120 120 0 0 1 0 120"
                            fill="none" stroke="url(#linearColors2)" stroke-width="10" />
                    <path d="M253.9230 190 a120 120 0 0 1 -103.9230 60"
                            fill="none" stroke="url(#linearColors3)" stroke-width="10" />
                    <path d="M150 250 a120 120 0 0 1 -103.9230 -60"
                            fill="none" stroke="url(#linearColors4)" stroke-width="10" />
                    <path d="M46.077 190 a120 120 0 0 1 0 -120"
                            fill="none" stroke="url(#linearColors5)" stroke-width="10" />
                    <path d="M46.077 70 a120 120 0 0 1 103.9230 -60"
                            fill="none" stroke="url(#linearColors6)" stroke-width="10" />
                    <text x="18" y="14" text-anchor="middle" dy="7" font-size="20"> 25°C</text>
                </svg>
            </div>
        </div>
    );
};