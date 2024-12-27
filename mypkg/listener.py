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
        

    def listener_callback(self, msg):
        

        # 現在の時刻を解析
        try:
            current_time_str = msg.data.split(" ")[2]  # "現在の日時: YYYY-MM-DD HH:MM:SS" から時刻部分を抽出
            current_time = datetime.strptime(current_time_str, '%H:%M:%S')
            hour = current_time.hour

            # 時間帯の判定
            if 5 <= hour < 11:
                time_of_day = '朝'
            elif 11 <= hour < 17:
                time_of_day = '昼'
            else:
                time_of_day = '晩'

            self.get_logger().info(f'現在の時間帯は{time_of_day}です。')

        except Exception as e:
            self.get_logger().error(f'日時の解析に失敗: {e}')


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

