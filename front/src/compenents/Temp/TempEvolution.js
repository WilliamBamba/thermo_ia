import { /*useState,*/ useRef, useEffect } from "react";
import React from 'react';
import * as d3 from 'd3';
import fetch from '../../helpers/fetch';
import config from '../../config';


export default ({store}) => {

    const svgRef = useRef();

    function graphiqueTemp(svgRef,data){
        data = data.sort((a,b) => b.id - a.id).slice(0,100)
        
        var margin = {top: 30, right: 30, bottom: 30, left: 50},
            width = 460 - margin.left - margin.right,
            height = 400 - margin.top - margin.bottom;

        let svgElement = d3.select(svgRef.current)
                .attr("width", width + margin.left + margin.right)
                .attr("height", height + margin.top + margin.bottom)
            .append("g")
                .attr("transform",
                    "translate(" + margin.left + "," + margin.top + ")");

        var x = d3.scaleLinear()
                .domain([0,100])
                .range([0,width])

        svgElement.append("g")
                .attr("transform", "translate(0," + height + ")")
                .call(d3.axisBottom(x));

        var y = d3.scaleLinear()
        .range([height, 0])
        .domain([0, 60]);
        
        svgElement.append("g")
          .call(d3.axisLeft(y));
        
          // Plot the area
        svgElement.append('g')
            .selectAll("dot")
            .data(data)
            .enter()
            .append("circle")
                .attr("cx", function (d) { return x(d.id); } )
                .attr("cy", function (d) { return y(d.temperature); } )
                .attr("r", 1.5)
                .style("fill", "#69b3a2")
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