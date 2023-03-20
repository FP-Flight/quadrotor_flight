import tf_my
import numpy as np

yaw, pitch, roll = np.pi/2, 0, 0
R1 = tf_my.euler2rotate_maxtrix((yaw, pitch, roll),"zyx")
yaw, pitch, roll = -np.pi/2, 0, 0
R2 = tf_my.euler2rotate_maxtrix((yaw, pitch, roll),"zyx")
# print(R1*R2)
print(np.matmul(R1, R2))
q1 = tf_my.rotation_matrix2quaternion(R1) 
q2 = tf_my.rotation_matrix2quaternion(R2)

q_new = tf_my.quaternion_multiply(q1,q2)
print(q_new)

R_new = tf_my.quaternion2rotation_matrix(q_new)
print(R_new)