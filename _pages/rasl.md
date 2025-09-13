---
layout: archive
#title: "CV"
permalink: /rasl/
author_profile: true
---

{% include base_path %}

  <img src="/images/rasl/robotics_sensor_pods.png" style="margin-left: 0px;" alt="Test" width="820" />  

## Overview ##
 The Robust Autonomous Systems Laboratory (RASL) in the Department of Electrical and Computer Engineering at
 Michigan Tech focuses on improving the performance of autonomous systems in adverse, real-world conditions. Our
 research is grounded in the unique challenges of Michigan’s Upper Peninsula, where we stress-test perception and
 navigation systems in heavy snowfall, icy roads, and unstructured off-road environments. Through rigorous sensor
 benchmarking, developing novel algorithms for winter autonomy, and creating resilient off-road path planning solu
 tions, we identify the precise failure points of current technology. This hands-on expertise in diagnostics is essential
 for developing the measurement science and robust evaluation standards needed to ensure safety

## Facilities and Resources ##
The RASL lab is equipped with a diverse fleet of platforms and sensors to support research in perception and autonomy. Beyond our hardware resources, our unique location in Michigan's Upper Peninsula provides an unparalleled natural laboratory for advancing autonomous systems in genuine adverse winter conditions.

## Unique Location ##
Nestled in Houghton, Michigan, in the heart of the Lake Superior snowbelt, RASL has a major strategic advantage: immediate access to a severe, real-world winter testing environment. With over 200 inches of annual snowfall, long winters, and frequent storms, our location is perfect for gathering challenging sensor data in truly tough conditions - the kind that are very hard to recreate in a lab or milder climates. Rather than a challenge, this extreme environment is a core research asset. It acts as a consistent and demanding natural lab, allowing for the quick and cost-effective collection of important data from Lidar, Radar, cameras, and other systems. This access lets us build datasets in real adverse weather that would otherwise be very difficult and expensive to get. This provides a unique advantage for thoroughly testing the robustness and safety of autonomous systems.

## Hardwares ##
To support advanced research in perception and autonomy, the RASL lab is equipped with a comprehensive, high-performance sensor suite. This includes an array of LiDARs such as the Luminar Iris, Robosense Ruby 128-channel, and Ouster OS1-64, complemented by a variety of RGB, thermal, and event cameras. These sensors are integrated into our diverse all-weather ground fleet, featuring 5x Clearpath Jackals (IP56) and 2x Clearpath Husky A200s (IP66), ensuring robust data collection in challenging environments. The entire pipeline is supported by high-performance GPU clusters for the rapid training and validation of our machine learning models.

## Research ##
  * LiDAR Benchmarking
  * Adverse weather autonomy
  * Off-road path planning
  * Terrain generation

## Selected Projects ##

### 1. Winter Adverse Driving Dataset (WADS) ###

<img src="/images/rasl/robotics_sensor_pods_image_lidar_winter.png" style="margin-left: 5px;" alt="Test" width="820" />  

  * Funding Agency/Sponsor: IRAD.
  * Description: WADS addresses a critical gap in autonomous systems research by providing the first large-scale, multimodal dataset focused exclusively on severe winter weather. WADS features challenging conditions, including heavy snowfall and white-outs, that disable most perception systems. The multi-modal sensor suite includes LiDAR and cameras across the visible, NIR, and LWIR spectrums. WADS has 45 TB of data collected and includes 2,000 annotated LiDAR sequences with over 3.6 billion labeled points. Its value to the research community is demonstrated by over 80,000 downloads, making it Michigan Tech’s most impactful public dataset.

### 2. AutoDrive Challenge I & II ###
  * Funding Agency/Sponsor: General Motors & SAE International.
  * Description: Developing a fully autonomous Level-4 passenger vehicle, including robust perception systems using LiDAR and cameras. This work provides our team with extensive hands-on experience in sensor calibration, data synchronization, sensor fusion and real-world system integration in challenging environments like those found in Houghton.

### 3. NEXTCAR I & II ###
  * Funding Agency/Sponsor: Advanced Research Projects Agency-Energy (ARPA-E).
  * Description: In this multi-phase ARPA-E project, RASL developed and deployed a LiDAR-based perception system for fuel-efficient platooning. Our work centered on creating a 3D tracking algorithm for precise relative state estimation to enable stable, close-formation driving, and a novel method for estimating upcoming road grade from the point cloud to proactively optimize the powertrain.

### 4. NIST: Standards Development Center for Automated Driving Systems in Inclement Winter Weather ###
  * Funding Agency/Sponsor: Department of Commerce (DOC).
  * Description: RASL is establishing a national center to create the foundational test methods and standards for Automated Driving Systems (ADS) in winter weather. Our role is to systematically characterize the performance degradation of individual sensors - including LiDAR, optical and infrared cameras, and radar - through both component-level testing and real-world data collection from our ADS-equipped vehicle fleet.  We then use this data to validate the performance of state-of-the-art machine learning models, providing the objective analysis needed by standards organizations and government agencies. This project positions our lab at the forefront of developing the crucial measurement science required to ensure the safety and reliability of autonomous systems in all weather conditions.

### 5. Enabling WNS Management via Autonomous Monitoring of Microclimates and Animal State in Bat Hibernacula ###
  * Funding Agency/Sponsor: US Dept of the Interior/US Fish and Wildlife Service (FWS).
  * Description: RASL is developing an autonomous system for monitoring bat populations. By integrating thermal and NIR cameras with machine learning algorithms, the system automatically counts bats and analyzes their clustering and behavioral states. This technology provides researchers with unprecedented, continuous data on bat activity and social dynamics, empowering studies on behavior, seasonal distribution, and population trends. It represents a transformative tool for moving wildlife ecology from periodic sampling to continuous, data-rich observation.
