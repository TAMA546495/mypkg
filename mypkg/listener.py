#!/usr/bin/python3
# SPDX-FileCopyrightText: 2024 Yuuki Tamada
# SPDX-License-Identifier: BSD-3-Clause



import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from datetime import datetime


class DateTimeSubscriber(Node):
    def __init__(self):
        super().__init__('datetime_subscriber')
        self.subscription = self.create_subscription(
            String,
            'datetime',
            self.listener_callback,
            10
        )
        self.subscription  # 未使用の変数警告を防ぐ
        self.get_logger().info('DateTimeSubscriber開始')

    def listener_callback(self, msg):
        current_time = datetime.now()
        
        # 受信した日時を日本語で表示
        self.get_logger().info(f'受信した日時: {msg.data}')

        # 時間帯を判定
        hour = current_time.hour
        if 5 <= hour < 12:
            time_of_day = '朝'
        elif 12 <= hour < 18:
            time_of_day = '昼'
        else:
            time_of_day = '夜'

        self.get_logger().info(f'現在の時間帯は「{time_of_day}」です。')


def main():
    rclpy.init()
    node = None
    try:
        node = DateTimeSubscriber()
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

