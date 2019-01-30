#!/usr/bin/env python
import rospy
import time
from visualization_msgs.msg import MarkerArray
from Tkinter import *



initialise = 1

def drawCircle(canvas,x0,y0,r, colour):
   id = canvas.create_oval(x0-r,y0-r,x0+r,y0+r, fill=colour)
   return id



def callback(data):
    redGoal = data.markers[0].pose.position
    blueGoal = data.markers[1].pose.position
    global initialise
    displayWidth = 1900
    displayHeight = 1640
    goalRad = 30

    print initialise

    print redGoal
    print blueGoal


    displayBlue = [(blueGoal.y+1)/2*displayWidth, abs(blueGoal.x)*displayHeight]
    displayRed = [(redGoal.y+1)/2*displayWidth, abs(redGoal.x)*displayHeight]
        

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






