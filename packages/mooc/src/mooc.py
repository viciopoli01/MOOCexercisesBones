#!/usr/bin/env python2
import sys
import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError



import exercise as mooc_exercise

class image_subscriber:

  def __init__(self):
    self.image_pub = rospy.Publisher("/image_subscriber/image_out",Image, queue_size=1)

    self.bridge = CvBridge()
    self.image_sub = rospy.Subscriber("/camera_node/image/compressed",Image,self.callback, queue_size=1)

  def callback(self,data):
    try:
      cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
    except CvBridgeError as e:
      print(e)

    self.image_pub.publish(self.bridge.cv2_to_imgmsg(mooc_exercise.CannyF(cv_image), "bgr8"))

def main(args):
  image_subscriber_node = image_subscriber()
  rospy.init_node('image_subscriber', anonymous=True)
  rospy.spin()

if __name__ == '__main__':
    main(sys.argv)