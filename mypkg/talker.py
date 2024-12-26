#!/usr/bin/python3
# SPDX-FileCopyrightText: 2024 Yuuki Tamada
# SPDX-License-Identifier: BSD-3-Clause


import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from datetime import datetime


class DateTimePublisher(Node):
    def __init__(self, timer_period=1.0):
        super().__init__('datetime_publisher')
        self.publisher_ = self.create_publisher(String, 'datetime', 10)
        self.timer = self.create_timer(timer_period, self.publish_datetime)
        self.get_logger().info('DateTimePublisher開始')

    def publish_datetime(self):
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        msg = String()
        msg.data = f'現在の日時: {current_time}'
        self.publisher_.publish(msg)
        self.get_logger().info(f'送信中: {msg.data}')


def main():
    rclpy.init()
    node = None
    try:
        node = DateTimePublisher()
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        if node is not None:
            node.destroy_node()
        rclpy.shutdown()
        print("終了")


if __name__ == '__main__':
    main()

