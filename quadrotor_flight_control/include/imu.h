#ifndef __IMU_H
#define __IMU_H
#include <ros/ros.h>
#include <Eigen/Dense>
#include <sensor_msgs/Imu.h>



class Imu_Data_t
{
public:
  Eigen::Quaterniond q;
  Eigen::Vector3d w;
  Eigen::Vector3d a;

  sensor_msgs::Imu msg;
  ros::Time rcv_stamp;

  Imu_Data_t();
  void feed(sensor_msgs::ImuConstPtr pMsg);
};

#endif