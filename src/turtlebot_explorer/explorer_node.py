import random

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class Explorer(Node):
    """Simple ROS 2 node that drives the robot randomly."""

    def __init__(self):
        super().__init__('explorer')
        self.cmd_pub = self.create_publisher(Twist, 'cmd_vel', 10)
        self.timer = self.create_timer(5.0, self.move_randomly)
        self.get_logger().info('Explorer node started')

    def move_randomly(self):
        twist = Twist()
        twist.linear.x = random.uniform(0.0, 0.2)
        twist.angular.z = random.uniform(-1.0, 1.0)
        self.cmd_pub.publish(twist)
        self.get_logger().info(
            f'Moving with linear.x: {twist.linear.x:.2f}, angular.z: {twist.angular.z:.2f}'
        )


def main(args=None):
    rclpy.init(args=args)
    node = Explorer()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
