---
title: "Microscopic Traffic Safety Analysis and macro-level transportation analysis"
excerpt: "Multi-scale traffic analysis combining microscopic safety metrics with macroscopic transportation trends.<br/> <img src='/images/portfolio5/lane_polygon_for_map_matching.png' width='500' height='300'>"
collection: portfolio
---

| Key Information | Details |
| :--- | :--- |
| **Analysis Scale** | Microscopic (Intersection/Agent Level) & Macroscopic (Network/Regional Level) |
| **Primary Datasets** | Waymo Open Dataset, Wejo Connected Vehicle Data |
| **Key Output** | Conflict point modeling, lane polygon map-matching, OD demand matrices |

---

## 🔬 Microscopic Traffic Safety Analysis

Leveraging the **Waymo Dataset**, I conducted granular safety analysis focusing on high-accuracy trajectory and road geometry modeling:

### 1. Agent Dynamics & Trajectory Visualization
Visualizing agent kinetics—including position, velocity, and yaw angle—integrated with underlying pavement markings and road boundaries.

![Agent Dynamics](/images/portfolio5/traffic_analysis.gif)
*_Figure 1: Real-time dynamic agent visualization with road layer overlays._*

---

### 2. Lane Geometry & Connectivity Modeling
Extracting individual lane centerlines, geometries, and topological IDs to model vehicle trajectory paths.

![Lane Geometry](/images/portfolio5/lane_center_line_visualization.png)
*_Figure 2: Extracted lane centerline geometries and connectivity network._*

---

### 3. Intersection Conflict Point Detection
Analyzing spatial interactions to pinpoint conflict points and potential collision zones across complex signalized/unsignalized intersections.

![Conflict Points](/images/portfolio5/conflict_point_intersection.png)
*_Figure 3: Conflict point identification and spatial distribution at intersections._*

---

### 4. Polygon Map-Matching
Generating spatial lane polygon boundaries to facilitate precision map-matching for low-error trajectory alignment.

![Map Matching](/images/portfolio5/lane_polygon_map_matching.png)
*_Figure 4: Detailed lane boundary polygons used for map-matching algorithms._*

---

## 🌐 Macro-Level Transportation Analysis

Using the **Wejo Dataset**, I conducted a large-scale Origin-Destination (OD) analysis to investigate regional travel patterns:

* **Spatial Resolution:** Aggregated at the Census Block Group level.
* **Key Findings:** Identified peak-hour congestion hot-spots, key commuting corridors, and spatial trip distribution dynamics.

![Macro Transportation Analysis](/images/portfolio5/transportation_analysis.png)
*_Figure 5: Origin-Destination flow visualization and mobility patterns at the block group level._*