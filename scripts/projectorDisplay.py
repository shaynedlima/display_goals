#!/usr/bin/env python
import rospy
import time
from visualization_msgs.msg import MarkerArray
import pygame




def callback(data):
    redGoal = data.markers[0].pose.position
    blueGoal = data.markers[1].pose.position

    print redGoal
    print blueGoal

    #red.x = -0.3, red.y = 0.45
    #blue.x = -0.3, blue.y = -0.45



    for event in pygame.event.get():
        if(event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_ESCAPE):
                pygame.quit()
                return
        else:
            gameDisplay.fill((0,0,0))
            #pygame.draw.circle(gameDisplay, (255, 0, 0), (int(round(random.random()*displayWidth)), int(round(random.random()*displayHeight))), 200)
            #pygame.draw.circle(gameDisplay, (0, 0, 255), (int(round(random.random()*displayWidth)), int(round(random.random()*displayHeight))), 200)
            
            pygame.draw.circle(gameDisplay, (255, 0, 0), (int((redGoal.y+1)/2*displayWidth), int(abs(redGoal.x)*displayHeight)), 200)
            pygame.draw.circle(gameDisplay, (0, 0, 255), (int((blueGoal.y+1)/2*displayWidth), int(abs(blueGoal.x)*displayHeight)), 200)
            pygame.display.update()


    
def listener():
    rospy.init_node('projectorDisplay', anonymous=True)
    rospy.Subscriber("scan_objects/goal_markers", MarkerArray, callback)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    pygame.init()
    screenInfo = pygame.display.Info()
    displayWidth = screenInfo.current_w 
    displayHeight = screenInfo.current_h
    gameDisplay = pygame.display.set_mode((displayWidth, displayHeight), pygame.FULLSCREEN)
    pygame.display.set_caption('Goal Regions')
    print displayWidth
    print displayHeight

    listener()





