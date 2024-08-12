# card-reader-for-RC-S380
A sample program using a card reader (RC-S380/S) and nfcpy to read the name and student ID number from the student card.

カードリーダーを用いて学生証から氏名と学籍番号を読み取るためのサンプルプログラム。

## 参考URL
- https://qiita.com/taiki-kuraishi/items/9c8d7d66bddb9efa20f3

## カードリーダー
- パソリ RC-S380/S

※なお、後継機のRC-S300/S1はnfcpyで値を読み取ることができない。

## 事前準備
- Zadig(USBドライバ)
  - [公式サイト](https://zadig.akeo.ie/)
  - optionからList All Devicesを選択し、driverをWinUSBに変更後Replace Driverをクリック
  - pasoriの元の機能が失われる可能性あり。[参考](https://qiita.com/frameair/items/abcaebbd654c304a0906)
- libusb(ユーザー空間からUSBデバイスと通信できるようにするオープン・ソース・ライブラリ)
  - [公式サイト](https://libusb.info/)
  - DownloadsからLatest Windows Binariesをクリックすることでダウンロードすることができる
    - VS2015-x64\dll\libusb-1.0.dllをC:\Windows\System32に配置
    - VS2015-Win32\dll\libusb-1.0.dllをC:\Windows\SysWOW64に配置

## 仮想環境の作成
- `python -m venv myenv`

## モジュールのインストール
- `pip install nfcpy`

## プログラムの実行
- `myenv\Script\activate`
- `python sample.py`