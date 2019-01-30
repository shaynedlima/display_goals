#!/usr/bin/env python
import rospy
import time
from visualization_msgs.msg import MarkerArray
from Tkinter import *
import numpy as np


initialise = 1

def drawCircle(canvas,x0,y0,r, colour):
   id = canvas.create_oval(x0-r,y0-r,x0+r,y0+r, fill=colour)
   return id



def callback(data):
    redGoal = data.markers[0].pose.position
    blueGoal = data.markers[1].pose.position
    global initialise
    displayWidth = 1920
    displayHeight = 1080
    goalRad = 130

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
    redGoal.x = redGoal.x + 0.4
    redGoal.y = redGoal.y + 0.85

    blueGoal.x = blueGoal.x + 0.4
    blueGoal.y = blueGoal.y + 0.85
    print redGoal
    # x: -0.17 to -0.85 -->  0 to displayHeight
    # y: -0.75 to 0.4 -->  0 to displayWidth

    #displayBlue = [(blueGoal.y+1)/2*displayWidth, (abs(blueGoal.x) - 0.17)/0.68*displayHeight]
    #displayRed = [(redGoal.y+1)/2*displayWidth, (abs(redGoal.x) - 0.17)/0.68*displayHeight]
    #displayBlue = [(blueGoal.y+0.4)/1.15*displayWidth,(0.68-(abs(blueGoal.x)-0.17))/0.68*displayHeight]
    #displayRed = [(redGoal.y+0.4)/1.15*displayWidth,(0.68-(abs(redGoal.x)-0.17))/0.68*displayHeight]
    displayBlue = [blueGoal.x/1.15*displayWidth, blueGoal.y/0.68*displayHeight]
    displayRed = [redGoal.x/1.15*displayWidth, redGoal.y/0.68*displayHeight]


    print displayBlue
    print displayRed

    if(initialise):
    	global top, canvas, red, blue
    	top = Tk()
    	canvas = Canvas(top, width=displayWidth, height=displayHeight, bg='black')
    	canvas.pack(expand=YES, fill=BOTH)
    	blue = canvas.create_oval(displayBlue[0]-goalRad,displayBlue[1]-goalRad,displayBlue[0]+goalRad,displayBlue[1]+goalRad, fill="blue")
    	#blue = drawCircle(canvas, displayBlue[0], displayBlue[1], 30, "blue")
    	#red = drawCircle(canvas, displayRed[0], displayRed[1] , 30, "red")
    	red = canvas.create_oval(displayRed[0]-goalRad,displayRed[1]-goalRad,displayRed[0]+goalRad,displayRed[1]+goalRad, fill="red")
    	top.update_idletasks()
    	top.update()
    	initialise = 0
    else:
    	canvas.coords(red, displayRed[0]-goalRad,displayRed[1]-goalRad,displayRed[0]+goalRad,displayRed[1]+goalRad)
    	canvas.coords(blue, displayBlue[0]-goalRad,displayBlue[1]-goalRad,displayBlue[0]+goalRad,displayBlue[1]+goalRad)
    	top.update_idletasks()
    	top.update()

    #red.x = -0.3, red.y = 0.45
    #blue.x = -0.3, blue.y = -0.45

    #gameDisplay.fill((0,0,0))
    #pygame.draw.circle(gameDisplay, (255, 0, 0), (int(round(random.random()*displayWidth)), int(round(random.random()*displayHeight))), 200)
    #pygame.draw.circle(gameDisplay, (0, 0, 255), (int(round(random.random()*displayWidth)), int(round(random.random()*displayHeight))), 200)
    #pygame.draw.circle(gameDisplay, (255, 0, 0), (int((redGoal.y+1)/2*displayWidth), int(abs(redGoal.x)*displayHeight)), 200)
    #pygame.draw.circle(gameDisplay, (0, 0, 255), (int((blueGoal.y+1)/2*displayWidth), int(abs(blueGoal.x)*displayHeight)), 200)
    #pygame.display.update()





def listener():

	rospy.init_node('projectorDisplay', anonymous=True)
	rospy.Subscriber("scan_objects/goal_markers", MarkerArray, callback)

	rospy.spin()

if __name__ == '__main__':

	listener()
