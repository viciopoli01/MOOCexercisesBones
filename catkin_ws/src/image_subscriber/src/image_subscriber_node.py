#!/usr/bin/env python3
import sys
import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
# from mooc import NotebookFinder
# sys.meta_path.append(NotebookFinder())
# import ipynb.fs.full.test_exercise import ourCanny
from test_exercise.py import ourCanny

class image_subscriber:

  def __init__(self):
    self.image_pub = rospy.Publisher("/image_subscriber/image_out",Image, queue_size=1)

    self.bridge = CvBridge()
    self.image_sub = rospy.Subscriber("/image_publisher/image_raw",Image,self.callback, queue_size=1)

  def callback(self,data):
    try:
      cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
    except CvBridgeError as e:
      print(e)

    (rows,cols,channels) = cv_image.shape

    # if cols > 60 and rows > 60 :
    #   cv2.circle(cv_image, (int(rows/2),int(cols/2)), int(rows/4), 255)
    cv_image_out = ourCanny(cv_image,75,150)

    self.image_pub.publish(self.bridge.cv2_to_imgmsg(cv_image_out, "mono8"))

def main(args):
  image_subscriber_node = image_subscriber()
  rospy.init_node('image_subscriber', anonymous=True)
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Shutting down")

if __name__ == '__main__':
    main(sys.argv)