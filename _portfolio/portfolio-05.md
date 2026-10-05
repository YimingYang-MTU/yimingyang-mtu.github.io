---
title: "Microscopic Traffic Safety & Macro-Level Transportation Analysis"
excerpt: "Multi-scale traffic analysis combining granular microscopic safety metrics with macroscopic mobility trends."
collection: portfolio
header:
  teaser: "/images/portfolio5/lane_polygon_map_matching.png"
---

<!-- Quick Metadata Header -->
<div style="background-color: #f8f9fa; border-left: 4px solid #2b5797; padding: 16px 20px; border-radius: 6px; margin-bottom: 30px;">
  <p style="margin: 0; font-size: 1.02em; line-height: 1.6;">
    <strong>Scope:</strong> Microscopic Traffic Safety & Macroscopic Urban Mobility<br/>
    <strong>Datasets:</strong> Waymo Open Motion Dataset, Wejo Connected Vehicle Data<br/>
    <strong>Key Focus:</strong> Agent Dynamics, Map Matching, Conflict Analysis, Block-Group OD Trends
  </p>
</div>

## 🔬 Microscopic Traffic Safety Analysis

Leveraging the **Waymo Open Motion Dataset**, this research conducts granular safety and agent interaction analysis across four spatial dimensions.

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 24px; margin: 25px 0;">

  <!-- Card 1: Agent Dynamics (GIF) -->
  <div style="border: 1px solid #e1e4e8; border-radius: 8px; background: #ffffff; padding: 16px; box-shadow: 0 2px 8px rgba(0,0,0,0.06); display: flex; flex-direction: column; justify: space-between;">
    <div style="height: 240px; display: flex; align-items: center; justify-content: center; background-color: #fdfdfd; border-radius: 6px; overflow: hidden; border: 1px solid #f0f0f0;">
      <img src="/images/portfolio5/traffic_analysis.gif" alt="Agent Dynamics GIF" style="max-height: 100%; max-width: 100%; object-fit: contain;" />
    </div>
    <div style="margin-top: 12px;">
      <h4 style="margin: 0 0 6px 0; color: #2b5797; font-size: 1.05em;">1. Agent Trajectory & Dynamics</h4>
      <p style="margin: 0; font-size: 0.9em; color: #555;">Visualization of agent position, velocity vector, and yaw angle synchronized with road markings.</p>
    </div>
  </div>

  <!-- Card 2: Lane Centerlines -->
  <div style="border: 1px solid #e1e4e8; border-radius: 8px; background: #ffffff; padding: 16px; box-shadow: 0 2px 8px rgba(0,0,0,0.06); display: flex; flex-direction: column; justify: space-between;">
    <div style="height: 240px; display: flex; align-items: center; justify-content: center; background-color: #fdfdfd; border-radius: 6px; overflow: hidden; border: 1px solid #f0f0f0;">
      <img src="/images/portfolio5/lane_center_line_visualization.png" alt="Lane Center Line Visualization" style="max-height: 100%; max-width: 100%; object-fit: contain;" />
    </div>
    <div style="margin-top: 12px;">
      <h4 style="margin: 0 0 6px 0; color: #2b5797; font-size: 1.05em;">2. Lane Geometry Extraction</h4>
      <p style="margin: 0; font-size: 0.9em; color: #555;">Extraction of lane IDs, centerlines, and topological connectivity graphs.</p>
    </div>
  </div>

  <!-- Card 3: Conflict Points -->
  <div style="border: 1px solid #e1e4e8; border-radius: 8px; background: #ffffff; padding: 16px; box-shadow: 0 2px 8px rgba(0,0,0,0.06); display: flex; flex-direction: column; justify: space-between;">
    <div style="height: 240px; display: flex; align-items: center; justify-content: center; background-color: #fdfdfd; border-radius: 6px; overflow: hidden; border: 1px solid #f0f0f0;">
      <img src="/images/portfolio5/conflict_point_intersection.png" alt="Conflict Points at Intersection" style="max-height: 100%; max-width: 100%; object-fit: contain;" />
    </div>
    <div style="margin-top: 12px;">
      <h4 style="margin: 0 0 6px 0; color: #2b5797; font-size: 1.05em;">3. Intersection Conflict Identification</h4>
      <p style="margin: 0; font-size: 0.9em; color: #555;">Spatial identification of safety-critical vehicle interaction points at complex intersections.</p>
    </div>
  </div>

  <!-- Card 4: Lane Polygons -->
  <div style="border: 1px solid #e1e4e8; border-radius: 8px; background: #ffffff; padding: 16px; box-shadow: 0 2px 8px rgba(0,0,0,0.06); display: flex; flex-direction: column; justify: space-between;">
    <div style="height: 240px; display: flex; align-items: center; justify-content: center; background-color: #fdfdfd; border-radius: 6px; overflow: hidden; border: 1px solid #f0f0f0;">
      <img src="/images/portfolio5/lane_polygon_map_matching.png" alt="Lane Polygon Map Matching" style="max-height: 100%; max-width: 100%; object-fit: contain;" />
    </div>
    <div style="margin-top: 12px;">
      <h4 style="margin: 0 0 6px 0; color: #2b5797; font-size: 1.05em;">4. Map Matching via Lane Polygons</h4>
      <p style="margin: 0; font-size: 0.9em; color: #555;">Generation of boundary polygons enabling sub-meter map-matching precision.</p>
    </div>
  </div>

</div>

---

## 🌐 Macro-Level Transportation Analysis

Using high-resolution **Wejo connected vehicle data**, this section explores macro-scale origin-destination (OD) mobility dynamics to quantify urban traffic flow patterns.

* **Block-Group Mobility Modeling**: Analyzes daily movement trends across census block groups.
* **Congestion Hotspot Detection**: Highlights peak-hour bottleneck corridors and trip distribution density.

<div style="max-width: 720px; margin: 30px auto; border: 1px solid #e1e4e8; border-radius: 8px; padding: 16px; background: #ffffff; box-shadow: 0 2px 8px rgba(0,0,0,0.06); text-align: center;">
  <div style="background-color: #fdfdfd; padding: 10px; border-radius: 6px; border: 1px solid #f0f0f0;">
    <img src="/images/portfolio5/transportation_analysis.png" alt="Macro Transportation Analysis" style="max-width: 100%; height: auto; border-radius: 4px;" />
  </div>
  <p style="font-size: 0.88em; color: #666; margin: 12px 0 0 0; font-style: italic;">
    Figure 5: Block-group level origin-destination mobility patterns and flow intensity visualization.
  </p>
</div>