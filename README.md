# mypkg                                                                                                                        
ロボットシステム学授業用

# 現在日時表示/判定ノード
[![test](https://github.com/TAMA546495/mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/TAMA546495/mypkg/actions/workflows/test.yml)

## テスト環境
- Ubuntu
  22.04.5
  LTS
 

## 開発環境
- Ubuntu
  22.04.5
  LTS
- Python 3

## 概要

- このノードはパブリッシャーから現在の日時を送信し、サブスクライバーで朝昼晩のメッセージを受信するものです。
- 現在の時刻が知りたいときに便利です。
- 5時〜11時:朝　11時〜17時:昼　17時〜5時:晩

## 使用方法

- 以下のリポジトリをクローンして、ディレクトリを移動します。
```
$ git clone https://github.com/TAMA546495/mypkg.git
$ cd ~/ros2_ws/src/mypkg
```

## 実行方法
- datetime_publisher node
```
$ ros2 run mypkg talker                                        
[INFO] [1735234199.677088561] [datetime_publisher]: DateTimePublisher開始
[INFO] [1735234200.665418640] [datetime_publisher]:  2024-12-27 02:30:00
```
- パブリッシュするトピック
  'datetime'
- 型:String



- hantei_subscriber node
```
$ ros2 run mypkg listener
[INFO] [1735234470.350324116] [hantei_subscriber]: 「晩」です。
```
- サブスクライブするトピック
　'hantei'
- 型:String




## 著作権・ライセンス
- このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布および使用が許可されます。
- © 2025 Yuuki Tamada

