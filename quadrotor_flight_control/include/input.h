#ifndef __INPUT_H
#define __INPUT_H

#include <ros/ros.h>
#include <Eigen/Dense>

#include <sensor_msgs/Imu.h>
#include <quadrotor_msgs/PositionCommand.h>
#include <quadrotor_msgs/TakeoffLand.h>
#include <nav_msgs/Odometry.h>
#include <mavros_msgs/RCIn.h>
#include <mavros_msgs/State.h>
#include <mavros_msgs/ExtendedState.h>
#include <sensor_msgs/BatteryState.h>
#include "PX4CtrlParam.h"
#include <uav_utils/geometry_utils.h>
#include <uav_utils/converters.h>


class RC_Data_t
{
public:
  double mode;
  double gear;
  double reboot_cmd;
  double last_mode;
  double last_gear;
  double last_reboot_cmd;
  bool have_init_last_mode{false};
  bool have_init_last_gear{false};
  bool have_init_last_reboot_cmd{false};
  double ch[4];

  mavros_msgs::RCIn msg;
  ros::Time rcv_stamp;

  bool is_command_mode;
  bool enter_command_mode;
  bool is_hover_mode;
  bool enter_hover_mode;
  bool toggle_reboot;

  static constexpr double GEAR_SHIFT_VALUE = 0.75;
  static constexpr double API_MODE_THRESHOLD_VALUE = 0.75;
  static constexpr double REBOOT_THRESHOLD_VALUE = 0.5;
  static constexpr double DEAD_ZONE = 0.25;

  RC_Data_t();
  void check_validity();
  bool check_centered();
  void feed(mavros_msgs::RCInConstPtr pMsg);
  bool is_received(const ros::Time &now_time);
};





class State_Data_t
{
public:
  mavros_msgs::State current_state;
  mavros_msgs::State state_before_offboard;

  State_Data_t();
  void feed(mavros_msgs::StateConstPtr pMsg);
};

class ExtendedState_Data_t
{
public:
  mavros_msgs::ExtendedState current_extended_state;

  ExtendedState_Data_t();
  void feed(mavros_msgs::ExtendedStateConstPtr pMsg);
};

class Command_Data_t
{
public:
  EIGEN_MAKE_ALIGNED_OPERATOR_NEW
  Eigen::Vector3d p;
  Eigen::Vector3d v;
  Eigen::Vector3d a;
  Eigen::Vector3d j;
  double yaw;
  double yaw_rate;

  quadrotor_msgs::PositionCommand msg;
  ros::Time rcv_stamp;

  Command_Data_t();
  void feed(quadrotor_msgs::PositionCommandConstPtr pMsg);
};



class Takeoff_Land_Data_t
{
public:
  EIGEN_MAKE_ALIGNED_OPERATOR_NEW
  bool triggered{false};
  uint8_t takeoff_land_cmd; // see TakeoffLand.msg for its defination

  quadrotor_msgs::TakeoffLand msg;
  ros::Time rcv_stamp;

  Takeoff_Land_Data_t();
  void feed(quadrotor_msgs::TakeoffLandConstPtr pMsg);
};

#endif