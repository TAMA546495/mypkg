#!/bin/bash
# SPDX-FileCopyrightText: 2024 Yuuki Tamada
# SPDX-License-Identifier: BSD-3-Clause

# 作業ディレクトリの設定
dir=~
[ "$1" != "" ] && dir="$1"   # 引数があったら、そちらをホームに変える

# 作業ディレクトリに移動してビルド
cd $dir/ros2_ws
colcon build
source $dir/.bashrc

# 10秒間タイムアウトでros2のランチャーを実行
timeout 10 ros2 launch mypkg talk_listen.launch.py > /tmp/mypkg.log

# ログファイルの内容を確認して、必要な出力が含まれているかチェック
if grep -q "現在の時間帯は" /tmp/mypkg.log; then
    echo "OK"
    exit 0
else
    echo "テスト失敗: 時間帯メッセージが出力されませんでした。"
    cat /tmp/mypkg.log  # エラーログを出力
    exit 1
fi

