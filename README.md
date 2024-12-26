# mypkg                                                                                                                        
ロボットシステム学授業用

# 現在日時表示ノード
 [![test](https://github.com/TAMA546495/robosys2024/actions/workflows/test.yml/badge.svg)](https://github.com/TAMA546495/robosys2024/actions/workflows/test.yml)

## テスト環境
- Ubuntu20.4 LTS
- ROS2 Humble Hawksbil

## 開発環境
- ubuntu20.04 LTS
- ROS2 Humble Hawksbil
- Python 3

## 概要

- このノードはパブリッシャーから現在の日時を送信し、サブスクライバーで朝昼晩のメッセージを受信するものです。
- 現在の時刻が知りたいときに便利です。

## 使用方法

- 以下のリポジトリをクローンして、ディレクトリを移動します。
```
$ git clone https://github.com/TAMA546495/mypkg.git
$ cd ~/ros2_ws/src/mypkg
```

## 実行方法
- 端末1パブリッシャー
```
$ ros2 run mypkg talker                                        
[INFO] [1735234199.677088561] [datetime_publisher]: DateTimePublisher開始
[INFO] [1735234200.665418640] [datetime_publisher]: 送信中: 現在の日時: 2024-12-27 02:30:00

```
- 端末2サブスクライバー
```
$ ros2 run mypkg listener
[INFO] [1735234470.163040036] [datetime_subscriber]: DateTimeSubscriber開始
[INFO] [1735234470.349724468] [datetime_subscriber]: 受信した日時: 現在の日時: 2024-12-27 02:34:30
[INFO] [1735234470.350324116] [datetime_subscriber]: 現在の時間帯は「夜」です。
```

## ライセンス
- このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布および使用が許可されます。


## クレジット

- このパッケージのコードは、下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを、本人の許可を得て自身の著作としたものです。
- [ryuichiueda/my_slides robosys_2022](https://github.com/ryuichiueda/slides_marp/tree/169907a7645812969a347a91caed6246febd6bf1/robosys2024)

- © 2024 Yuuki Tamada

