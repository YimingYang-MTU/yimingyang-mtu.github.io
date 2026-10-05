---
title: "OSM to VISUM: Automated Infrastructure Generation for Transport Planning"  
excerpt: "An automated toolchain converting OpenStreetMap into VISUM networks.<br/><img src='/images/portfolio6/osm2visum.png' width='600' height='300'>"  
collection: projects  
---

<div style="background: #f8f9fa; border-left: 4px solid #0056b3; padding: 14px 18px; border-radius: 6px; margin: 20px 0 30px 0;">
  <p style="margin: 0; font-size: 0.98em; line-height: 1.6;">
    <strong>Focus:</strong> Transportation Network Generation &amp; Automation &nbsp;|&nbsp; 
    <strong>Tools:</strong> OpenStreetMap (OSM), PTV VISUM, Python &nbsp;|&nbsp; 
    <strong>Impact:</strong> Reduced network creation time from days to minutes
  </p>
</div>

## Motivation & Overview

In transportation planning, PTV VISUM is a standard tool for road network simulation, Origin-Destination (OD) matrix estimation, and traffic assignment. However, manually modeling large-scale networks beyond a few intersections is time-consuming and prone to errors.

To overcome this bottleneck, I developed an automated toolchain leveraging OpenStreetMap to generate VISUM-ready networks for large geographic regions. By extracting raw OSM road topologies and converting them into VISUM-compatible formats, this approach dramatically reduces manual effort while maintaining high-fidelity network structure for simulation.

---

## Automated Pipeline

<div style="display: flex; flex-direction: column; gap: 24px; margin: 24px 0;">

  <!-- Row 1 -->
  <div style="border: 1px solid #e1e4e8; border-radius: 8px; padding: 20px; background: #ffffff;">
    <h3 style="margin-top: 0; color: #0056b3; font-size: 1.1em;">1. Network Topology &amp; Connectivity</h3>
    <p style="font-size: 0.95em; color: #444; line-height: 1.6;">
      Parses raw OSM nodes, ways, and tags into structured links while enforcing guaranteed topological connectivity so every path remains fully traversable for simulation.
    </p>
    <figure style="margin: 16px 0 0 0; text-align: center;">
      <img src="/images/portfolio6/osm2visum_node_link.png" alt="OSM Node and Link Topology" style="max-width: 100%; width: 620px; border-radius: 6px; border: 1px solid #eee;" />
    </figure>
  </div>

  <!-- Row 2 -->
  <div style="border: 1px solid #e1e4e8; border-radius: 8px; padding: 20px; background: #ffffff;">
    <h3 style="margin-top: 0; color: #0056b3; font-size: 1.1em;">2. POI &amp; Traffic Zone Generation</h3>
    <p style="font-size: 0.95em; color: #444; line-height: 1.6;">
      Extracts building/amenity polygons to compute centroids and surface areas, automatically partitioning OSM boundaries into grid-based or administrative traffic zones.
    </p>
    <figure style="margin: 16px 0 0 0; text-align: center;">
      <img src="/images/portfolio6/osm2visum_zones_1.png" alt="Traffic Zone Division" style="max-width: 100%; width: 620px; border-radius: 6px; border: 1px solid #eee;" />
    </figure>
  </div>

  <!-- Row 3 -->
  <div style="border: 1px solid #e1e4e8; border-radius: 8px; padding: 20px; background: #ffffff;">
    <h3 style="margin-top: 0; color: #0056b3; font-size: 1.1em;">3. Format Conversion &amp; Validation</h3>
    <p style="font-size: 0.95em; color: #444; line-height: 1.6;">
      Exports node-link topologies to VISUM formats (<code>.net</code> / <code>.ver</code>). Validated via direct import into VISUM for equilibrium traffic assignment.
    </p>
    <figure style="margin: 16px 0 0 0; text-align: center;">
      <img src="/images/portfolio6/osm2visum_transportation_assignment_1.png" alt="VISUM Traffic Assignment" style="max-width: 100%; width: 620px; border-radius: 6px; border: 1px solid #eee;" />
    </figure>
  </div>

  <!-- Row 4 -->
  <div style="border: 1px solid #e1e4e8; border-radius: 8px; padding: 20px; background: #ffffff;">
    <h3 style="margin-top: 0; color: #0056b3; font-size: 1.1em;">4. Rapid Scenario Testing</h3>
    <p style="font-size: 0.95em; color: #444; line-height: 1.6;">
      Enables rapid urban planning scenario testing (e.g., infrastructure expansion impact studies) while cutting manual modeling time from days down to minutes.
    </p>
    <figure style="margin: 16px 0 0 0; text-align: center;">
      <img src="/images/portfolio6/osm2visum_export.png" alt="VISUM Export and Scenario Testing" style="max-width: 100%; width: 620px; border-radius: 6px; border: 1px solid #eee;" />
    </figure>
  </div>

</div>