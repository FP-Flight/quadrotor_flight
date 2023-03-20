cmake_minimum_required(VERSION 3.0.2)
project(quadrotor_flight_control)

set(CMAKE_BUILD_TYPE "Release")
set(CMAKE_CXX_FLAGS "-std=c++11")
set(CMAKE_CXX_FLAGS_RELEASE "-O3 -Wall -g")

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED
  roscpp
  rospy
  geometry_msgs
  sensor_msgs
  mavros
  quadrotor_msgs
  nav_msgs
  uav_utils
)

## System dependencies are found with CMake's conventions
find_package(Eigen3 REQUIRED) 

## Uncomment this if the package has a setup.py. This macro ensures
## modules and global scripts declared therein get installed
## See http://ros.org/doc/api/catkin/html/user_guide/setup_dot_py.html
# catkin_python_setup()

###################################
## catkin specific configuration ##
###################################
## The catkin_package macro generates cmake config files for your package
## Declare things to be passed to dependent projects
## INCLUDE_DIRS: uncomment this if your package contains header files
## LIBRARIES: libraries you create in this project that dependent projects also need
## CATKIN_DEPENDS: catkin_packages dependent projects also need
## DEPENDS: system dependencies of this project that dependent projects also need
catkin_package(
  INCLUDE_DIRS include
#  LIBRARIES quadrotors_fight_control
#  CATKIN_DEPENDS other_catkin_pkg
#  DEPENDS system_lib
)

###########
## Build ##
###########

## Specify additional locations of header files
## Your package locations should be listed before other locations
include_directories(
 include
 include/${PROJECT_NAME}
 ${catkin_INCLUDE_DIRS}
 ${EIGEN_INCLUDE_DIRS}
)
## Declare a C++ executable
## With catkin_make all packages are built within a single CMake context
## The recommended prefix ensures that target names across packages don't collide
add_executable(${PROJECT_NAME}_node src/px4ctrl_node.cpp
src/input.cpp
src/controller.cpp
src/PX4CtrlFSM.cpp
src/PX4CtrlParam.cpp

src/battery.cpp
src/imu.cpp
src/odom.cpp

)
add_dependencies(${PROJECT_NAME}_node quadrotor_msgs_generate_messages_cpp)

## Specify libraries to link a library or executable target against
target_link_libraries(${PROJECT_NAME}_node
   ${catkin_LIBRARIES}
 )

