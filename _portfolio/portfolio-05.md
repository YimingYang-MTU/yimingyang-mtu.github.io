---
title: "From OSM to VISUM: Automated Infrastructure Generation for Transport Planning"  
excerpt: "A Python program to extract transportation features from OpenStreetMap (OSM) for any user-defined geographic area. <img src='/images/portfolio5/osm2visum.png' width='600' height='300'>"  
collection: portfolio  
---

- **Motivation**: In transportation planning, PTV VISUM is a powerful tool for simulating road networks, origin-destination (OD) matrix estimation and analysis, traffic assignment & simulation, etc. However, manually modeling large-scale networks—beyond just a few intersections—becomes time-consuming and inefficient. To streamline this process, I leveraged OSM, an open-source geospatial database, to automate VISUM network generation for large areas. By extracting OSM road topology and converting it into Vissim-compatible formats, this approach significantly reduces manual effort while enabling scalable, high-fidelity traffic simulations.

1. OpenStreetMap (OSM) represents geographic features—such as roads, railways, parks, and points of interest—using nodes, ways, and tags. However, for transportation planning in VISUM, networks must be constructed with guaranteed connectivity to ensure a traversable path exists between any two nodes.
    <img src="/images/portfolio5/osm2visum_node_link.png" alt="Test" width="520" /> 
2. To generate POIs from OSM, extract building/amenity polygons, calculate their centroids and areas, while automated zone division can be achieved by partitioning OSM boundaries into grid-based or administrative units with computed shape points and centroids.
   <img src="/images/portfolio5/osm2visum_zones_1.png" alt="Test" width="520" />  
3. Export functionality to VISUM-compatible formats (e.g., .net or .ver files) with correct link-node topology for traffic assignment. Validated outputs by importing into VISUM for transportation assignment.
     <img src="/images/portfolio5/osm2visum_transportation_assignment_1.png" alt="Test" width="520" />  
4. Enabled rapid scenario testing for urban planning (e.g., new infrastructure impact studies). Reduced manual network-building time from days to minutes.  
    <img src="/images/portfolio5/osm2visum_export.png" alt="Test" width="520" /> 