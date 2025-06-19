---
title: "Constrained optimization and distributed model predictive control-based merging strategies for adjacent connected autonomous vehicle platoons"
collection: publications
category: manuscripts
permalink: /publication/2019-11-12-IEEE-ACCESS
excerpt: 'H. Min, Y. Yang, Y. Fang, P. Sun and X. Zhao, "Constrained Optimization and Distributed Model Predictive Control-Based Merging Strategies for Adjacent Connected Autonomous Vehicle Platoons," in IEEE Access, vol. 7, pp. 163085-163096, 2019, doi: 10.1109/ACCESS.2019.2952049.'
date: 2019-11-12
venue: 'IEEE Access, vol. 7'
status: "published"
# slidesurl: 'http://academicpages.github.io/files/slides2.pdf'
# paperurl: 'https://ieeexplore.ieee.org/abstract/document/8892730'
# citation: 'H. Min, Y. Yang, Y. Fang, P. Sun and X. Zhao, "Constrained Optimization and Distributed Model Predictive Control-Based Merging Strategies for Adjacent Connected Autonomous Vehicle Platoons," in IEEE Access, vol. 7, pp. 163085-163096, 2019, doi: 10.1109/ACCESS.2019.2952049.'
---

---
## Motivation ##

Vehicle platooning has gained significant attention for its potential to improve fuel efficiency, traffic safety, and road utilization. A critical challenge lies in developing practical platoon merging strategies that balance safety and efficiency, especially for connected autonomous vehicles (CAVs). This study addresses the gap by proposing merging maneuvers that account for safe spacing and acceleration limits, ensuring feasible real-world deployment.  
  <img src="/images/publication_2019_IEEE_ACCESS/platoon_merge.gif" style="margin-left: 0px;" width="520" /> 

## Methods ##

The study introduces a distributed model predictive control (DMPC) framework with two key components:  
A space-making DMPC controller that adjusts the target platoon’s trajectory to create safe merging gaps while respecting acceleration constraints.  
A platoon DMPC controller that guides the merge platoon into the target platoon, simplifying the problem by treating the merge as a unified maneuver.  
The DMPC approach enables real-time computation and handles constraints explicitly, enhancing feasibility.  
    <img src="/images/publication_2019_IEEE_ACCESS/methods.png" style="margin-left: 0px;" width="520" /> 

## Experiments and Results ##

Simulations evaluated the strategy across diverse scenarios and parameters, benchmarking it against state-of-the-art methods. The experiments tested robustness to varying traffic conditions, platoon sizes, and acceleration limits. The proposed method outperformed existing approaches in feasibility, efficiency, and computational speed, while rigorously incorporating safety distances and control constraints. Results demonstrated a reliable solution for CAV platoon merging.  
    <img src="/images/publication_2019_IEEE_ACCESS/results_pos.png" style="margin-left: 0px;" width="520" /> 

For more details, the paper can be found [here](https://ieeexplore.ieee.org/document/8892730).