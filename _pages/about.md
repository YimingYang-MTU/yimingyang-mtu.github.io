---
permalink: /
title: "About Me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

<style>
  .hero-gallery {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    margin-top: 10px;
    margin-bottom: 24px;
  }
  .hero-gallery-item {
    position: relative;
    overflow: hidden;
    border-radius: 8px;
    box-shadow: 0 2px 6px rgba(0,0,0,0.08);
    border: 1px solid #e5e7eb;
  }
  .hero-gallery-item img {
    width: 100%;
    height: 240px;
    object-fit: cover;
    display: block;
    transition: transform 0.3s ease;
  }
  .hero-gallery-item:hover img {
    transform: scale(1.03);
  }
  .hero-caption {
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    background: linear-gradient(transparent, rgba(15, 23, 42, 0.78));
    color: #ffffff;
    padding: 12px 10px 6px 10px;
    font-size: 0.78rem;
    font-weight: 500;
  }
  
  @media (max-width: 640px) {
    .hero-gallery {
      grid-template-columns: 1fr;
    }
    .hero-gallery-item img {
      height: 200px;
    }
  }
</style>

<div class="hero-gallery">
  <div class="hero-gallery-item">
    <img src="/images/me/field_work_setup.jpg" alt="Field Data Collection & Sensor Calibration" />
    <div class="hero-caption">Field Data Collection & Sensor Calibration</div>
  </div>
  <div class="hero-gallery-item">
    <img src="/images/me/vehicle_testing.jpg" alt="Autonomous Vehicle Field Testing" />
    <div class="hero-caption">Autonomous Vehicle Testing on Snow & Off-Grid Roads</div>
  </div>
</div>

I am a **Postdoctoral Researcher** at **Oklahoma State University**, working in the School of Civil and Environmental Engineering with. My research spans **Rural Automated Vehicles (RAVs)**, **Foundation Models**, **robust perception in adverse weather** and **Field Robotics**.

<style>
  /* Vertical Research Timeline Styling */
  .timeline-container {
    position: relative;
    padding-left: 28px;
    margin: 32px 0;
    border-left: 3px solid #00070ee7;
  }
  .timeline-card {
    position: relative;
    margin-bottom: 32px;
    padding: 16px 20px;
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.05);
  }
  .timeline-card:last-child {
    margin-bottom: 0;
  }
  .timeline-dot {
    position: absolute;
    left: -37px;
    top: 18px;
    width: 15px;
    height: 15px;
    border-radius: 50%;
    background-color: #01060a;
    border: 3px solid #ffffff;
    box-shadow: 0 0 0 2px #000203;
  }
  .timeline-date {
    font-size: 0.82rem;
    font-weight: 700;
    color: #07869c;
    letter-spacing: 0.5px;
    text-transform: uppercase;
    margin-bottom: 4px;
  }
  .timeline-role {
    font-size: 1.15rem;
    font-weight: 700;
    color: #0f172a;
    margin: 0 0 2px 0;
  }
  .timeline-institution {
    font-size: 0.95rem;
    font-weight: 600;
    color: #475569;
    margin-bottom: 10px;
  }
  .timeline-institution a {
    color: #0366d6;
    text-decoration: none;
  }
  .timeline-institution a:hover {
    text-decoration: underline;
  }
  .timeline-body {
    font-size: 0.92rem;
    color: #334155;
    line-height: 1.55;
  }
  .timeline-body ul {
    margin: 6px 0 10px 18px;
    padding: 0;
  }
  .timeline-body li {
    margin-bottom: 4px;
  }
  .tag-container {
    margin-top: 10px;
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
  }
  .tag {
    display: inline-block;
    padding: 2px 9px;
    font-size: 0.78rem;
    font-weight: 600;
    border-radius: 12px;
    background-color: #e0f2fe;
    color: #0369a1;
    border: 1px solid #bae6fd;
  }
</style>

## Research Journey

<div class="timeline-container">

  <!-- Stage 1: Oklahoma State University -->
  <div class="timeline-card">
    <div class="timeline-dot"></div>
    <div class="timeline-date">2026 – Present</div>
    <h3 class="timeline-role">Postdoctoral Researcher</h3>
    <div class="timeline-institution">
      Oklahoma State University &bull; School of Civil & Environmental Engineering
    </div>
    <div class="timeline-body">
      Working with <a href="https://scholar.google.com/citations?user=OUcKeVkAAAAJ&hl=en" target="_blank">Dr. Joshua Li</a> focusing on rural autonomous driving.
      <ul>
        <li><strong>Zero-Shot VLMs for Rural Driving:</strong> Benchmarking Vision-Language Models for road scene comprehension in off-grid and unpaved conditions.</li>
        <li><strong>Infrastructure Preparedness for Autonomous Driving:</strong> AV-based framework for automated physical/digital infrastructure evaluation.</li>
        <li><strong>Teaching:</strong> ROS 2 and Autoware teaching.</li>
      </ul>
    </div>
    <div class="tag-container">
      <span class="tag">Rural Autonomous Vehicles</span>
      <span class="tag">Vision-Language Models</span>
      <span class="tag">AV Infrastructure Evaluation</span>
    </div>
  </div>

  <!-- Stage 2: Michigan Technological University -->
  <div class="timeline-card">
    <div class="timeline-dot"></div>
    <div class="timeline-date">2021 – 2026</div>
    <h3 class="timeline-role">Ph.D. in Electrical & Computer Engineering</h3>
    <div class="timeline-institution">
      Michigan Technological University &bull; Planetary Surface Technology Development Lab
    </div>
    <div class="timeline-body">
      Advised by <a href="https://scholar.google.com/citations?user=Iacaw6IAAAAJ&hl=en&oi=ao" target="_blank">Dr. Jeremy P. Bos</a>, concentrating on field robotics and off-road/winter vehicle autonomy.
      <ul>
        <li><strong>Adverse Weather Autonomy:</strong> LiDAR-based object detection under severe snowfall.</li>
        <li><strong>Traversability Estimation:</strong> Thermal-RGB fusion and self-supervised wheel track detection for featureless snowy terrains.</li>
        <li><strong>Stochastic Sampling-based Optimal Control:</strong> Model Predictive Path Integral (MPPI) control on low-friction surfaces.</li>

      </ul>
    </div>
    <div class="tag-container">
      <span class="tag">Winter Autonomy</span>
      <span class="tag">LiDAR Object Detection</span>
      <span class="tag">Traversability Estimation</span>
      <span class="tag">MPPI Controller</span>
      <span class="tag">Field Robotics</span>
    </div>
  </div>

  <!-- Stage 3: Chang'an University -->
  <div class="timeline-card">
    <div class="timeline-dot"></div>
    <div class="timeline-date">Prior Stage</div>
    <h3 class="timeline-role">B.S. & M.S. Research Focus</h3>
    <div class="timeline-institution">
      Chang'an University &bull; School of Electrical and Control Engineering
    </div>
    <div class="timeline-body">
      Focused on autonomous vehicle control, trajectory tracking, and connected and automated vehicle (CAV) platoon control.
      <ul>
        <li><strong>Autonomous Vehicle Control:</strong> PID control for gas, brake, steering.<li> <li><strong>Trajectory TRracking:</strong> Purepursuit controller, Model Predictive Control (MPC).<li>
        <li><strong>Platoon Control:</strong> Distributed Model Predictive Control (DMPC) and Deep Deterministic Policy Gradient (DDPG) reinforcement learning.</li>
      </ul>
    </div>
    <div class="tag-container">
      <span class="tag">Autonomous Vehicle</span>
      <span class="tag">PID Control</span>
      <span class="tag">Model Predictive Control</span>
      <span class="tag">Platoon Control</span>
      <span class="tag">Deep Reinforcement Learning</span>
      <span class="tag">Vehicle Dynamics</span>
    </div>
  </div>

</div>

<!-- **Markdown generator**

The repository includes [a set of Jupyter notebooks](https://github.com/academicpages/academicpages.github.io/tree/master/markdown_generator
) that converts a CSV containing structured data about talks or presentations into individual markdown files that will be properly formatted for the Academic Pages template. The sample CSVs in that directory are the ones I used to create my own personal website at stuartgeiger.com. My usual workflow is that I keep a spreadsheet of my publications and talks, then run the code in these notebooks to generate the markdown files, then commit and push them to the GitHub repository.

How to edit your site's GitHub repository
------
Many people use a git client to create files on their local computer and then push them to GitHub's servers. If you are not familiar with git, you can directly edit these configuration and markdown files directly in the github.com interface. Navigate to a file (like [this one](https://github.com/academicpages/academicpages.github.io/blob/master/_talks/2012-03-01-talk-1.md) and click the pencil icon in the top right of the content preview (to the right of the "Raw | Blame | History" buttons). You can delete a file by clicking the trashcan icon to the right of the pencil icon. You can also create new files or upload files by navigating to a directory and clicking the "Create new file" or "Upload files" buttons. 

Example: editing a markdown file for a talk
![Editing a markdown file for a talk](/images/editing-talk.png)

For more info
------
More info about configuring Academic Pages can be found in [the guide](https://academicpages.github.io/markdown/), the [growing wiki](https://github.com/academicpages/academicpages.github.io/wiki), and you can always [ask a question on GitHub](https://github.com/academicpages/academicpages.github.io/discussions). The [guides for the Minimal Mistakes theme](https://mmistakes.github.io/minimal-mistakes/docs/configuration/) (which this theme was forked from) might also be helpful. -->
