# turtlebot_explorer

This package contains a very small example of autonomous exploration for TurtleBot3 in ROS 2. The `Explorer` node publishes random velocity commands so the robot wanders around a Gazebo world.

## Folder Structure

```
.
├── launch/                 # Launch files
├── resource/               # ament resource index
├── src/
│   └── turtlebot_explorer/
│       ├── __init__.py
│       └── explorer_node.py
├── package.xml
└── setup.py
```

## Building

Create a ROS 2 workspace and clone this repository into the `src` folder. Then build with `colcon`:

```bash
cd ~/ros2_ws
colcon build --packages-select turtlebot_explorer
source install/setup.bash
```

Ensure that the TurtleBot3 Gazebo packages are installed:

```bash
sudo apt install ros-humble-turtlebot3-gazebo
```

## Running

Launch Gazebo with the exploration node:

```bash
# Set the TurtleBot model for Gazebo
export TURTLEBOT3_MODEL=burger
ros2 launch turtlebot_explorer explore.launch.py
```

The robot will spawn in the default TurtleBot3 world and start moving randomly, demonstrating a very simple exploration behavior.

