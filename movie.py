import cv2
import sys
import rospy
import roslib
from cv_bridge import CvBridge
import numpy as np
from sensor_msgs.msg import Image

delay = 30
window_name = 'frame'

args = sys.argv

rospy.init_node('image_feature', anonymous=True)

print(args[1])
file_path = args[1]
image_pub = rospy.Publisher("image_data",Image,queue_size = 10)


cap = cv2.VideoCapture(file_path)

if not cap.isOpened():
    sys.exit()
rate = rospy.Rate(30)  # 30hz

while True:
    ret, frame = cap.read()
    if ret:
        cv2.imshow(window_name, frame)
        # make bridge
        bridge = CvBridge()
        msg = bridge.cv2_to_imgmsg(frame, encoding="bgr8")
        image_pub.publish(msg)

        if cv2.waitKey(delay) & 0xFF == ord('q'):
            break
    else:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
    rate.sleep()

cv2.destroyWindow(window_name)

