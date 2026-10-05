---
title: "OSM to VISSIM: Automating Large-Scale Traffic Network Modeling"  
excerpt: "Generating high-fidelity VISSIM networks from OSM, rapid setup of large-scale microscopic traffic simulations.<br/><img src='/images/portfolio7/vissim_network.png' width='600' height='300'>"  
collection: projects  
---

<div style="background: #f8f9fa; border-left: 4px solid #0056b3; padding: 14px 18px; border-radius: 6px; margin: 20px 0 30px 0;">
  <p style="margin: 0; font-size: 0.98em; line-height: 1.6;">
    <strong>Focus:</strong> Microscopic Traffic Simulation &amp; Network Automation &nbsp;|&nbsp; 
    <strong>Tools:</strong> OpenStreetMap (OSM), PTV VISSIM (.inpx), Python &nbsp;|&nbsp; 
    <strong>Standards:</strong> MUTCD Geometry Compliance
  </p>
</div>

## Motivation & Overview

In microscopic traffic simulation, PTV VISSIM specializes in modeling complex, dynamic interactions among vehicles, pedestrians, and signal infrastructure. While VISSIM excels at detailed scenarios—such as signal timing optimization, intersection performance evaluation, and connected/autonomous vehicle (CAV) testing—manually constructing large networks with lane-level geometry is exceptionally labor-intensive.

To streamline this process, I developed an automated pipeline that converts OpenStreetMap road topology into VISSIM-compatible networks while preserving critical microscopic parameters. This methodology enables the rapid generation of high-resolution models for corridor studies and city-scale simulations, maintaining VISSIM’s high fidelity in emulating real-world traffic dynamics.

---

## Automated Pipeline

<div style="display: flex; flex-direction: column; gap: 24px; margin: 24px 0;">

  <!-- Row 1 -->
  <div style="border: 1px solid #e1e4e8; border-radius: 8px; padding: 20px; background: #ffffff;">
    <h3 style="margin-top: 0; color: #0056b3; font-size: 1.1em;">1. Intersection Dimensioning &amp; Standardized Layouts</h3>
    <p style="font-size: 0.95em; color: #444; line-height: 1.6;">
      Dimensioning is calculated using three key factors: intersection control type (signalized, stop-controlled, roundabout), approach lane counts (from OSM tags or road classification), and posted speed limits. Layouts incorporate <strong>MUTCD (Manual on Uniform Traffic Control Devices)</strong> design standards for accurate lane widths, corner radii, and stop bar placements.
    </p>
    <figure style="margin: 16px 0 0 0; text-align: center;">
      <img src="/images/portfolio7/vissim_intersection_design.png" alt="Intersection Design and Geometry" style="max-width: 100%; width: 620px; border-radius: 6px; border: 1px solid #eee;" />
    </figure>
  </div>

  <!-- Row 2 -->
  <div style="border: 1px solid #e1e4e8; border-radius: 8px; padding: 20px; background: #ffffff;">
    <h3 style="margin-top: 0; color: #0056b3; font-size: 1.1em;">2. Spline-Based Connector Generation</h3>
    <p style="font-size: 0.95em; color: #444; line-height: 1.6;">
      Utilizes spline-based geometric modeling to generate smooth VISSIM intersection connectors. This accurately represents various movement maneuvers, including straight-through paths, left/right turns, and complex irregular turning trajectories.
    </p>
    <figure style="margin: 16px 0 0 0; text-align: center;">
      <img src="/images/portfolio7/vissim_intersection_connector.png" alt="Spline-Based Intersection Connectors" style="max-width: 100%; width: 620px; border-radius: 6px; border: 1px solid #eee;" />
    </figure>
  </div>

  <!-- Row 3 -->
  <div style="border: 1px solid #e1e4e8; border-radius: 8px; padding: 20px; background: #ffffff;">
    <h3 style="margin-top: 0; color: #0056b3; font-size: 1.1em;">3. Link Topology &amp; Alignment Processing</h3>
    <p style="font-size: 0.95em; color: #444; line-height: 1.6;">
      Adaptively processes inter-intersection links alongside interior connectors. Handles alignments ranging from standard grid geometries to complex curved/irregular roadways, ensuring network-wide topological fidelity.
    </p>
    <figure style="margin: 16px 0 0 0; text-align: center;">
      <img src="/images/portfolio7/vissim_intersection_link.png" alt="Link and Connector Alignment" style="max-width: 100%; width: 620px; border-radius: 6px; border: 1px solid #eee;" />
    </figure>
  </div>

  <!-- Row 4 -->
  <div style="border: 1px solid #e1e4e8; border-radius: 8px; padding: 20px; background: #ffffff;">
    <h3 style="margin-top: 0; color: #0056b3; font-size: 1.1em;">4. Native VISSIM Export (.inpx) &amp; Execution</h3>
    <p style="font-size: 0.95em; color: #444; line-height: 1.6;">
      Generates native <code>.inpx</code> network files that can be directly opened and executed inside PTV VISSIM without requiring manual post-processing or manual geometric corrections.
    </p>
    <figure style="margin: 16px 0 0 0; text-align: center;">
      <img src="/images/portfolio7/vissim_network_simulation.png" alt="VISSIM Network Simulation Output" style="max-width: 100%; width: 620px; border-radius: 6px; border: 1px solid #eee;" />
    </figure>
  </div>

</div>