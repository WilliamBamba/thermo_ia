import { /*useState,*/ useRef, useEffect } from "react";
import React from 'react';
import * as d3 from 'd3';
import fetch from '../../helpers/fetch';
import config from '../../config';


export default ({ store }) => {

    const svgRef = useRef();

    function graphiqueTemp(svgRef, data) {
        
        console.log('changing graph');

        data = data.sort((a, b) => b.id - a.id).slice(0, 1000)

        let margin = { top: 30, right: 30, bottom: 30, left: 50 },
            width = 610 - margin.left - margin.right,
            height = 300 - margin.top - margin.bottom;

        let svgElement = d3.select(svgRef.current)
            .attr("width", width + margin.left + margin.right)
            .attr("height", height + margin.top + margin.bottom)
            .append("g")
            .attr("transform",
                "translate(" + margin.left + "," + margin.top + ")");

        let min = data[0].created_at;
        let max = data[data.length - 1].created_at;
        // Add X axis --> it is a date format


        let xScale = d3.scaleTime()//.scaleLinear() // #ScaleTime()
            .domain([new Date(max), new Date(min)])
            .range([0, width]);

        svgElement.append("g")
            .attr("transform", "translate(0," + height + ")")
            .call(d3.axisBottom(xScale));

        // Add Y axis
        let yScale = d3.scaleLinear()
            .domain([0, 60])
            .range([height, 0]);

        svgElement.append("g")
            .call(d3.axisLeft(yScale));

        svgElement.append("linearGradient")
            .attr("id", "line-gradient")
            .attr("gradientUnits", "userSpaceOnUse")
            .attr("x1", 0)
            .attr("y1", yScale(0))
            .attr("x2", 0)
            .attr("y2", yScale(60))
            .selectAll("stop")
            .data([
                { offset: "0%", color: "rgb(42,203,236)" },
                { offset: "59%", color: "rgb(232, 194, 5)" },
                { offset: "100%", color: "rgb(252, 33, 33)" }
            ])
            .enter().append("stop")
            .attr("offset", function (d) { return d.offset; })
            .attr("stop-color", function (d) { return d.color; });


        // Add the line
        svgElement.append("path")
            .datum(data)
            .attr("fill", "none")
            .attr("stroke", "url(#line-gradient)")
            .attr("stroke-width", 3)
            .attr("d", d3.line()
                .x((d) => xScale(new Date(d.created_at)))
                .y((d) => yScale(d.temperature)));

    }


    useEffect(() => {
        fetch.getData(config.server + config.routes.sensor.get)
            .then(r => r.json())
            .then(data => graphiqueTemp(svgRef, data))
    }, []);


    return (
        <div id='tempEvolution'>
            <p className='TitreSection'> Evolution Température Intérieure </p>
            <svg ref={svgRef} />
        </div>
    );
};