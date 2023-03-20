import numpy as np
# reference
# https://zhuanlan.zhihu.com/p/45404840
# https://en.wikipedia.org/wiki/Rotation_matrix

def euler2rotate_maxtrix(vector, order):
    if (order == "zyx" or order == "ypr"):
        yaw   = vector[0]
        pitch = vector[1]
        roll  = vector[2]

        R = np.array([[np.cos(yaw)*np.cos(pitch), np.cos(yaw)*np.sin(pitch)*np.sin(roll)-np.sin(yaw)*np.cos(roll), np.cos(yaw)*np.sin(pitch)*np.cos(roll)+np.sin(yaw)*np.sin(roll)],
                      [np.sin(yaw)*np.cos(pitch), np.sin(yaw)*np.sin(pitch)*np.sin(roll)+np.cos(
                          yaw)*np.cos(roll), np.sin(yaw)*np.sin(pitch)*np.cos(roll)-np.cos(yaw)*np.sin(roll)],
                      [-np.sin(pitch), np.cos(pitch)*np.sin(roll), np.cos(pitch)*np.cos(roll)]])
    else:
        print("unsupported")
    return R


def rotation_matrix2quaternion(R):
    """
    Covert a full three-dimensional rotation matrix into  a quaternion.

    Input
    :param R: A 3x3 element matrix representing the full 3D rotation matrix. 
             This rotation matrix converts a point in the local reference 
             frame to a point in the global reference frame.


    Output
    :return: A 4 element array representing the quaternion (q0,q1,q2,q3) 
    """
    # # 将旋转矩阵转化为四元数
    q0 = np.sqrt(1+R[0, 0]+R[1, 1]+R[2, 2])/2
    q = np.array([np.sqrt(1+R[0, 0]+R[1, 1]+R[2, 2])/2,
                  (R[2, 1]-R[1, 2])/(4*q0),
                  (R[0, 2]-R[2, 0])/(4*q0),
                  (R[1, 0]-R[0, 1])/(4*q0)])
    return q


def quaternion2rotation_matrix(Q):
    """
    Covert a quaternion into a full three-dimensional rotation matrix.

    Input
    :param Q: A 4 element array representing the quaternion (q0,q1,q2,q3) 

    Output
    :return: A 3x3 element matrix representing the full 3D rotation matrix. 
             This rotation matrix converts a point in the local reference 
             frame to a point in the global reference frame.
    """
    # Extract the values from Q
    w = Q[0]
    x = Q[1]
    y = Q[2]
    z = Q[3]

    # # First row of the rotation matrix
    # r00 = 2 * (q0 * q0 + q1 * q1) - 1
    # r01 = 2 * (q1 * q2 - q0 * q3)
    # r02 = 2 * (q1 * q3 + q0 * q2)

    # # Second row of the rotation matrix
    # r10 = 2 * (q1 * q2 + q0 * q3)
    # r11 = 2 * (q0 * q0 + q2 * q2) - 1
    # r12 = 2 * (q2 * q3 - q0 * q1)

    # # Third row of the rotation matrix
    # r20 = 2 * (q1 * q3 - q0 * q2)
    # r21 = 2 * (q2 * q3 + q0 * q1)
    # r22 = 2 * (q0 * q0 + q3 * q3) - 1

    r00 = 1 - 2 * (y * y + z * z)
    r01 = 2 * (x * y - z * w)
    r02 = 2 * (x * z + y * w)

    r10 = 2 * (x * y + z * w)
    r11 = 1 - 2 * (x * x + z * z)
    r12 = 2 * (y * z - x * w)

    r20 = 2 * (x * z - y * w)
    r21 = 2 * (y * z + x * w)
    r22 = 1 - 2 * (x * x + y * y)

    # 3x3 rotation matrix
    rot_matrix = np.array([[r00, r01, r02],
                           [r10, r11, r12],
                           [r20, r21, r22]])

    return rot_matrix


def quaternion_multiply(quaternion1, quaternion0):
    w0, x0, y0, z0 = quaternion0
    w1, x1, y1, z1 = quaternion1
    return np.array([-x1 * x0 - y1 * y0 - z1 * z0 + w1 * w0,
                     x1 * w0 + y1 * z0 - z1 * y0 + w1 * x0,
                     -x1 * z0 + y1 * w0 + z1 * x0 + w1 * y0,
                     x1 * y0 - y1 * x0 + z1 * w0 + w1 * z0], dtype=np.float64)