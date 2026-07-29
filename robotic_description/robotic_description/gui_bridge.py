import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState
from std_msgs.msg import Int32MultiArray
import math

class GUIBridge(Node):
    def __init__(self):
        super().__init__('gui_bridge')

        # Publisher → ESP32 topic
        self.pub = self.create_publisher(Int32MultiArray, '/arm_cmd', 10)

        # Subscriber → GUI topic
        self.sub = self.create_subscription(
            JointState,
            '/joint_states',
            self.callback,
            10
        )

    def callback(self, msg):
        out = Int32MultiArray()

        # Convert radians → degrees
        angles = [int(math.degrees(p)) for p in msg.position]

        # 🔥 IMPORTANT: match your joint order
        # Example mapping (CHANGE if needed)
        # base, shoulder, elbow, roll, pitch, gripper
        mapped = [90, 90, 90, 90, 90, 90]

        if len(angles) >= 1:
            mapped[0] = angles[0]   # base
        if len(angles) >= 2:
            mapped[1] = angles[1]   # shoulder
        if len(angles) >= 3:
            mapped[2] = angles[2]   # elbow
        if len(angles) >= 4:
            mapped[3] = angles[3]   # wrist roll

        # Optional defaults
        mapped[4] = 90  # wrist pitch
        mapped[5] = 90  # gripper

        out.data = mapped

        self.get_logger().info(f"Sending: {mapped}")

        self.pub.publish(out)


def main():
    rclpy.init()
    node = GUIBridge()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
