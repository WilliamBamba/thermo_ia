import { /*useState,*/ useRef, useEffect } from "react";
import React from 'react';
import * as d3 from 'd3';
import fetch from '../../helpers/fetch';
import config from '../../config';


export default ({store}) => {

    const svgRef = useRef();

    function graphiqueTemp(svgRef,data){
        var tailleData = data.length < 1000 ? 1000 : data.length; // Si tu passes à l'heure, tu auras surement plus besoin de ça.
        data = data.sort((a,b) => b.id - a.id).slice(0,1000) // Pensez à modifier selon le nombre de données qu'on veut faire apparaître.
        
        var margin = {top: 30, right: 30, bottom: 30, left: 150},
            width = 610 - margin.left - margin.right,
            height = 300 - margin.top - margin.bottom;

        let svgElement = d3.select(svgRef.current)
                .attr("width", width + margin.left + margin.right)
                .attr("height", height + margin.top + margin.bottom)
            .append("g")
                .attr("transform",
                    "translate(" + margin.left + "," + margin.top + ")");


        // Add X axis --> it is a date format
        var x = d3.scaleLinear() // #ScaleTime()
            .domain([tailleData - 1000, tailleData])
            .range([ 0, width ]);
        svgElement.append("g")
            .attr("transform", "translate(0," + height + ")")
            .call(d3.axisBottom(x));

        // Add Y axis
        var y = d3.scaleLinear()
            .domain([0, 60])
            .range([ height, 0 ]);
        svgElement.append("g")
            .call(d3.axisLeft(y));

        svgElement.append("linearGradient")
            .attr("id", "line-gradient")
            .attr("gradientUnits", "userSpaceOnUse")
            .attr("x1", 0)
            .attr("y1", y(0))
            .attr("x2", 0)
            .attr("y2", y(60))
            .selectAll("stop")
              .data([
                {offset: "0%", color: "rgb(42,203,236)"},
                {offset: "59%", color: " rgba(199,203,44,1)"},
                {offset: "100%", color: "rgba(205,47,47,1)"}
              ])
            .enter().append("stop")
              .attr("offset", function(d) { return d.offset; })
              .attr("stop-color", function(d) { return d.color; });
      

        // Add the line
        svgElement.append("path")
            .datum(data)
            .attr("fill", "none")
            .attr("stroke", "url(#line-gradient)")
            .attr("stroke-width", 3)
            .attr("d", d3.line()
            .x(function(d) { console.log('id',d.id);return x(d.id) })
            .y(function(d) { console.log('temperature',d.temperature);return y(d.temperature) })
            )
            }


    useEffect(() => {
        fetch.getData(config.server + config.routes.sensor.get)
        .then(r => r.json())
        .then(data => {
            graphiqueTemp(svgRef,data)
        })
      }, [])


    return (
        <div id='tempEvolution'>
            <p className='TitreSection'> Evolution Température Intérieure </p>
            <svg ref={svgRef}/>
        </div>
    );
};