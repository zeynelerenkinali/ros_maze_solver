#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Range   

class mase_BASICsolver():
    def __init__(self):
        # Initializations for robots speed, scan variables.
        self.cmd_vel = Twist()
        self.front_sensor_msg = Range()
        self.left_sensor_msg = Range()
        self.right_sensor_msg = Range()

        # Initialization for algorithm
        
        # Topics
        self.cmd_vel_topic = "cmd_vel"
        self.front_sensor_topic = "base_scan_1"
        self.left_sensor_topic = "base_scan_2"
        self.right_sensor_topic = "base_scan_3"

        # Correctly subscribe and publish data by topicb(get contact with robot).
        self.rospy_front_sensor_pub = rospy.Subscriber(self.front_sensor_topic, Range, self.front_sensor_callback, queue_size=1)
        self.rospy_left_sensor_pub = rospy.Subscriber(self.left_sensor_topic, Range, self.left_sensor_callback, queue_size=1)
        self.rospy_right_sensor_pub = rospy.Subscriber(self.right_sensor_topic, Range, self.right_sensor_callback, queue_size=1)
        
        # Connect to cmd_vel topic with publisher variable in order to publish robot cmd_vel
        self.pub_CMD = rospy.Publisher(self.cmd_vel_topic, Twist, queue_size=1)

        # Determine appropriate hertz(hz)
        self.rate = rospy.Rate(5)

    def front_sensor_callback(self, msg):
        self.front_sensor_msg = msg
    def left_sensor_callback(self, msg):
        self.left_sensor_msg = msg
    def right_sensor_callback(self, msg):
        self.right_sensor_msg = msg
    
    def basic_solver(self):
            #------------------------
            # Algorithm to search map
            # -----------------------
            #--------code----------- 
            # Publish the command
            self.pub_CMD.publish(self.cmd_vel)
            
    def run(self):
        while not rospy.is_shutdown():
            self.basic_solver()
            self.rate.sleep()

if __name__ == "__main__":
    rospy.init_node("maze_BASICsolver_py")
    controller = mase_BASICsolver()
    controller.run()