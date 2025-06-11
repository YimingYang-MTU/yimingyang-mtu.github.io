---
title: "Project: Key technologies for driverless commercial vehicle control systems"
excerpt: "CAN buse communication, steering, throttle, brake calibration of autonomous gas vehicle:<br/>
 Motion Control System <img src='/images/portfolio10/gas_xinda.png' width='500' height='300'>"
collection: portfolio
---

1. Motion control system<br/>
Designed and implemented throttle-by-wire, brake-by-wire (pump pressure control), and steer-by-wire systems for precise vehicle actuation.<br/>
Developed incremental PID control algorithms for smooth and responsive dynamic adjustments.<br/>
1. Safety-Critical Remote Control<br/>
Engineered a fail-safe remote controller with:<br/>
Real-time motion override capability (throttle/brake/steering).<br/>
Emergency stop (E-stop) system with hardware redundancy (mechanical + software triggers).<br/>
1. Robust Power Distribution<br/>
Architected power supply system for:<br/>
Microcontroller & compute units (stable 12V/5V/3.3V rails).<br/>
Sensor suite (LiDAR, IMU, cameras) with noise isolation and surge protection.<br/>
1. Trajectory Tracking Algorithms<br/>
Implemented and tuned two-tier path tracking:<br/>
Pure Pursuit for waypoint-following (optimized lookahead distance).<br/>
Model Predictive Control (MPC) for dynamic obstacle avoidance (solved with OSQP).<br/>
Achieved <0.2m lateral error at 60 km/h in highway tests.<br/>
