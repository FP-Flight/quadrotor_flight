# QGC install in Ubuntu 20.04

[QGC official website](https://docs.qgroundcontrol.com/master/en/getting_started/download_and_install.html)


## 环境配置
```bash
sudo usermod -a -G dialout $USER
sudo apt-get remove modemmanager -y
sudo apt install gstreamer1.0-plugins-bad gstreamer1.0-libav gstreamer1.0-gl -y
sudo apt install libqt5gui5 -y
sudo apt install libfuse2 -y
```

下载 GQC
```
cd ~ && wget https://d176tv9ibo4jno.cloudfront.net/latest/QGroundControl.AppImage

```
重启电脑
给执行权限
```bash
chmod +x ./QGroundControl.AppImage
```

## RUN
```
~/QGroundControl.AppImage
```

## BUG
### 1. 6C 没有办法刷固件
6C比较新QGC4.24之后才添加了支持，请先在[Github_releases](https://github.com/mavlink/qgroundcontrol/releases)页面下载最新版本
