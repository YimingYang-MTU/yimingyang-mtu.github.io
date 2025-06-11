---
title: "From OSM to VISSIM: Automating Large-Scale Traffic Network Modeling"  
excerpt: "A Python program to extract road networks from OpenStreetMap (OSM) for any user-defined geographic area: <img src='/images/portfolio6/vissim_network.png' width='600' height='300'>"  
collection: portfolio  
---

- **Motivation**: In microscopic traffic simulation, PTV VISSIM specializes in modeling complex, dynamic interactions between vehicles, pedestrians, and infrastructure. VISSIM excels at detailed scenarios: signal timing, intersection performance, and connected/autonomous vehicle testing. However, manually constructing large networks (with precise lane geometries, signal heads, and driver behavior parameters) is labor-intensive. To automate this, I developed a pipeline that converts OSM road topology into VISSIM-compatible networks, preserving key microscopic features. This approach enables rapid generation of high-resolution models for corridor studies or city-scale simulations while maintaining VISSIM’s fidelity in emulating real-world traffic dynamics.  

1. When converting OSM road networks to VISSIM, accurate intersection modeling requires dimensioning based on three key factors: (1) the intersection type/level (e.g., signalized, stop-controlled, or roundabout), (2) the number of approach lanes per connecting link (derived from OSM's lanes tag or inferred from road class), and (3) the posted speed limit (from OSM maxspeed or regional defaults). For standardized layouts, the MUTCD (Manual on Uniform Traffic Control Devices) provides typical design templates—e.g., lane widths, corner radii, and stop bar placements—which should be referenced to ensure realistic geometry.  
     <img src="/images/portfolio6/vissim_intersection_design.png" alt="Test" width="520" />  
2. Spline-based modeling generates VISSIM intersection connectors capable of accurately representing diverse movement types, including through movements, left/right turns, and complex irregular turning paths.
    <img src="/images/portfolio6/vissim_intersection_connector.png" alt="Test" width="520" /> 
3. In VISSIM, accurate traffic simulation requires precise modeling of both intersection connectors and the links between intersections. The proposed methodology adaptively processes link types from regular geometric to complex irregular alignments, ensuring network fidelity across diverse scenarios.
    <img src="/images/portfolio6/vissim_intersection_link.png" alt="Test" width="520" /> 
4. The proposed program generates output files in the standard PTV VISSIM format (.inpx), which can be directly imported and executed in VISSIM for immediate simulation. This ensures full compatibility with VISSIM’s native environment while eliminating manual conversion steps.   
    <img src="/images/portfolio6/vissim_network_simulation.png" alt="Test" width="520" /> 