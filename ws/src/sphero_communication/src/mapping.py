#!/usr/bin/env python3

import rospy

from std_msgs.msg import String
from std_msgs.msg import UInt8

last_emotion = None
count = 0

def emotion_to_action(argument):
    # Use dictionary as swtich-case statement
    switcher = {
	"Angry": 0,
	"Disgust": 1,
	"Fear": 2,
	"Happy": 3,
	"Neutral": 4,
	"Sad": 5,
	"Surprise": 6        
    }

    return switcher.get(argument, None)

def callback(emotion):
    print("received emotion: " + emotion.data)
    global last_emotion
    global count
    
    command = UInt8()

    # Only send action if emotion has changed
    if emotion.data != last_emotion: 
        if command.data != None:
            count = 0
            print("count reset")
        else:
            print("emotion not recognized")
    else:
        print("emotion unchanged")
        if count >= 10:
            command.data = emotion_to_action(last_emotion)
            pub.publish(command)
            count = 0
            print("action sent")
        else:
            count += 1
            print(f"count incremented: count = {count}")
    
    last_emotion = emotion.data


if __name__ == "__main__":
    # Initialize the node
    rospy.init_node('mapping', log_level=rospy.DEBUG)

    # Setup publisher
    pub = rospy.Publisher('/mapping',UInt8,queue_size=10)

    # Setup subscriber
    sub = rospy.Subscriber('/emotion',String,callback)

    print("mapping node ready")

    rospy.spin()
