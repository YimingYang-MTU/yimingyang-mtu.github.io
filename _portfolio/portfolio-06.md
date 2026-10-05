---
title: "OSM to VISUM: Automated Infrastructure Generation for Transport Planning"
excerpt: "An automated toolchain converting OpenStreetMap geospatial data into fully connected PTV VISUM traffic simulation networks."
collection: portfolio
---

> **Project Summary**  
> **Goal:** Automate large-scale PTV VISUM network modeling using OpenStreetMap.  
> **Key Capabilities:** Topology connectivity checking, POI/Zone partitioning, native `.net`/`.ver` export.  
> **Efficiency Gain:** Reduced network creation time from days to minutes.

## Overview & Motivation

In transportation planning, **PTV VISUM** is a powerful tool for simulating road networks, origin-destination (OD) matrix estimation, and traffic assignment. However, manually modeling large-scale networks—beyond just a few intersections—is time-consuming and inefficient. 

To streamline this process, this project leverages **OpenStreetMap (OSM)**, an open-source geospatial database, to automate VISUM network generation. By extracting OSM road topology and converting it into VISUM-compatible formats, this approach significantly reduces manual modeling effort while enabling scalable, high-fidelity traffic simulations.

---

## Technical Workflow

<div style="max-width: 680px; margin: 30px auto; display: flex; flex-direction: column; gap: 28px;">

  <!-- Step 1 -->
  <div style="border: 1px solid #e1e4e8; border-radius: 8px; background: #ffffff; padding: 18px; box-shadow: 0 2px 6px rgba(0,0,0,0.05);">
    <h3 style="margin: 0 0 10px 0; color: #0056b3; font-size: 1.1em;">Step 1: Topology Extraction & Network Connectivity</h3>
    <p style="margin: 0 0 12px 0; font-size: 0.95em; color: #444;">OSM represents geographic features using nodes, ways, and tags. To ensure valid VISUM routing, the algorithm guarantees continuous link-node connectivity so a traversable path exists across the entire network graph.</p>
    <div style="height: 280px; display: flex; align-items: center; justify-content: center; background: #fafafa; border-radius: 6px; border: 1px solid #f0f0f0;">
      <img src="/images/portfolio6/osm2visum_node_link.png" alt="Node and Link Topology" style="max-height: 100%; max-width: 100%; object-fit: contain;" />
    </div>
  </div>

  <!-- Step 2 -->
  <div style="border: 1px solid #e1e4e8; border-radius: 8px; background: #ffffff; padding: 18px; box-shadow: 0 2px 6px rgba(0,0,0,0.05);">
    <h3 style="margin: 0 0 10px 0; color: #0056b3; font-size: 1.1em;">Step 2: Zone Partitioning & POI Generation</h3>
    <p style="margin: 0 0 12px 0; font-size: 0.95em; color: #444;">Extracts building and amenity polygons, calculating centroids and surface areas. Automated zone division partitions OSM boundaries into grid-based or administrative units with computed shape points.</p>
    <div style="height: 280px; display: flex; align-items: center; justify-content: center; background: #fafafa; border-radius: 6px; border: 1px solid #f0f0f0;">
      <img src="/images/portfolio6/osm2visum_zones_1.png" alt="Zone Division and POIs" style="max-height: 100%; max-width: 100%; object-fit: contain;" />
    </div>
  </div>

  <!-- Step 3 -->
  <div style="border: 1px solid #e1e4e8; border-radius: 8px; background: #ffffff; padding: 18px; box-shadow: 0 2px 6px rgba(0,0,0,0.05);">
    <h3 style="margin: 0 0 10px 0; color: #0056b3; font-size: 1.1em;">Step 3: Export & Traffic Assignment Validation</h3>
    <p style="margin: 0 0 12px 0; font-size: 0.95em; color: #444;">Exports formatted <code>.net</code> and <code>.ver</code> files containing correct link-node topology. Network validity is verified directly by running assignment models inside VISUM.</p>
    <div style="height: 280px; display: flex; align-items: center; justify-content: center; background: #fafafa; border-radius: 6px; border: 1px solid #f0f0f0;">
      <img src="/images/portfolio6/osm2visum_transportation_assignment_1.png" alt="Transportation Assignment" style="max-height: 100%; max-width: 100%; object-fit: contain;" />
    </div>
  </div>

  <!-- Step 4 -->
  <div style="border: 1px solid #e1e4e8; border-radius: 8px; background: #ffffff; padding: 18px; box-shadow: 0 2px 6px rgba(0,0,0,0.05);">
    <h3 style="margin: 0 0 10px 0; color: #0056b3; font-size: 1.1em;">Step 4: Rapid Urban Scenario Testing</h3>
    <p style="margin: 0 0 12px 0; font-size: 0.95em; color: #444;">Enables quick scenario testing for urban planning and impact assessment studies, slashing network setup time from days down to minutes.</p>
    <div style="height: 280px; display: flex; align-items: center; justify-content: center; background: #fafafa; border-radius: 6px; border: 1px solid #f0f0f0;">
      <img src="/images/portfolio6/osm2visum_export.png" alt="Exported Network Visualization" style="max-height: 100%; max-width: 100%; object-fit: contain;" />
    </div>
  </div>

</div>