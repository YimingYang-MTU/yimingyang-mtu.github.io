---
title: "OSM-to-VISUM Network Converter: Automated Infrastructure Generation for Transport Planning"  
excerpt: "A Python-based tool to extract road networks from OpenStreetMap (OSM) for any user-defined geographic area: <img src='/images/portfolio7/osm2visum.png' width='800' height='500'>"  
collection: portfolio  
---

1. Implemented topology correction to ensure full connectivity (e.g., resolving dead-ends, enforcing node-link relationships).  
2. Automated conversion of OSM XML data into a directed graph (using osmnx/networkx), preserving attributes (e.g., road types, speed limits), applied network simplification to merge redundant nodes while maintaining critical intersections.  
3. Engineered export functionality to VISUM-compatible formats (e.g., .net or .ver files) with correct link-node topology for traffic assignment. Validated outputs by importing into VISUM for microsimulation (e.g., PTV Vissim) and macroscopic modeling.  
4. Enabled rapid scenario testing for urban planning (e.g., new infrastructure impact studies). Reduced manual network-building time from days to minutes.  