---
title: "The Railroad Crossing Vehicle Warning (RCVW) system"
excerpt: "V2X safety warning system deployed at active Highway-Rail Grade Crossings.<br/><img src='/images/portfolio3/rail_crossing_car_train.jpg' width='500' height='300'>"
collection: portfolio
---

<!-- ==========================================
     PROJECT OVERVIEW CONTAINER
     ========================================== -->
<div style="margin-bottom: 40px; background: #fafafa; border: 1px solid #e5e7eb; border-radius: 12px; padding: 24px;">

  <!-- Metadata Bar -->
  <div style="border-bottom: 2px solid #2563eb; padding-bottom: 16px; margin-bottom: 20px;">
    <h2 style="margin: 0 0 12px 0; font-size: 26px; color: #1e293b;">Railroad Crossing Vehicle Warning (RCVW) System</h2>
    
    <div style="display: flex; flex-wrap: wrap; gap: 12px; font-size: 14px;">
      <div style="background: #eff6ff; border: 1px solid #bfdbfe; color: #1e40af; padding: 6px 12px; border-radius: 6px;">
        <strong>Role:</strong> Research Assistant
      </div>
      <div style="background: #f3f4f6; border: 1px solid #e5e7eb; color: #374151; padding: 6px 12px; border-radius: 6px;">
        <strong>Tools:</strong> VBS, RBS, RSU, V2I Hub, PTV Vissim, Ublox GPS (RTK), C++
      </div>
    </div>
  </div>

  <!-- Project Summary -->
  <div style="margin-bottom: 20px;">
    <h3 style="margin: 0 0 10px 0; font-size: 18px; color: #0f172a;">Project Overview</h3>
    <p style="margin: 0 0 16px 0; color: #4b5563; line-height: 1.6;">
      The Railroad Crossing Vehicle Warning (RCVW) system is a V2X safety initiative aiming to eliminate fatalities at Highway-Rail Grade Crossings (HRGCs). Developed in collaboration between Michigan Tech, Battelle, and 2nd Sandbar Productions, RCVW uses connected vehicle technology to directly alert drivers of approaching trains. The system was validated across four live field events in Michigan using instrumented vehicles/crossings alongside virtual co-simulations in V2I Hub and PTV Vissim. Results and training materials were publicly published on the <a href="https://www.rail-learning.mtu.edu/" target="_blank" style="color: #2563eb; text-decoration: underline;">Rail Learning System (RLS)</a> and FRA website to support national zero-fatality crossing safety goals.
    </p>
    <img src="/images/portfolio3/team_photo.jpg" alt="RCVW Team Photo" style="max-width: 100%; width: 520px; height: auto; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.08);" />
  </div>

</div>

<!-- ==========================================
     KEY CONTRIBUTIONS
     ========================================== -->
<h2 style="margin: 0 0 20px 0; font-size: 24px; color: #1e293b;">Key Technical Contributions</h2>

<div style="display: flex; flex-direction: column; gap: 24px;">

  <!-- Contribution 1 -->
  <div style="background: #fff; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.04);">
    <h3 style="margin: 0 0 8px 0; font-size: 18px; color: #0f172a;">1. V2X System Hardware Configuration &amp; RTK Mapping</h3>
    <p style="margin: 0 0 12px 0; color: #475569; line-height: 1.5;">
      Provided real-time RTK positioning to VBS by retrieving and processing RTCM corrections from MDOT’s CORS NTRIP network. Generated high-precision HRGC maps to support RCVW validation, and configured VBS, RBS, and RSU hardware and software protocols for V2X communication.
    </p>
    <img src="/images/portfolio3/system_in_lab.png" alt="System Setup in Lab" style="max-width: 100%; width: 520px; height: auto; border-radius: 6px;" />
  </div>

  <!-- Contribution 2 -->
  <div style="background: #fff; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.04);">
    <h3 style="margin: 0 0 8px 0; font-size: 18px; color: #0f172a;">2. Hardware-in-the-Loop (HIL) Virtual Demo Platform</h3>
    <p style="margin: 0 0 12px 0; color: #475569; line-height: 1.5;">
      Developed a Hardware-in-the-Loop (HIL) virtual demonstration system for the <a href="https://www.rail-learning.mtu.edu/rcvw" target="_blank" style="color: #2563eb; text-decoration: underline;">RCVW Application</a> integrated into the <a href="https://www.rail-learning.mtu.edu/" target="_blank" style="color: #2563eb; text-decoration: underline;">Rail Learning System (RLS)</a> open education platform.
    </p>
    <img src="/images/portfolio3/virtual_demo_system.png" alt="Virtual Demo System" style="max-width: 100%; width: 520px; height: auto; border-radius: 6px;" />
  </div>

  <!-- Contribution 3 -->
  <div style="background: #fff; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.04);">
    <h3 style="margin: 0 0 8px 0; font-size: 18px; color: #0f172a;">3. PTV Vissim Co-Simulation &amp; Driver Alert Evaluation</h3>
    <p style="margin: 0 0 12px 0; color: #475569; line-height: 1.5;">
      Developed and hosted comprehensive RCVW virtual demonstrations in RLS. The platform combined physical HIL hardware with a high-fidelity rail-highway crossing model in PTV Vissim, enabling testing and visualization of connected vehicle scenarios and driver alert timings under controlled conditions.
    </p>
    <img src="/images/portfolio3/system_animation_2d.gif" alt="2D Simulation Animation" style="max-width: 100%; width: 520px; height: auto; border-radius: 6px;" />
  </div>

  <!-- Contribution 4 -->
  <div style="background: #fff; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.04);">
    <h3 style="margin: 0 0 8px 0; font-size: 18px; color: #0f172a;">4. V2I Hub Integration &amp; 3D Multi-Scenario Simulation</h3>
    <p style="margin: 0 0 12px 0; color: #475569; line-height: 1.5;">
      Simulated RCVW-equipped vehicles passing grade crossings across four use cases in V2I Hub (utilizing RBS/VBS plugins, RSU, OBU, GPS, DVI, and computing units). Coupled with PTV Vissim to model surrounding traffic and train dynamics, recording synchronized multi-angle demonstration videos.
    </p>
    <img src="/images/portfolio3/system_animation_3d.gif" alt="3D Simulation Animation" style="max-width: 100%; width: 520px; height: auto; border-radius: 6px;" />
  </div>

  <!-- Contribution 5 -->
  <div style="background: #fff; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.04);">
    <h3 style="margin: 0 0 8px 0; font-size: 18px; color: #0f172a;">5. Michigan Rail Conference Live Demonstration</h3>
    <p style="margin: 0 0 12px 0; color: #475569; line-height: 1.5;">
      Staged an interactive demonstration route at the Michigan Rail Conference (Escanaba, MI) featuring an active grade crossing with flashing lights. Established site mapping beforehand and conducted live ride-along demonstrations for conference attendees in RCVW-equipped vehicles.
    </p>
    <img src="/images/portfolio3/real_test_michigan_rail_conference.png" alt="Michigan Rail Conference Test" style="max-width: 100%; width: 520px; height: auto; border-radius: 6px;" />
  </div>

  <!-- Contribution 6 -->
  <div style="background: #fff; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.04);">
    <h3 style="margin: 0 0 8px 0; font-size: 18px; color: #0f172a;">6. Field Testing at Active HRGCs (Crystal Falls, MI)</h3>
    <p style="margin: 0 0 12px 0; color: #475569; line-height: 1.5;">
      Executed a two-day field testing campaign across two active Highway-Rail Grade Crossings in Crystal Falls, MI (a gated county road and a state highway with flashing lights). Conducted pre-event mapping and protocol setup to validate real-world RCVW warning triggers.
    </p>
    <img src="/images/portfolio3/real_test_1.gif" alt="Real Field Test" style="max-width: 100%; width: 520px; height: auto; border-radius: 6px;" />
  </div>

</div>