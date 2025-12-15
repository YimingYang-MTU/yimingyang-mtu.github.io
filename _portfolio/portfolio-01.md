---
title: "SAE Autodrive Challenge II year 2 - 5"
excerpt: "Graduate Teaching Assistant (GTA) for SAE Autodrive Challenge II. <br/><img src='/images/portfolio1/adii_team18.jpg' width='500' height='300'>"
collection: portfolio
---

## Year 4
<hr style="height:2px; border-width:0; color:gray; background-color:gray">
- **Role of year4**: GTA of teams: Controls and Mathworks, Safety and Testing 
- **Tools**: MATLAB/Simulink, MicroAutoBox III dSpace, ROS, DVP&R
- **Achievement 1**: A full-spectrum testing team handling vehicle dynamics, perception/planning, HMI, and mission management systems.
  <img src="/images/portfolio1/safety_and_testing.png" alt="Test" width="520" />
- **Achievement 2**: Developed and finalized the Safety Validation Report (SVR), which details the comprehensive testing and validation status for all requirements listed in the Requirement Traceability Matrix (RTM). The SVR confirms system compliance by presenting test results (from simulation or physical testing) and their conclusions, ensuring every requirement is traceable to an associated safety goal.
  <img src="/images/portfolio1/safety_validation.png" alt="Test" width="520" />
- **Achievement 3**: Completed the Safety of the Intended Functionality (SOTIF) Report (ISO 21448-aligned) to assess and mitigate risks from functional insufficiencies. The report delivered a defined Operational Design Domain (ODD), analyzed relevant use cases, and outlined the minimal risk maneuver and resulting safety requirements needed to ensure the vehicle achieves its minimal risk condition.
  <img src="/images/portfolio1/sotif_analysis.png" alt="Test" width="520" />
- **Achievement 4**: Designed a detailed, high-fidelity test map in one of Michigan Tech's parking lots for the Design Your Own Challenge (DYOC) event. The map was engineered to ensure comprehensive validation of all autonomous vehicle functionalities by incorporating a diverse set of real-world elements, including varied intersection types, multiple traffic signage scenarios, and pedestrian crossings.
  <img src="/images/portfolio1/dyoc.png" alt="Test" width="520" />
- **Achievement 5**: Upgraded the Safe and Robust Autonomy State Machine to expand its functional scope and improve testing flexibility. While retaining the original centralized steering, braking, and propulsion integration and arbitration, the architecture was enhanced to include new capabilities, such as decoupled lateral and longitudinal control. This upgrade enables  mixing manual steering with automated longitudinal control, which is essential for conducting Safety Functionality Validation and meeting complex safe testing requirements for autonomous vehicles.
  <img src="/images/portfolio1/autonomy_state_machine_y4.png" alt="Test" width="520" />  
- **Achievement 6**: Developed a state machine to control the vehicle's exterior signaling system, encompassing left and right turn indicators and hazard warning lights. The system also permits the precise adjustment and tuning of the signal blinking frequency for enhanced operational safety and standards compliance.
  <img src="/images/portfolio1/autonomy_state_machine_lighting.png" alt="Test" width="520" />  
- **Achievement 7**: Implemented and validated the Stanley Controller, replacing the existing Pure Pursuit algorithm to achieve more precise and accurate path-following. This upgrade reduced lateral control errors, imporving the performance and stability during autonomous curving.
  <img src="/images/portfolio1/stanley_controller.png" alt="Test" width="520" />  

---

## Year 3
<hr style="height:2px; border-width:0; color:gray; background-color:gray">

- **Role of year3**: GTA of team: Controls
- **Tools**: MATLAB/Simulink, ROS, MicroAutoBox III dSpace  
- **Achievement 1**: Development of a Safe and Robust Autonomy State Machine that provides centralized integration and arbitration for all core vehicle control functions, including steering, braking, and propulsion. The state machine is designed to ensure functional safety by implementing fault-tolerant logic and deterministic transitions, guaranteeing reliable execution across all operational modes as well as safe exist mechanism.
  <img src="/images/portfolio1/autonomy_state_machine_y3.png" alt="Steering Test" width="520" />
- **Achievement 2**: Implementation and testing of the vehicle's Human-Machine Interface (HMI), collaborating closely with the hardware team across multiple design generations. Successfully evolved the interface through three distinct phases: from a simple physical button setup, to a mixed screen-and-button solution, and finally to an advanced large-format touchscreen system. This iterative process resulting in a significant and quantified improvement in the HMI's effectiveness, clarity, and overall user experience for autonomous system interaction.
  <img src="/images/portfolio1/hmi.png" alt="Steering Test" width="520" />
- **Achievement 3**: Implemented the core HMI Autonomy State Machine responsible for the safe enabling/disabling of the autonomous control model. This state machine integrates key safety-critical logic to manage driver override events and ensures the reliable execution of safe stopping procedures.
  <img src="/images/portfolio1/autonomy_state_machine_hmi.png" alt="Steering Test" width="520" />
- **Achievement 4**: Developed and verified the lighting control functionalities, leveraging the CAN protocol, and Vehicle Spy to manipulate all lighting-related messages on the CAN bus.
  <img src="/images/portfolio1/lighting_control.gif" alt="Test" width="520" />  
- **Achievement 5**: Finalized comprehensive documentation detailing the step-by-step procedures for initializing the autonomous vehicle control via simulation and the dSPACE. This resource ensures system reproducibility and streamlined onboarding for new development team members.
<img src="/images/portfolio1/doc_dspace.png" alt="Steering Test" width="520" />

---

## Year 2
<hr style="height:2px; border-width:0; color:gray; background-color:gray">

- **Role of year2**: GTA of team: Controls
- **Tools**: MATLAB/Simulink, ROS, MicroAutoBox III dSpace.    
- **Object**: Vehicle interface and control through CAN messaging.  

1. **Achievement 1** : Hardware-software integration by collaborating with the hardware team to design and validate robust wire harnesses and CAN bus segmentation, ensuring reliable communication across diverse electronic control units (ECUs).   
  <img src="/images/portfolio1/dspace_in_trunk.jpg" alt="Trunk Rack" width="500" />  
1. **Achievement 2** : Designed and applied a torque-based drive-override mechanism within the steering-by-wire system to ensure instantaneous and safe manual intervention capability during autonomous operation.  
  <img src="/images/portfolio1/steering_test.gif" alt="Steering Test" width="500" />  
1. **Achievement 3** : Engineered and validated propulsion and brake-by-wire control systems, tuning the PID lower-level controllers to deliver highly accurate, stable, and responsive torque and deceleration control, complemented by an instantaneous pedal-actuated drive-override safety mechanism.  
  <img src="/images/portfolio1/propulsion_brake_test.gif" alt="Steering Test" width="500" />  