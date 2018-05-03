import rospy
from geometry_msgs.msg import Pose, PoseWithCovarianceStamped, Point, Quaternion, Twist
import json
from json import dumps, loads, JSONEncoder, JSONDecoder
import urllib2
import time #for sleep()
import roslib
import pickle

url="http://ec2-18-216-168-161.us-east-2.compute.amazonaws.com/scott-server-test/locate.php?locate"

class PythonObjectEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (list, dict, str, unicode, int, float, bool, type(None))):
            return JSONEncoder.default(self, obj)
        return {'_python_object': pickle.dumps(obj)}

def as_python_object(dct):
    if '_python_object' in dct:
        return pickle.loads(str(dct['_python_object']))
    return dct


def callback(msgAMCL):
	poseAMCLx = msgAMCL.pose.pose.position.x;
	poseAMCLy = msgAMCL.pose.pose.position.y;
	poseAMCLw = msgAMCL.pose.pose.orientation.w;
	poseAMCLz = msgAMCL.pose.pose.orientation.z;
        data={
		'poseAMCLx':poseAMCLx,
		'poseAMCLy':poseAMCLy,
		'poseAMCLw':poseAMCLw,
		'poseAMCLz':poseAMCLz
	}

	headers = {'Content-Type': 'application/json'}
	request = urllib2.Request(url, headers=headers, data=json.dumps(data, cls=PythonObjectEncoder))
	response = urllib2.urlopen(request)
        rospy.loginfo(msgAMCL);

def listener():

	rospy.init_node('amcl_sub', anonymous=False)
	rospy.Subscriber("amcl_pose",PoseWithCovarianceStamped,callback)
	rospy.spin()



if __name__ == '__main__':
	listener()
