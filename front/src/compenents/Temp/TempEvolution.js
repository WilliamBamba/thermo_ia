import { /*useState,*/ useRef, useEffect } from "react";
import React from 'react';
import * as d3 from 'd3';


export default ({store}) => {

    const svgRef = useRef();

    useEffect(() => {
        const svgElement = d3.select(svgRef.current)
        svgElement
            .append("circle")
            .attr('cx', 150)
            .attr('cy', 70)
            .attr('r',  50)
            .style('fill', 'red')
      }, [])

    return (
        <div id='tempEvolution'>
            <p className='TitreSection'> Evolution Température Intérieure </p>
            <svg ref={svgRef}/>
        </div>
    );
};