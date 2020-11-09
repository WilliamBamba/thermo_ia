import { useState } from "react";
import React from 'react';


export default ({store}) => {

    function jeFaisUnTest(val) {
        if(val <= 10) {
            console.log('TEMP EN DESSOUS DE 8');
            return(<path d="M253.9230 70 a120 120 0 0 1 0 120"
                fill="none" stroke="url(#linearColors2)" stroke-width="10" />)
        }
        if( val > 10 && val <= 20) {
            console.log('TEMP EN DESSUS DE 8 ET EN DESSOUS DE 16');
            return(
                <>
                    <path d="M253.9230 70 a120 120 0 0 1 0 120"
                        fill="none" stroke="url(#linearColors2)" stroke-width="10" />
                    <path d="M253.9230 190 a120 120 0 0 1 -103.9230 60"
                        fill="none" stroke="url(#linearColors3)" stroke-width="10" />
                </>)
        }
        if( val > 20 && val <= 30) {
            console.log('TEMP EN DESSUS DE 16 ET EN DESSOUS DE 24');
            return(
                <>
                    <path d="M253.9230 70 a120 120 0 0 1 0 120"
                        fill="none" stroke="url(#linearColors2)" stroke-width="10" />
                    <path d="M253.9230 190 a120 120 0 0 1 -103.9230 60"
                        fill="none" stroke="url(#linearColors3)" stroke-width="10" />
                    <path d="M150 250 a120 120 0 0 1 -103.9230 -60"
                        fill="none" stroke="url(#linearColors4)" stroke-width="10" />
                </>)
        }
        if( val > 30 && val <= 40) {
            console.log('TEMP EN DESSUS DE 24 ET EN DESSOUS DE 32');
            return(
                <>
                    <path d="M253.9230 70 a120 120 0 0 1 0 120"
                        fill="none" stroke="url(#linearColors2)" stroke-width="10" />
                    <path d="M253.9230 190 a120 120 0 0 1 -103.9230 60"
                        fill="none" stroke="url(#linearColors3)" stroke-width="10" />
                    <path d="M150 250 a120 120 0 0 1 -103.9230 -60"
                        fill="none" stroke="url(#linearColors4)" stroke-width="10" />
                    <path d="M46.077 190 a120 120 0 0 1 0 -120"
                        fill="none" stroke="url(#linearColors5)" stroke-width="10" />
                </>)
        }
        if( val > 40) {
            console.log('TEMP EN DESSUS DE 32');
            return(
                <>
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
                </>)
        }
    }


    return (
        <div id='tempActuel'>
            <p  className='TitreSection'> Température Intérieure </p>
            <div id="cercle-container" >
                <div id='cercle'>
                    <svg className="circle-svg">
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
                                fill="none" stroke="#2c3239" stroke-width="10" />
                        <path d="M253.9230 70 a120 120 0 0 1 0 120"
                                fill="none" stroke="#2c3239" stroke-width="10" />
                        <path d="M253.9230 190 a120 120 0 0 1 -103.9230 60"
                                fill="none" stroke="#2c3239" stroke-width="10" />
                        <path d="M150 250 a120 120 0 0 1 -103.9230 -60"
                                fill="none" stroke="#2c3239" stroke-width="10" />
                        <path d="M46.077 190 a120 120 0 0 1 0 -120"
                                fill="none" stroke="#2c3239" stroke-width="10" />
                        <path d="M46.077 70 a120 120 0 0 1 103.9230 -60"
                                fill="none" stroke="#2c3239" stroke-width="10" />
                        
                    
                        <path d="M150 10 a120 120 0 0 1 103.9230 60"
                            fill="none" stroke="url(#linearColors1)" stroke-width="10" />
                        {jeFaisUnTest(store.state.temp)}
                        
                        
                        
                        
                        
                        
                        
                        
                        <text x="50%" y="50%" dominant-baseline="center" text-anchor="middle" font-size="45" stroke="white" strokeWidth="4" >{store.state.temp}°C</text>
                    </svg>
                </div>
            </div>
        </div>
    );
};