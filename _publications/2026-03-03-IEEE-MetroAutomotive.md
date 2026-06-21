---
title: "Geometric and Radiometric Enhancements of Vehicles in LiDAR Point Clouds with Snow Accumulation"
# collection: publications
category: manuscripts
permalink: /publication/2026-03-03-IEEE
excerpt: 'Yiming Yang, Jeremy P. Bos'
status: "Accepted"
date: 2026-03-03
venue: 'IEEE International Workshop on Metrology for Automotive (IEEE MetroAutomotive 2026)'
# slidesurl: 'http://academicpages.github.io/files/slides1.pdf'
paperurl: #'http://academicpages.github.io/files/paper1.pdf'
bibtexurl: #'http://academicpages.github.io/files/bibtex1.bib'
# citation: 'This paper is being reviewed by IEEE Translations-Intelligent Vehicles (T-IV).'
---

---
<!-- # ThermalTrack # -->

  <img src="/images/publication_2026_IEEE_METROAUTOMOTIVE/experiment_picture.png" style="margin-left: 0px;" width="720" /> 

## Motivation ##

While LiDAR perception is critical for autonomous driving, the scientific community has historically treated winter weather—specifically falling snow—purely as atmospheric noise that degrades sensor performance. The impact of snow accumulated on target objects, however, has remained largely unexplored. My recent work was sparked by a surprising observation during preliminary evaluations of the WADS-3D and CADC datasets: heavier snowfall actually led to a counter-intuitive improvement in vehicle detection accuracy due to an increase in object point counts. This unexpected finding motivated me to dig deeper into the physical reasons behind why snow might actually help sensors "see" vehicles better.

## Hypothesis ##

To explain this anomaly, I proposed and investigated two underlying physical mechanisms. The first hypothesis is geometric inflation, which suggests that a layer of accumulated snow physically increases the effective surface area and volume of a vehicle. The second hypothesis involves a radiometric shift from specular to diffuse reflectance. Essentially, the shiny, specular surfaces of a standard car often deflect LiDAR laser pulses away from the sensor, whereas a coating of snow transforms the vehicle into a highly reflective, diffuse surface that scatters light back toward the receiver much more effectively.

  <img src="/images/publication_2026_IEEE_METROAUTOMOTIVE/specular_diffuse_reflection.png" style="margin-left: 0px;" width="520" /> 

## Experiments ##

To validate these hypotheses, we designed a controlled experiment to meticulously analyze LiDAR point counts and intensity distributions. To ensure our findings were robust and sensor-agnostic, we tested these metrics across four different industry-standard LiDAR systems: Ouster, Velodyne, Ruby, and Iris. The results confirmed our theories: accumulated snow not only geometrically inflates the vehicle but fundamentally alters its surface physics. By converting vehicles into diffuse-like reflectors, the snow effectively increases both point density and return intensity, significantly enhancing the visibility and detection of distant vehicles in winter conditions.


