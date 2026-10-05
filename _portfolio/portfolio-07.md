---
title: "OSM to VISSIM: Automating Large-Scale Traffic Network Modeling"
excerpt: "Automated toolchain parsing OpenStreetMap topology into high-fidelity PTV VISSIM microscopic traffic simulation networks (.inpx)."
collection: portfolio
---

> **Project Summary**  
> **Goal:** Eliminate manual link/connector construction for large PTV VISSIM microscopic simulation models.  
> **Methodology:** Programmatic parsing of OSM tags + MUTCD design rules + spline connector generation.  
> **Output:** Native, simulation-ready VISSIM `.inpx` network files.

## Project Overview

In microscopic traffic simulation, **PTV VISSIM** specializes in modeling complex, dynamic interactions between vehicles, pedestrians, and infrastructure. VISSIM excels at detailed scenarios: signal timing, intersection performance, and connected/autonomous vehicle testing. 

However, manually constructing large networks—with precise lane geometries, signal heads, and driver behavior parameters—is labor-intensive. To automate this, I developed a software pipeline that converts OSM road topology into VISSIM-compatible networks, preserving key microscopic features and enabling rapid model generation for corridor studies or city-scale simulations.

---

## Technical Workflow

<div style="max-width: 680px; margin: 30px auto; display: flex; flex-direction: column; gap: 28px;">

  <!-- Step 1 -->
  <div style="border: 1px solid #e1e4e8; border-radius: 8px; background: #ffffff; padding: 18px; box-shadow: 0 2px 6px rgba(0,0,0,0.05);">
    <h3 style="margin: 0 0 10px 0; color: #0056b3; font-size: 1.1em;">Step 1: Intersection Dimensioning & MUTCD Standards</h3>
    <p style="margin: 0 0 12px 0; font-size: 0.95em; color: #444;">Accurate intersection modeling relies on three key factors: junction control type, approach lane counts (parsed from OSM <code>lanes</code> or inferred from road class), and posted speed limits (from <code>maxspeed</code> tags). MUTCD design templates provide standard lane widths, corner radii, and stop bar placements.</p>
    <div style="height: 280px; display: flex; align-items: center; justify-content: center; background: #fafafa; border-radius: 6px; border: 1px solid #f0f0f0;">
      <img src="/images/portfolio7/vissim_intersection_design.png" alt="Intersection Design" style="max-height: 100%; max-width: 100%; object-fit: contain;" />
    </div>
  </div>

  <!-- Step 2 -->
  <div style="border: 1px solid #e1e4e8; border-radius: 8px; background: #ffffff; padding: 18px; box-shadow: 0 2px 6px rgba(0,0,0,0.05);">
    <h3 style="margin: 0 0 10px 0; color: #0056b3; font-size: 1.1em;">Step 2: Spline-Based Connector Generation</h3>
    <p style="margin: 0 0 12px 0; font-size: 0.95em; color: #444;">Spline-based modeling programmatically constructs VISSIM intersection connectors to smoothly represent diverse vehicle movements, including through paths, left/right turns, and complex turning radii.</p>
    <div style="height: 280px; display: flex; align-items: center; justify-content: center; background: #fafafa; border-radius: 6px; border: 1px solid #f0f0f0;">
      <img src="/images/portfolio7/vissim_intersection_connector.png" alt="Connector Generation" style="max-height: 100%; max-width: 100%; object-fit: contain;" />
    </div>
  </div>

  <!-- Step 3 -->
  <div style="border: 1px solid #e1e4e8; border-radius: 8px; background: #ffffff; padding: 18px; box-shadow: 0 2px 6px rgba(0,0,0,0.05);">
    <h3 style="margin: 0 0 10px 0; color: #0056b3; font-size: 1.1em;">Step 3: Adaptive Link & Alignment Processing</h3>
    <p style="margin: 0 0 12px 0; font-size: 0.95em; color: #444;">Microscopic accuracy requires precise modeling of both intersection connectors and mid-block link segments. The pipeline adaptively handles link types ranging from straight geometric corridors to complex curved alignments.</p>
    <div style="height: 280px; display: flex; align-items: center; justify-content: center; background: #fafafa; border-radius: 6px; border: 1px solid #f0f0f0;">
      <img src="/images/portfolio7/vissim_intersection_link.png" alt="Link Alignment" style="max-height: 100%; max-width: 100%; object-fit: contain;" />
    </div>
  </div>

  <!-- Step 4 -->
  <div style="border: 1px solid #e1e4e8; border-radius: 8px; background: #ffffff; padding: 18px; box-shadow: 0 2px 6px rgba(0,0,0,0.05);">
    <h3 style="margin: 0 0 10px 0; color: #0056b3; font-size: 1.1em;">Step 4: Native .inpx Export & Direct Execution</h3>
    <p style="margin: 0 0 12px 0; font-size: 0.95em; color: #444;">Outputs ready-to-run files in standard PTV VISSIM format (<code>.inpx</code>). Networks can be imported directly into VISSIM for immediate simulation without manual cleanup steps.</p>
    <div style="height: 280px; display: flex; align-items: center; justify-content: center; background: #fafafa; border-radius: 6px; border: 1px solid #f0f0f0;">
      <img src="/images/portfolio7/vissim_network_simulation.png" alt="Network Simulation" style="max-height: 100%; max-width: 100%; object-fit: contain;" />
    </div>
  </div>

</div>