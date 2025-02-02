# ROS Maze Solver

This repository contains ROS-based maze-solving algorithms developed for the **RobotCraft Competition**. The project includes two versions of maze-solving algorithms: **Basic** (using IR sensors) and **Advanced** (using YDLIDAR). The goal is to navigate a robot through a maze autonomously using ROS (Robot Operating System).

## Features

- **Basic Maze Solver (IR Sensors).**
  - Uses IR sensors for wall detection and navigation.
  - Implements a simple wall-following algorithm to solve the maze.

- **Advanced Maze Solver (YDLIDAR).**
  - Utilizes YDLIDAR for precise mapping and navigation.
  - Implements a more sophisticated algorithm for maze-solving, such as **A*** or **Dijkstra's algorithm**.

- **ROS Integration.**
  - Fully integrated with ROS for communication between sensors, actuators, and the control system.
  - Supports simulation in **Gazebo** and real-world deployment.

## Repository Structure
ros_maze_solver/
├── basic_maze_solver/ # Basic maze solver using IR sensors
│ ├── launch/ # ROS launch files
│ ├── scripts/ # Python scripts for IR sensor-based navigation
│ ├── urdf/ # URDF files for the robot model
│ └── worlds/ # Gazebo world files for simulation
│
├── advanced_maze_solver/ # Advanced maze solver using YDLIDAR
│ ├── launch/ # ROS launch files
│ ├── scripts/ # Python scripts for YDLIDAR-based navigation
│ ├── maps/ # Pre-generated maps for testing
│ └── config/ # Configuration files for YDLIDAR and navigation
│
├── README.md # This file
└── LICENSE # License file


## Requirements

- **ROS Noetic** (or another ROS distribution).
- **Gazebo** for simulation.
- **YDLIDAR** driver (for the advanced solver).
- **Python 3** and necessary ROS packages.


---

## Requirements  

- **ROS Noetic** (or another ROS distribution).  
- **Gazebo** for simulation.  
- **YDLIDAR** driver (for the advanced solver).  
- **Python 3** and necessary ROS packages.

---

## Installation  

- **Clone the Repository:**  
   `git clone https://github.com/zeynelerenkinali/ros_maze_solver.git`  
   `cd ros_maze_solver`

- **Install Dependencies:**  
   `sudo apt-get install ros-noetic-desktop-full`  
   `sudo apt-get install ros-noetic-ydlidar`

- **Build the ROS Workspace:**  
   `catkin_make`  
   `source devel/setup.bash`

- **Run the Simulation:**

   - **For the Basic Maze Solver:**  
     `roslaunch basic_maze_solver maze_world.launch`

   - **For the Advanced Maze Solver:**  
     `roslaunch advanced_maze_solver lidar_maze.launch`

---

## Usage  

**Basic Maze Solver (IR Sensors):**  

- Launch the simulation:  
   `roslaunch basic_maze_solver maze_world.launch`

- Run the wall-following algorithm:  
   `rosrun basic_maze_solver wall_follower.py`

**Advanced Maze Solver (YDLIDAR):**  

- Launch the simulation:  
   `roslaunch advanced_maze_solver lidar_maze.launch`

- Run the advanced navigation algorithm:  
   `rosrun advanced_maze_solver advanced_navigation.py`

---

## Results  

- **Basic Maze Solver:**  
   - The robot successfully navigates the maze using IR sensors and a wall-following algorithm.  
   - Suitable for simple mazes with clear walls.

- **Advanced Maze Solver:**  
   - The robot uses YDLIDAR to create a map of the maze and applies advanced path-planning algorithms.  
   - Capable of solving complex mazes with dynamic obstacles.

---

## Future Improvements  

- **Integration with SLAM:**  
   Implement SLAM (Simultaneous Localization and Mapping) for real-time mapping in unknown environments.

- **Machine Learning:**  
   Explore reinforcement learning for adaptive maze-solving.

- **Optimization:**  
   Improve the efficiency of the navigation algorithms for faster maze-solving.

---

## License  

This project is licensed under the MIT License. See the LICENSE file for details.
