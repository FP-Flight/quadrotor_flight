#ifndef __BATTERY_H
#define __BATTERY_H
#include <ros/ros.h>
#include <Eigen/Dense>
#include <sensor_msgs/BatteryState.h>
class Battery_Data_t
{
public:
  EIGEN_MAKE_ALIGNED_OPERATOR_NEW
  double volt{0.0};
  double percentage{0.0};

  sensor_msgs::BatteryState msg;
  ros::Time rcv_stamp;

  Battery_Data_t();
  void feed(sensor_msgs::BatteryStateConstPtr pMsg);
};
#endif