# pikabot

A ROS2 Package of a Webots Simulation of 2-Wheel Differential Drive Robot Capable of SLAM and Autonomous Navigation

How to Install:
1) Go to the src folder of your colcon workspace. cd ~/ros2_ws/src
2) Clone the repository: https://github.com/AddyPete/pikabot.git
3) Go back to the main workspace: cd ~/ros2_ws
4) Build the package: colcon build --packages-select pikabot --symlink-install
5) Then do: source install/setup.bash

How to Run (Without SLAM and Navigation):
1) Type ros2 launch pikabot robot_launch.py
2) Run teleop twist ROS2 package with ros2 run teleop_twist_keyboard teleop_twist_keyboard
