---
title: "The Railroad Crossing Vehicle Warning (RCVW) system"
excerpt: "Real-world deployment of a V2X safety warning system. Validated low-latency communication between trains and cars at active Highway-Rail Grade Crossings.<br/><img src='/images/portfolio2/rail_crossing_car_train.jpg' width='500' height='300'>"
collection: portfolio
---

- **Project overview**: The Railroad Crossing Vehicle Warning (RCVW) system is a major step toward eliminating fatalities at highway-rail grade crossings (HRGCs). Developed through a collaboration between Michigan Tech, Battelle, and 2nd Sandbar Productions, RCVW uses connected vehicle (V2X) technology to directly alert drivers of an approaching train, significantly improving safety. We successfully demonstrated this life-saving potential through four live field events in Michigan - utilizing instrumented crossings and vehicles, and extensive virtual simulations in V2I Hub and VISSIM. The comprehensive results, including videos, educational materials, and simulation models, were publicly shared via the Rail Learning System (RLS) and the FRA website to accelerate industry adoption. This project directly supports the national vision of zero fatalities at HRGCs.

- **Role**: Research Assistant 
- **Tools**: VBS, RBS, RSU, V2I hub, VISSIM, Ublox GPS application board, C++  
- **Contributions 1**:  
  System development: provided real-time RTK positioning to VBS by retrieving and processing RTCM correction data from MDOT’s CORS NTRIP network. Created high-precision HRGCs maps to support RCVW system validation. Configured VBS/RBS/RSU and software protocols for V2X communication.   
  <img src="/images/portfolio2/system_in_lab.png" alt="Test" width="520" />  
- **Contributions 2**:  
  Development of hardare-in-the-loop (HIL) virtual demo system for [Railroad Crossing Violation Warning (RCVW)](https://www.rail-learning.mtu.edu/rcvw) application with Connected Vehicles in [Rail Learning System](https://www.rail-learning.mtu.edu/), which is an open learning platform that initially provides basic education on high speed rail topics.  
  <img src="/images/portfolio2/virtual_demo_system.png" alt="Test" width="520" /> 
- **Contributions 3**:  
  I developed and hosted comprehensive virtual demonstrations of the (RCVW) applications within the RLS. This demonstration was executed using the HIL system integrated with a high-fidelity rail-highway crossing model built in PTV Vissim. This co-simulation approach allowed for the rigorous testing and visualization of connected vehicle scenarios and driver alerts under controlled, yet realistic, conditions. 
  <img src="/images/portfolio2/system_animation_2d.gif" alt="Test" width="520" />  
- **Contributions 4**:  
  This simulation were developed in V2I Hub (with RBS/VBS plugins, RSU, OBU, GPS, DVI, and computing platforms) and VISSIM. In V2I Hub, I simulated an RCVW-equipped vehicle passing a grade crossing for four use cases. VISSIM added background traffic and train interactions, showing dynamic vehicle responses to RSU messages and train crossings. Videos from both simulators were recorded and integrated for demonstration.  
  <img src="/images/portfolio2/system_animation_3d.gif" alt="Test" width="520" />
- **Contributions 5**:  
  At the Michigan Rail Conference (Escanaba, MI), I staged a demo route in a parking lot, including an illustrative grade crossing with active warning devices (flashing lights). After a pre-event site visit to establish the route and MAP, attendees experienced rides in RCVW-equipped vehicles.  
  <img src="/images/portfolio2/real_test_michigan_rail_conference.png" alt="Test" width="520" />  
- **Contributions 6**:  
  Two-day field demonstration at two HRGCs in Crystal Falls, Michigan (a gated county road and a state highway with flashing lights), instrumented for RCVW testing. A pre-event visit ensured proper site mapping and communication protocols.  
  <img src="/images/portfolio2/real_test_1.gif" alt="Test" width="520" />


