#!/usr/bin/bash
# SPDX-FileCopyrightText: 2024 Yuuki Tamada
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc

ng() {
    echo "NG at Line $1"
    res=1
}

res=0


{
  ros2 run mypkg talker > /tmp/talker.log 2>&1
}&


{
  ros2 run mypkg listener > /tmp/listener.log 2>&1
}&


{
  sleep 10
  echo ""

  
  cat /tmp/listener.log | grep -a '受信した日時: 現在の日時:' || ng ${LINENO}
  cat /tmp/listener.log | grep -a '現在の時間帯は' || ng ${LINENO}
}
echo ""


sleep 5
[ "$res" = 0 ] && echo "OK" || echo "テスト失敗"
exit $res

