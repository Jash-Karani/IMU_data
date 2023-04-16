#!/usr/bin/env python3
# license removed for brevity
import rospy
from std_msgs.msg import String
import time
from sensor_msgs.msg import Imu
from geometry_msgs.msg import Vector3
def talker():
    pub = rospy.Publisher('my_imu_data', Imu, queue_size=10)
    rospy.init_node('publisher', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    ax=0
    ay=0
    az=9.8
    alphay=0
    counter=0
    timezero=time.time()
    while not rospy.is_shutdown():
        counter+=1
        if ax<2.5:
           ax=(time.time()-timezero)
           alphay=(time.time()-timezero)*4
           linear_obj = Vector3(ax,ay,az)
           angular_obj = Vector3(0,0,alphay)
           final_obj=Imu(linear_acceleration=linear_obj,angular_velocity=angular_obj)
        rospy.loginfo(final_obj)
        pub.publish(final_obj)
        rate.sleep()


if __name__ == '__main__':
    try:
        talker()

    except rospy.ROSInterruptException:
        pass