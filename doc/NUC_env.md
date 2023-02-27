# 1.系统安装

## 1.1.分区

1. EFI 分区 512M
2. SWAP 分区 内存大小两倍
3. 主分区 剩下的

系统安装时间 约 2min，安装前务必断网，（因为联网安装时ubuntu会自动下载一些东西，非常慢）

# 2.环境配置(ubuntu20.04)

```bash
# 1.换源(清华源) （也可以选中科大）
sudo sed -i "s@http://.*archive.ubuntu.com@https://mirrors.tuna.tsinghua.edu.cn@g" /etc/apt/sources.list
sudo sed -i "s@http://.*security.ubuntu.com@https://mirrors.tuna.tsinghua.edu.cn@g" /etc/apt/sources.list

# 1.换源(中科大)
sudo sed -i 's@//.*archive.ubuntu.com@//mirrors.ustc.edu.cn@g' /etc/apt/sources.list

# 2.安装必要的工具
sudo apt update
sudo apt install -y net-tools openssh-server git vim curl terminator htop

# 3.设置魔法
mkdir -p install && cd install 
git clone https://gitee.com/wangdaochuan/auto-clash-cli.git
cd auto-clash-cli
touch clash_link.txt
vim clash_link.txt  # 将url复制进去
./config_clash.sh AMD64
#

# 4.安装ROS Neotic
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
sudo apt update $apt_proxy
sudo apt install -y ros-noetic-desktop-full $apt_proxy
echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc
source ~/.bashrc

# 5. 安装Realsense 驱动
# https://github.com/IntelRealSense/librealsense/blob/master/doc/distribution_linux.md
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-key F6E65AC044F831AC80A06380C8B3A55A6F3EFCDE || sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-key F6E65AC044F831AC80A06380C8B3A55A6F3EFCDE
sudo add-apt-repository "deb https://librealsense.intel.com/Debian/apt-repo $(lsb_release -cs) main" -u
sudo apt-get install -y librealsense2-dkms librealsense2-utils librealsense2-dev
librealsense2-dbg $apt_proxy

# 6. 必要的 ROS package 安装
sudo apt install -y ros-noetic-ddynamic-reconfigure ros-noetic-mavros ros-noetic-realsense2-camera $apt_proxy
## mavros需要下载一些额外的依赖才能正常使用
cd /opt/ros/noetic/lib/mavros/
sudo vim ./install_geographiclib_datasets.sh
# 从第四行开始 添加
export http_proxy=http://127.0.0.1:7890
export https_proxy=http://127.0.0.1:7890
export HTTP_PROXY=http://127.0.0.1:7890
export HTTPS_PROXY=http://127.0.0.1:7890
########
# 保存并退出


sudo ./install_geographiclib_datasets.sh

# 7.安装 ceres
sudo apt-get install -y libgoogle-glog-dev libgflags-dev
sudo apt-get install -y libatlas-base-dev
sudo apt-get install -y libeigen3-dev
sudo apt-get install -y libsuitesparse-dev
cd ~ && mkdir -p lib && cd lib
curl http://ceres-solver.org/ceres-solver-2.1.0.tar.gz -o cere-2.1.tar.gz
tar zxf cere-2.1.tar.gz
mkdir ceres-bin
cd ceres-bin
cmake ../ceres-solver-2.1.0
make -j16
sudo make install
```

