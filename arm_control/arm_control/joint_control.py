import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState
from std_msgs.msg import Float32MultiArray

class ArmController(Node):
    def __init__(self):
        super().__init__('arm_controller')

        self.sub = self.create_subscription(
            JointState,
            '/joint_states',
            self.callback,
            10
        )

        self.pub = self.create_publisher(
            Float32MultiArray,
            '/joint_commands',
            10
        )

    def callback(self, msg):
        cmd = Float32MultiArray()
        cmd.data = list(msg.position)
        self.pub.publish(cmd)

def main(args=None):
    rclpy.init(args=args)
    node = ArmController()
    rclpy.spin(node)
    rclpy.shutdown()
