#!/usr/bin/env python3

import rospy

from std_msgs.msg import String
from std_msgs.msg import UInt8MultiArray

last_emotion = None
count = 0

def emotion_to_action(argument):
    # Use dictionary as swtich-case statement
    switcher = {
	"Angry": [0,0],
	"Disgust": [1,1],
	"Fear": [2,0],
	"Happy": [None,None],
	"Neutral": [3,2],
	"Sad": [3,2],
	"Surprise": [None,None]        
    }

    return switcher.get(argument, [None,None])

def callback(emotion):
    print("received emotion: " + emotion.data)
    global last_emotion
    global count
    
    command = UInt8MultiArray()

    # Only send action if emotion has changed
    if emotion.data != last_emotion: 
        count = 0
        print("different emotion, count reset")
    else:
        print("emotion unchanged")
        if count >= 10:
            command.data = emotion_to_action(last_emotion)
            pub.publish(command)
            count = 0
            print("command sent")
        else:
            count += 1
            print(f"count incremented: count = {count}")
    
    last_emotion = emotion.data


if __name__ == "__main__":
    # Initialize the node
    rospy.init_node('mapping', log_level=rospy.DEBUG)

    # Setup publisher
    pub = rospy.Publisher('/mapping',UInt8MultiArray,queue_size=10)

    # Setup subscriber
    sub = rospy.Subscriber('/emotion',String,callback)

    print("mapping node ready")

    rospy.spin()
