#!/usr/bin/env python3

import cv2
import label_image

import rospy

from std_msgs.msg import String

if __name__ == "__main__":
    # Initialize the node
    rospy.init_node('emotion', log_level=rospy.DEBUG)

    # Setup publisher
    pub = rospy.Publisher('/emotion',String,queue_size=10)

    command = String()

    

    size = 8

    # We load the xml file
    classifier = cv2.CascadeClassifier()
    load_test = classifier.load('/home/zack/rob421/Pet_Sphero/ws/src/emotion_detection/src/haarcascade_frontalface_alt.xml')
    if load_test:
        print("classifier loaded")
    else:
        print("classifier not loaded")

    webcam = cv2.VideoCapture(0) #Using default WebCam connected to the PC.

    r = rospy.Rate(200)

    print("emotion node ready")
    
    while not rospy.is_shutdown():
        (rval, im) = webcam.read()
        im=cv2.flip(im,1,0) #Flip to act as a mirror

        # Resize the image to speed up detection
        mini = cv2.resize(im, (int(im.shape[1]/size), int(im.shape[0]/size)))

        # detect MultiScale / faces 
        faces = classifier.detectMultiScale(mini)

        # Draw rectangles around each face
        for f in faces:
            (x, y, w, h) = [v * size for v in f] #Scale the shapesize backup
            cv2.rectangle(im, (x,y), (x+w,y+h), (0,255,0), 4)
        
            #Save just the rectangle faces in SubRecFaces
            sub_face = im[y:y+h, x:x+w]

            FaceFileName = "/home/zack/rob421/Pet_Sphero/ws/src/emotion_detection/src/test.jpg" #Saving the current image from the webcam for testing.
            cv2.imwrite(FaceFileName, sub_face)
        
            text = label_image.main(FaceFileName)# Getting the Result from the label_image file, i.e., Classification Result.
            text = text.title()# Title Case looks Stunning.
            font = cv2.FONT_HERSHEY_TRIPLEX
            cv2.putText(im, text,(x+w,y), font, 1, (0,0,255), 2)

            command.data = text
            pub.publish(command)

        # Show the image
        cv2.imshow('Capture',   im)
        key = cv2.waitKey(3)

        # Sleep to allow other ROS nodes to run
        r.sleep()
