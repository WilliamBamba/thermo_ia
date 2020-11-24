import { /*useState,*/ useRef, useEffect } from "react";
import React from 'react';
import * as d3 from 'd3';
import fetch from '../../helpers/fetch';
import config from '../../config';


export default ({store}) => {

    const svgRef = useRef();

    function graphiqueTemp(svgRef,data){
        data = data.sort((a,b) => b.id - a.id).slice(0,100).reverse()

        var margin = {top: 20, right: 20, bottom: 30, left: 50},
        width = 460 - margin.left - margin.right,
        height = 400 - margin.top - margin.bottom;

        // set the ranges
        var x = d3.scaleTime().range([0, width]);
        var y = d3.scaleLinear().range([height, 0]);

        // define the line
        var valueline = d3.line()
           .x(function(d) { return x(d.id); })
           .y(function(d) { return y(d.temperature); });

        // append the svg obgect to the body of the page
        // appends a 'group' element to 'svg'
        // moves the 'group' element to the top left margin
        var svgElement = d3.select(svgRef.current)
           .attr("width", width + margin.left + margin.right)
           .attr("height", height + margin.top + margin.bottom)
           .append("g").attr("transform",
              "translate(" + margin.left + "," + margin.top + ")");

        // Get the data
        data.forEach(function(d) {
            d.id = d.id;
            d.temperature = d.temperature;
        });

        // Scale the range of the data
        x.domain(d3.extent(data, function(d) { return d.id; }));
        y.domain([0, d3.max(data, function(d) { return d.temperature; })]);

        // Add the valueline path.
        svgElement.append("path")
            .data([data])
            .attr("class", "line")
            .attr("d", valueline);

        // Add the X Axis
        svgElement.append("g")
            .attr("transform", "translate(0," + height + ")")
            .call(d3.axisBottom(x));

        // Add the Y Axis
        svgElement.append("g")
            .call(d3.axisLeft(y));
        
        // var margin = {top: 30, right: 30, bottom: 30, left: 50},
        //     width = 460 - margin.left - margin.right,
        //     height = 400 - margin.top - margin.bottom;

        // let svgElement = d3.select(svgRef.current)
        //         .attr("width", width + margin.left + margin.right)
        //         .attr("height", height + margin.top + margin.bottom)
        //     .append("g")
        //         .attr("transform",
        //             "translate(" + margin.left + "," + margin.top + ")");

        // var x = d3.scaleLinear()
        //         .domain([0,100])
        //         .range([0,width])

        // svgElement.append("g")
        //         .attr("transform", "translate(0," + height + ")")
        //         .call(d3.axisBottom(x));

        // var y = d3.scaleLinear()
        // .range([height, 0])
        // .domain([0, 60]);
        
        // svgElement.append("g")
        //   .call(d3.axisLeft(y));
        
        // // Add the line
        // svgElement.append("path")
        //   .datum(data)
        //   .attr("fill", "none")
        //   .attr("stroke", "#69b3a2")
        //   .attr("stroke-width", 1.5)
        //   .attr("d", d3.line()
        //     .x(function(data) { return x(data.id) })
        //     .y(function(data) { return y(data.temperature) })
        //     )
        // // Add the points
        // console.log(data[0].id)
        // svgElement
        //   .append("g")
        //   .selectAll("dot")
        //   .data(data)
        //   .enter()
        //   .append("circle")
        //     .attr("cx", function(data) { return x(data.id) } )
        //     .attr("cy", function(data) { return y(data.temperature) } )
        //     .attr("r", 5)
        //     .attr("fill", "#69b3a2")
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