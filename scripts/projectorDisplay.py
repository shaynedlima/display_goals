#!/usr/bin/env python
import rospy
import time
from visualization_msgs.msg import MarkerArray
from Tkinter import *
import numpy as np
import math

initialise = 1
red_goal_col = "#77efcd"
blue_goal_col = "#32aff2"

def rotateClockwise(xy, degrees):
    # Rotate point around origin
    x = xy[0]
    y = xy[1]
    xx = x * math.cos(degrees*math.pi/180) - y * math.sin(degrees*math.pi/180)
    yy = x * math.sin(degrees*math.pi/180) + y * math.cos(degrees*math.pi/180)
    return xx, yy

def drawCircle(canvas, x0, y0, r, colour):
   id = canvas.create_oval(x0-r,y0-r,x0+r,y0+r, fill=colour)
   return id



def callback(data):
    redGoal = data.markers[0].pose.position
    blueGoal = data.markers[1].pose.position
    global initialise
    #displayWidth = 1920
    #displayHeight = 1080


    redRad = data.markers[0].scale.x/2
    blueRad = data.markers[1].scale.x/2

    # Size of projection (region window appears in)
    widthProjected = 1.2
    heightProjected = 0.68
    # Scaling: 1 m = 1545.673077 pixels
    scale = 1545.673077 # pixels/m

    displayWidth = round(widthProjected*scale)
    displayHeight = round(heightProjected*scale)


    # 1m = 1545.673077 pixels



    print initialise


    #print blueGoal
    # Rotating coordinates
    temp = redGoal.y
    redGoal.y = redGoal.x
    redGoal.x = temp

    temp = blueGoal.y
    blueGoal.y = blueGoal.x
    blueGoal.x = temp

    # Translating point to top left of window
    redGoal.x = redGoal.x + 0.465
    redGoal.y = redGoal.y + 0.85

    blueGoal.x = blueGoal.x + 0.465
    blueGoal.y = blueGoal.y + 0.85
    print redGoal

    # Rotating point 0.76 degrees due to angle of projection
    blueGoal.x, blueGoal.y = rotateClockwise([blueGoal.x, blueGoal.y], 0.76)
    redGoal.x, redGoal.y = rotateClockwise([redGoal.x, redGoal.y], 0.76)


    # x: -0.17 to -0.85 -->  0 to displayHeight
    # y: -0.75 to 0.4 -->  0 to displayWidth

    #displayBlue = [(blueGoal.y+1)/2*displayWidth, (abs(blueGoal.x) - 0.17)/0.68*displayHeight]
    #displayRed = [(redGoal.y+1)/2*displayWidth, (abs(redGoal.x) - 0.17)/0.68*displayHeight]
    #displayBlue = [(blueGoal.y+0.4)/1.15*displayWidth,(0.68-(abs(blueGoal.x)-0.17))/0.68*displayHeight]
    #displayRed = [(redGoal.y+0.4)/1.15*displayWidth,(0.68-(abs(redGoal.x)-0.17))/0.68*displayHeight]
    displayBlue = [blueGoal.x/widthProjected*displayWidth, blueGoal.y/heightProjected*displayHeight]
    displayRed = [redGoal.x/widthProjected*displayWidth, redGoal.y/heightProjected*displayHeight]


    print displayBlue
    print displayRed

    if(initialise):
    	global top, canvas, red, blue
    	top = Tk()
    	canvas = Canvas(top, width=displayWidth, height=displayHeight, bg='black')
    	canvas.pack(expand=YES, fill=BOTH)
        # Position screen to show up on projector
        top.geometry('%dx%d+%d+%d' % (displayWidth, displayHeight, displayWidth, 0))
        redRadius = redRad*scale
        blueRadius = blueRad*scale
    	blue = canvas.create_oval(displayBlue[0]-blueRadius,displayBlue[1]-blueRadius,displayBlue[0]+blueRadius,displayBlue[1]+blueRadius, fill=blue_goal_col)
    	#blue = drawCircle(canvas, displayBlue[0], displayBlue[1], 30, "blue")
    	#red = drawCircle(canvas, displayRed[0], displayRed[1] , 30, "red")
    	red = canvas.create_oval(displayRed[0]-redRadius,displayRed[1]-redRadius,displayRed[0]+redRadius,displayRed[1]+redRadius, fill=red_goal_col)
    	top.update_idletasks()
    	top.update()
    	initialise = 0
    else:
        redRadius = redRad*scale
        blueRadius = blueRad*scale
    	canvas.coords(red, displayRed[0]-redRadius,displayRed[1]-redRadius,displayRed[0]+redRadius,displayRed[1]+redRadius)
    	canvas.coords(blue, displayBlue[0]-blueRadius,displayBlue[1]-blueRadius,displayBlue[0]+blueRadius,displayBlue[1]+blueRadius)
    	top.update_idletasks()
    	top.update()





def listener():
	rospy.init_node('projectorDisplay', anonymous=True)
	rospy.Subscriber("scan_objects/goal_markers", MarkerArray, callback)
	rospy.spin()

if __name__ == '__main__':
	listener()
