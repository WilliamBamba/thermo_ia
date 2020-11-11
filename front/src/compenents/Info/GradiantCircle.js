import { useState } from "react";
import React from 'react';


function jeFaisUnTest(val) {

    let chunks = [];

    if(val >= 10) {
        console.log('TEMP EN DESSOUS DE 8');
        chunks.push(<path d="M253.9230 70 a120 120 0 0 1 0 120" fill="none" stroke="url(#linearColors2)" strokeWidth="10" key={chunks.length} />)
    }


    if( val >= 20) {
        console.log('TEMP EN DESSUS DE 8 ET EN DESSOUS DE 16');
        chunks.push(<path d="M253.9230 190 a120 120 0 0 1 -103.9230 60" fill="none" stroke="url(#linearColors3)" strokeWidth="10" key={chunks.length} />)
    }

    if(val >= 30) {
        console.log('TEMP EN DESSUS DE 16 ET EN DESSOUS DE 24');
        chunks.push(<path d="M150 250 a120 120 0 0 1 -103.9230 -60" fill="none" stroke="url(#linearColors4)" strokeWidth="10" key={chunks.length} />)
    }

    if(val >= 40) {
        console.log('TEMP EN DESSUS DE 24 ET EN DESSOUS DE 32');
        chunks.push(<path d="M46.077 190 a120 120 0 0 1 0 -120" fill="none" stroke="url(#linearColors5)" strokeWidth="10" key={chunks.length} />)
    }

    if( val >= 50) {
        console.log('TEMP EN DESSUS DE 32');
        chunks.push(<path d="M46.077 70 a120 120 0 0 1 103.9230 -60" fill="none" stroke="url(#linearColors6)" strokeWidth="10" key={chunks.length} />)
    }

    return chunks;
}


export default ({ store }) => {

    return (
        <svg className="circle-svg">
            <linearGradient id="linearColors1" x1="0" y1="0" x2="1" y2="1">
                <stop offset="0%" stopColor="#ffffff"></stop>
                <stop offset="100%" stopColor="#2cbacb"></stop>
            </linearGradient>
            <linearGradient id="linearColors2" x1="0.5" y1="0" x2="0.5" y2="1">
                <stop offset="0%" stopColor="#2cbacb"></stop>
                <stop offset="100%" stopColor="#2cbacb"></stop>
            </linearGradient>
            <linearGradient id="linearColors3" x1="1" y1="0" x2="0" y2="1">
                <stop offset="0%" stopColor="#2cbacb"></stop>
                <stop offset="100%" stopColor="#d8eb15"></stop>
            </linearGradient>
            <linearGradient id="linearColors4" x1="1" y1="1" x2="0" y2="0">
                <stop offset="0%" stopColor="#d8eb15"></stop>
                <stop offset="100%" stopColor="#eb9615"></stop>
            </linearGradient>
            <linearGradient id="linearColors5" x1="0.5" y1="1" x2="0.5" y2="0">
                <stop offset="0%" stopColor="#eb9615"></stop>
                <stop offset="100%" stopColor="#eb5915"></stop>
            </linearGradient>
            <linearGradient id="linearColors6" x1="0" y1="1" x2="1" y2="0">
                <stop offset="0%" stopColor="#eb5915"></stop>
                <stop offset="100%" stopColor="#ff0000"></stop>
            </linearGradient>

            <path d="M150 10 a120 120 0 0 1 103.9230 60"
                fill="none" stroke="#2c3239" strokeWidth="10" />
            <path d="M253.9230 70 a120 120 0 0 1 0 120"
                fill="none" stroke="#2c3239" strokeWidth="10" />
            <path d="M253.9230 190 a120 120 0 0 1 -103.9230 60"
                fill="none" stroke="#2c3239" strokeWidth="10" />
            <path d="M150 250 a120 120 0 0 1 -103.9230 -60"
                fill="none" stroke="#2c3239" strokeWidth="10" />
            <path d="M46.077 190 a120 120 0 0 1 0 -120"
                fill="none" stroke="#2c3239" strokeWidth="10" />
            <path d="M46.077 70 a120 120 0 0 1 103.9230 -60"
                fill="none" stroke="#2c3239" strokeWidth="10" />

            <path d="M150 10 a120 120 0 0 1 103.9230 60" fill="none" stroke="url(#linearColors1)" strokeWidth="10" />


            {jeFaisUnTest(store.state.temp)}
            <text x="50%" y="50%" dominantBaseline="center" textAnchor="middle" fontSize="45" stroke="white" strokeWidth="4" >{store.state.temp}°C</text>
        </svg>

    );

};