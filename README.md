# pikabot

A ROS2 Package of a Webots Simulation of 2-Wheel Differential Drive Robot Capable of SLAM and Autonomous Navigation

## Installation

Go to the your colcon workspace.

```bash
  cd ~/ros2_ws
```
Clone the project.

```bash
  git clone https://github.com/AddyPete/pikabot.git pikabot
```

Build with colcon and source install setup.ash

```bash
  colcon build --packages-select pikabot --symlink-install
  source install/setup.bash
```

**How to Run (Without SLAM and Navigation):**
1) Type ros2 launch pikabot robot_launch.py
2) Run teleop twist ROS2 package with ros2 run teleop_twist_keyboard teleop_twist_keyboard
