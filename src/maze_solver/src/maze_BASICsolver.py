#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan   

class mase_BASICsolver():
    def __init__(self):
        # Initializations for robots speed, scan variables.
        rospy.loginfo("Starting basic_solver")
        self.cmd_vel = Twist()
        self.front_sensor_msg = float('inf')
        self.left_sensor_msg = float('inf')
        self.right_sensor_msg = float('inf')
        
        # Initialization for algorithm
        self.threshold = 0.7
        self.linear_speed = 0.5 
        self.angular_speed = 0.9

        # Topics
        self.cmd_vel_topic = "cmd_vel"
        self.front_sensor_topic = "base_scan_1"
        self.left_sensor_topic = "base_scan_2"
        self.right_sensor_topic = "base_scan_3"

        # Correctly subscribe and publish data by topicb(get contact with robot).
        self.rospy_front_sensor_pub = rospy.Subscriber(self.front_sensor_topic, LaserScan, self.front_sensor_callback, queue_size=1)
        self.rospy_left_sensor_pub = rospy.Subscriber(self.left_sensor_topic, LaserScan, self.left_sensor_callback, queue_size=1)
        self.rospy_right_sensor_pub = rospy.Subscriber(self.right_sensor_topic, LaserScan, self.right_sensor_callback, queue_size=1)
        
        # Connect to cmd_vel topic with publisher variable in order to publish robot cmd_vel
        self.cmd_vel_pub = rospy.Publisher(self.cmd_vel_topic, Twist, queue_size=1)

        # Determine appropriate hertz(hz)
        self.rate = rospy.Rate(5)

    def front_sensor_callback(self, msg):
        self.front_sensor_msg = min(msg.ranges)
    def left_sensor_callback(self, msg):
        self.left_sensor_msg = min(msg.ranges)
    def right_sensor_callback(self, msg):
        self.right_sensor_msg = min(msg.ranges)
    
    def basic_solver(self):
        #------------------------
        # Algorithm to search map *c=close *o=open f r l
        # -----------------------
        # 1. If there is no obstacle on front and left and right: turn radially to right - ooo 
        # 2. If there is an obstacle on front, no obstacle on right, no obstacle on left : stop and turn the direction that is "wider"-- coo
        # 3. If there is no obstacle on front and there is obstacle in right and no obstacle on left: go straight -- oco
        # 4. If there is no obstacle on front and no obstacle in right there is obstacle in left: go straight-- ooc
        # 5. If there is obstacle on front, no obstacle on right, obstacle on left, stop and turn right(maybe radially; slow linear high angular) -- coc 
        # 6. If there is no obstacle on front and obstacle on right and left : go forward -- occ
        # 7. If there is an obstacle on front and right no obstacle on left: stop and turn left(maybe radially; slow linear high angular) --cco
        # 8. If there is obstacle on right front and left: stop and turn back -- ccc
        #--------code----------- 
        #1. ooo
        if self.front_sensor_msg >= self.threshold and self.right_sensor_msg >= self.threshold and self.left_sensor_msg >= self.threshold:
            self.cmd_vel.linear.x = self.linear_speed/1.5
            self.cmd_vel.angular.z = self.angular_speed*2
            rospy.loginfo("F:0, R:0, L:0")
        #2. coo
        elif self.front_sensor_msg < self.threshold and self.right_sensor_msg >= self.threshold and self.left_sensor_msg >= self.threshold:
            self.cmd_vel.linear.x = 0.0
            if self.right_sensor_msg >= self.left_sensor_msg:
                self.cmd_vel.angular.z = -self.angular_speed
            else:
                self.cmd_vel.angular.z = self.angular_speed
            rospy.loginfo("F:1, R:0, L:0")
        #3. oco
        elif self.front_sensor_msg >= self.threshold and self.right_sensor_msg < self.threshold and self.left_sensor_msg >= self.threshold:
            self.cmd_vel.linear.x = self.linear_speed/2
            self.cmd_vel.angular.z = self.angular_speed
            rospy.loginfo("F:0, R:1, L:0")
        #4. ooc
        elif self.front_sensor_msg >= self.threshold and self.right_sensor_msg >= self.threshold and self.left_sensor_msg < self.threshold:
            if self.left_sensor_msg <= self.threshold / 3:
                self.cmd_vel.linear.x = self.linear_speed/2
                self.cmd_vel.angular.z = -self.angular_speed
            elif self.left_sensor_msg > self.threshold / 3:
                self.cmd_vel.linear.x = self.linear_speed
                self.cmd_vel.angular.z = 0.0
            rospy.loginfo("F:0, R:0, L:1")
        #5. coc
        elif self.front_sensor_msg < self.threshold and self.right_sensor_msg >= self.threshold and self.left_sensor_msg < self.threshold:
            self.cmd_vel.linear.x = self.linear_speed/2
            self.cmd_vel.angular.z = -self.angular_speed*2
            rospy.loginfo("F:1, R:0, L:1")
        #6. occ
        elif self.front_sensor_msg >= self.threshold and self.right_sensor_msg < self.threshold and self.left_sensor_msg < self.threshold:
            self.cmd_vel.linear.x = self.linear_speed
            self.cmd_vel.angular.z = 0.0
        #7. cco
        elif self.front_sensor_msg < self.threshold and self.right_sensor_msg < self.threshold and self.left_sensor_msg >= self.threshold:
            self.cmd_vel.linear.x = 0.0
            self.cmd_vel.angular.z = self.angular_speed
            rospy.loginfo("F:1, R:1, L:0")
        #8. ccc
        elif self.front_sensor_msg < self.threshold and self.right_sensor_msg < self.threshold and self.left_sensor_msg < self.threshold:
            self.cmd_vel.linear.x = 0.0
            self.cmd_vel.angular.z = -self.angular_speed*5
            rospy.loginfo("F:1, R:1, L:1")
        # Publish the command
        self.cmd_vel_pub.publish(self.cmd_vel)
            
    def run(self):
        while not rospy.is_shutdown():
            self.basic_solver()
            self.rate.sleep()

if __name__ == "__main__":
    rospy.init_node("maze_BASICsolver_py")
    controller = mase_BASICsolver()
    controller.run()