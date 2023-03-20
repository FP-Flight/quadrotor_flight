#ifndef __ODOM_H
#define __ODOM_H 
#include <nav_msgs/Odometry.h>
#include <Eigen/Dense>
#include <ros/ros.h>
#include <uav_utils/converters.h>

class Odom_Data_t
{
public:
  EIGEN_MAKE_ALIGNED_OPERATOR_NEW
  Eigen::Vector3d p;
  Eigen::Vector3d v;
  Eigen::Quaterniond q;
  Eigen::Vector3d w;

  nav_msgs::Odometry msg;
  ros::Time rcv_stamp;
  bool recv_new_msg;

  Odom_Data_t();
  void feed(nav_msgs::OdometryConstPtr pMsg);
};
#endif