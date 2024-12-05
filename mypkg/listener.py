import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

class Listener(Node):
    def __init__(self):
        super().__init__("Listener")
        self.pub = self.create_publisher(Int16, "countup", 10)
        self.create_timer(0.5, self.cb)
        self.n = 0

    def cb(self):
        msg = Int16()
        msg.data = self.n
        self.pub.publish(msg)
        self.get_logger().info(f"Listen: {msg.data}")
        self.n += 1

def main():
    rclpy.init()
    node = Listener()
    rclpy.spin(node)

