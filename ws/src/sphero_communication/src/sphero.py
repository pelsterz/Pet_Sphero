#!/usr/bin/env python3

import rospy

from std_msgs.msg import UInt8

import sys
from time import sleep

import itertools

from pysphero.core import Sphero
from pysphero.driving import Direction
from pysphero.device_api.user_io import Color
from pysphero.device_api.user_io import Pixel

global mac_address

def nothing():
    return "action not recognized"

def mild_bump():
    speed = 75
    heading = 0
    with Sphero(mac_address=mac_address) as sphero:
        sleep(2)
        print(f"Bump with speed {speed} and heading {heading}")

        for i in range(2):
            sphero.driving.drive_with_heading(speed, heading, Direction.forward)
            sleep(0.4)
            sphero.driving.drive_with_heading(0, heading, Direction.forward)
            sleep(1)
            sphero.driving.drive_with_heading(speed, heading, Direction.reverse)
            sleep(0.3)
            sphero.driving.drive_with_heading(0, heading, Direction.forward)
            sleep(1)
    return "mild bump performed"

def quick_bump():
    speed = 100
    heading = 0
    with Sphero(mac_address=mac_address) as sphero:
        sleep(2)
        print(f"Bump with speed {speed} and heading {heading}")

        for i in range(2):
            sphero.driving.drive_with_heading(speed, heading, Direction.forward)
            sleep(0.25)
            sphero.driving.drive_with_heading(0, heading, Direction.forward)
            sleep(0.75)
            sphero.driving.drive_with_heading(speed, heading, Direction.reverse)
            sleep(0.15)
            sphero.driving.drive_with_heading(0, heading, Direction.forward)
            sleep(0.75)
    return "quick bump performed"

def calm_bump():
    speed = 50
    heading = 0
    with Sphero(mac_address=mac_address) as sphero:
        sleep(2)
        print(f"Bump with speed {speed} and heading {heading}")

        for i in range(2):
            sphero.driving.drive_with_heading(speed, heading, Direction.forward)
            sleep(0.75)
            sphero.driving.drive_with_heading(0, heading, Direction.forward)
            sleep(1.25)
            sphero.driving.drive_with_heading(speed, heading, Direction.reverse)
            sleep(0.65)
            sphero.driving.drive_with_heading(0, heading, Direction.forward)
            sleep(1.25)
    return "calm bump performed"

def energetic_bump_spin():
    speed = 125
    heading = 0
    with Sphero(mac_address=mac_address) as sphero:
        sleep(2)
        print(f"Bump with speed {speed} and heading {heading}")

        for i in range(2):
            sphero.driving.drive_with_heading(speed, heading, Direction.forward)
            sleep(0.20)
            sphero.driving.drive_with_heading(0, heading, Direction.forward)
            sleep(0.65)
            sphero.driving.drive_with_heading(speed, heading, Direction.reverse)
            sleep(0.10)
            sphero.driving.drive_with_heading(0, heading, Direction.forward)
            sleep(0.65)
    return "energetic bump and spin performed"

def eyes():
    with Sphero(mac_address=mac_address) as sphero:
        sleep(2)
        print("Show eyes in matrix")
        pixels = [
                # Left Eye
                Pixel(x=0,y=1),
                Pixel(x=0,y=2),
                Pixel(x=0,y=3),
                Pixel(x=1,y=1),
                Pixel(x=1,y=2),
                Pixel(x=1,y=3),
                Pixel(x=2,y=1),
                Pixel(x=2,y=2),
                Pixel(x=2,y=3),
                # Right Eye
                Pixel(x=5,y=1),
                Pixel(x=5,y=2),
                Pixel(x=5,y=3),
                Pixel(x=6,y=1),
                Pixel(x=6,y=2),
                Pixel(x=6,y=3),
                Pixel(x=7,y=1),
                Pixel(x=7,y=2),
                Pixel(x=7,y=3)
        ]
        colors = [
                # Left Eye
                Color(red=0xff,green=0xff,blue=0xff),
                Color(red=0xff,green=0xff,blue=0xff),
                Color(red=0xff,green=0xff,blue=0xff),
                Color(red=0xff,green=0xff,blue=0xff),
                Color(blue=0xff),
                Color(red=0xff,green=0xff,blue=0xff),
                Color(red=0xff,green=0xff,blue=0xff),
                Color(red=0xff,green=0xff,blue=0xff),
                Color(red=0xff,green=0xff,blue=0xff),
                # Right Eye
                Color(red=0xff,green=0xff,blue=0xff),
                Color(red=0xff,green=0xff,blue=0xff),
                Color(red=0xff,green=0xff,blue=0xff),
                Color(red=0xff,green=0xff,blue=0xff),
                Color(blue=0xff),
                Color(red=0xff,green=0xff,blue=0xff),
                Color(red=0xff,green=0xff,blue=0xff),
                Color(red=0xff,green=0xff,blue=0xff),
                Color(red=0xff,green=0xff,blue=0xff)
        ]
        for (pixel, color) in zip(pixels, colors):
            sphero.user_io.set_led_matrix_pixel(pixel,color)

def look_left():
    with Sphero(mac_address=mac_address) as sphero:
        sleep(2)
        print("Look left")
        pixels = [
                # Left Eye
                Pixel(x=1,y=2),
                Pixel(x=2,y=2),
                # Right Eye
                Pixel(x=6,y=2),
                Pixel(x=7,y=2)
        ]
        colors = [
                # Left Eye
                Color(red=0xff,green=0xff,blue=0xff),
                Color(blue=0xff),
                # Right Eye
                Color(red=0xff,green=0xff,blue=0xff),
                Color(blue=0xff)
        ]
        for (pixel, color) in zip(pixels, colors):
            sphero.user_io.set_led_matrix_pixel(pixel,color)

def look_right():
    with Sphero(mac_address=mac_address) as sphero:
        sleep(2)
        print("Look right")
        pixels = [
                # Left Eye
                Pixel(x=1,y=2),
                Pixel(x=0,y=2),
                # Right Eye
                Pixel(x=6,y=2),
                Pixel(x=5,y=2)
        ]
        colors = [
                # Left Eye
                Color(red=0xff,green=0xff,blue=0xff),
                Color(blue=0xff),
                # Right Eye
                Color(red=0xff,green=0xff,blue=0xff),
                Color(blue=0xff)
        ]
        for (pixel, color) in zip(pixels, colors):
            sphero.user_io.set_led_matrix_pixel(pixel,color)

def sad_eyes():
    eyes()
    look_left()
    return "sad eyes performed"

def flashing_eyes():
    eyes()
    look_left()
    return "flashing eyes performed"

def happy_eyes():
    eyes()
    look_left()
    return "happy eyes performed"

def sphero_wake():
    with Sphero(mac_address=mac_address) as sphero:
        sphero.power.wake()

def sphero_sleep():
    with Sphero(mac_address=mac_address) as sphero:
        sphero.power.enter_soft_sleep()

def map_to_action(map_action):
    switcher = {
        0: mild_bump, # Anger
        1: quick_bump, # Disgust 
        2: calm_bump, # Fear
        3: energetic_bump_spin, # Neutral & Sad
    }
    func = switcher.get(map_action, nothing)
    return func()

def map_to_message(map_message):
    switcher = {
        0: sad_eyes, # Anger & Fear
        1: flashing_eyes, # Disgust 
        2: happy_eyes, # Neutral & Sad
    }
    func = switcher.get(map_message, nothing)
    return func()

def callback(emotion):
    sphero_wake()
    print("performing action")
    print(map_to_action(emotion.data))
    print("performing message")
    print(map_to_message(emotion.data))
    print("finished performing")
    sphero_sleep()


if __name__ == "__main__":
    # Initilize the node
    rospy.init_node('sphero', log_level=rospy.DEBUG)

    name = rospy.get_name()
    # Get address from parameters
    try:
        mac_address = rospy.get_param('%s/address'%name)
    except KeyError:
        print("Address not provided")
        sys.exit()
    
    # Setup subscriber
    sub = rospy.Subscriber('/mapping',UInt8,callback)

    print("sphero setup")
    
    # Turn control over to ROS
    rospy.spin()
