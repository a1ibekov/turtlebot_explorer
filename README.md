# turtlebot_explorer

This project implements a sampling-based autonomous exploration strategy for navigating unknown environments using TurtleBot and LiDAR in a Gazebo simulation.

## Folder Structure

```
.
├── config/     # Parameter files and configuration
├── launch/     # ROS launch files
├── maps/       # Saved maps
├── rviz/       # RViz configurations
├── scripts/    # Utility scripts
├── src/
│   └── turtlebot_explorer/
│       ├── __init__.py
│       └── explorer.py
├── worlds/     # Gazebo worlds
```

The `src/turtlebot_explorer/explorer.py` module contains a minimal `Explorer` class that can be extended with exploration logic.
