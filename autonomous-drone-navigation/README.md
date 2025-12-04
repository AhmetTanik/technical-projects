# Autonomous Drone Navigation System

This project demonstrates a **Python/ROS‑based control algorithm** for autonomous quadcopter flight. The goal is to showcase how sensor fusion, obstacle detection, and path planning can be combined into a modular system capable of navigating through complex environments.

## Overview

In 2024 I designed and implemented an autonomous drone navigation system while studying Software Engineering. The system integrates data from multiple sensors, uses obstacle avoidance strategies, and plans a safe path through a simulated environment built with Gazebo. Key achievements from the original project include:

- **Sensor fusion** combining IMU, GPS, and LiDAR/sonar data to estimate the drone's pose.
- **Obstacle detection and avoidance** using simple geometric algorithms and potential fields.
- **Path planning** via a basic A* search algorithm for way‑point generation.
- A **30 % reduction in flight path deviation** during obstacle‑dense missions compared with a baseline controller【423963862728788†L29-L35】.
- Comprehensive documentation and version control using Git.

This repository contains a minimal, self‑contained skeleton illustrating the architecture of the navigation system. The code is meant for educational purposes and does not represent a production‑ready controller. It can be extended to work with ROS and real hardware.

## Structure

```text
autonomous-drone-navigation/
├── README.md               ← Project documentation (this file)
├── src/
│   └── autonomous_drone_navigation.py  ← Python module with sensor fusion, obstacle detection, and path planning classes
└── requirements.txt        ← Python dependencies (optional)
```

### `autonomous_drone_navigation.py`

This script provides class definitions for the core components:

* **`SensorFusion`** – aggregates sensor data to estimate position and velocity.
* **`ObstacleDetector`** – identifies nearby obstacles and recommends avoidance maneuvers.
* **`PathPlanner`** – plans a path from the current position to a goal using a simple A* algorithm.
* **`DroneController`** – coordinates sensor fusion, obstacle detection, and path planning to produce control commands.

You can run the file as a module to see a simple simulation loop. The example uses randomly generated obstacles and a 2‑D grid environment to demonstrate how the components interact.

## Getting Started

1. **Install dependencies**: Ensure you have Python 3.8+ installed. Optionally create a virtual environment. Install dependencies using `pip install -r requirements.txt`.
2. **Run the example**: Navigate to the `src` directory and execute `python autonomous_drone_navigation.py`. You will see printed output showing the sensor estimates, detected obstacles, and chosen path.
3. **Extend with ROS/Gazebo**: To integrate with ROS, create ROS nodes wrapping each class and publish/subscribe to relevant topics. Set up a Gazebo world file with obstacles to simulate a more realistic environment.

## Dependencies

The project can run with standard Python libraries. If you decide to implement ROS integration, you'll need to install ROS (e.g., ROS Noetic) and `rospy`. Additional recommended packages include:

- `numpy` for vector math.
- `scipy` for path planning algorithms.
- `pytest` for testing.

You can list these in `requirements.txt` if you plan to use a package manager.

## Notes

This skeleton provides a starting point for designing a more complex drone controller. Real‑world autonomous systems must consider dynamics, safety constraints, and regulatory requirements. Use this code responsibly and ensure that any hardware testing complies with local regulations.