#!/usr/bin/env python3
import rospy
import numpy as np
from nav_msgs.msg import Odometry
import tf_my
# import time
out_odom = Odometry()

yaw, pitch, roll = -np.pi/2, 0, 0
R1 = tf_my.euler2rotate_maxtrix((yaw, pitch, roll), "zyx")
q1 = tf_my.rotation_matrix2quaternion(R1)
def odom_cb(odometry):
    global R1,q1
    position = np.array([
        odometry.pose.pose.position.x,
        odometry.pose.pose.position.y,
        odometry.pose.pose.position.z
    ])
    linear_v = np.array([
        odometry.twist.twist.linear.x,
        odometry.twist.twist.linear.y,
        odometry.twist.twist.linear.z
    ])

    q2 = np.array([
                odometry.pose.pose.orientation.w,
                odometry.pose.pose.orientation.x,
                odometry.pose.pose.orientation.y,
                odometry.pose.pose.orientation.z])
    # 方向居然不一样
    q_new = tf_my.quaternion_multiply(q2,q1)
    R_new = tf_my.quaternion2rotation_matrix(q_new)
    linear_v_new = np.matmul(np.transpose(R_new),linear_v)
    position_new = np.matmul(np.transpose(R_new),position)

    out_odom.header.frame_id = odometry.header.frame_id
    # out_odom.header.frame_id = "world"

    out_odom.header.stamp = odometry.header.stamp
    out_odom.child_frame_id = "body_px4"
    out_odom.pose.pose.position.x = position[0]
    out_odom.pose.pose.position.y = position[1]
    out_odom.pose.pose.position.z = position[2]
    
    out_odom.twist.twist.linear.x = linear_v[0]
    out_odom.twist.twist.linear.y = linear_v[1]
    out_odom.twist.twist.linear.z = linear_v[2]

    out_odom.pose.pose.orientation.w = q_new[0] 
    out_odom.pose.pose.orientation.x = q_new[1]
    out_odom.pose.pose.orientation.y = q_new[2]
    out_odom.pose.pose.orientation.z = q_new[3]   
    odo_pub.publish(out_odom)
    # auhOdom.vel[0] = odometry.twist.twist.linear.x
    # auhOdom.vel[1] = odometry.twist.twist.linear.y
    # auhOdom.vel[2] = odometry.twist.twist.linear.z
if __name__ == "__main__":
    rospy.init_node("lidar2imuframe")
    # time_factor= rospy.get_param('~time_factor')
    # auhOdom.pos[0]= rospy.get_param('~start_x_pos')
    # auhOdom.pos[1]= rospy.get_param('~start_y_pos')
    # auhOdom.pos[2]= rospy.get_param('~start_z_pos')

    odo_pub = rospy.Publisher("/lidar_odometry", Odometry, queue_size=100,tcp_nodelay=True)
    # odom_sub = rospy.Subscriber("getodom", Odometry, odom_cb)
    odom_sub = rospy.Subscriber(
        "/Odometry", Odometry, odom_cb, tcp_nodelay=True)

    rcv_odom = False
    rospy.spin()