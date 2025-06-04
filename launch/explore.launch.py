from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, SetEnvironmentVariable
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
import os
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    tb3_model = os.environ.get('TURTLEBOT3_MODEL', 'burger')

    tb3_world = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory('turtlebot3_gazebo'),
                'launch',
                'turtlebot3_world.launch.py'
            )
        )
    )

    explorer = Node(
        package='turtlebot_explorer',
        executable='explorer',
        output='screen'
    )

    return LaunchDescription([
        SetEnvironmentVariable('TURTLEBOT3_MODEL', tb3_model),
        tb3_world,
        explorer,
    ])
