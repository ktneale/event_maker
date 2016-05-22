#!/usr/bin/python

'''Program: Renders a scene producing JPEG snapshots (for use with mjpeg-streamer).
   Author: Kevin Neale
'''

import os
import sys
import getopt
import math
import time

from threading import Thread

import pygame
from pygame.locals import *


#Some basic colours
black = (0,0,0);
white = (255,255,255);
green = (0,255,0);
blue = (0,0,255);
red = (255,0,0);


def screen_capture(threadName, screen):
    count = 0

    eventPath = os.path.abspath(eventName)

    while True:
        count += 1
        filename = eventPath + "/img_" + str(count).zfill(6) + ".jpg"
        pygame.image.save(screen, filename)
        time.sleep(1)       #This is the capture frame rate in our case.


#Handle events so that we can exit early if required..
def event_handler(threadName):
    while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit();
                    os._exit(0);
                if event.type == KEYDOWN and event.key == K_ESCAPE:
                    pygame.quit();
                    os._exit(0);


def reset_screen(screen):
    screen.fill(black)
    font = pygame.font.Font(None, 50)
    title = font.render(eventName,1,red)
    screen.blit(title, (displayInfo.current_w/2 - title.get_rect().width/2, 50))
    pygame.display.update()


def main():

    if len(sys.argv) < 2:
        print("Usage: ./event_maker.py <event_name>");
        print("E.g. ./event_maker.py \"MOTION TEST 1A\"");
        os._exit(0);

    global eventName
    global displayInfo


    #Setup

    eventName = str(sys.argv[1])

    #Sanitise the supplied event name...
    eventName = eventName.replace(' ', '_')

    #The screen captures will be stored in this directory.
    if not os.path.exists(eventName):
        os.makedirs(eventName)

    pygame.init()
    displayInfo = pygame.display.Info()

    screen = pygame.display.set_mode((displayInfo.current_w, displayInfo.current_h), FULLSCREEN)

    eventHandler = Thread(target=event_handler, args=("event-handler",))
    eventHandler.start()

    screenCapture = Thread(target=screen_capture, args=("capture-screen",screen,))



    ##### Event script STARTS HERE!

    reset_screen(screen)

    circ1 = pygame.draw.circle(screen, white, (displayInfo.current_w/2, displayInfo.current_h/2), 100, 0) #filled
    pygame.display.update()

    screenCapture.start() #Start capturing the output

    time.sleep(10)

    reset_screen(screen)

    time.sleep(5)

    circ1 = pygame.draw.circle(screen, red, (displayInfo.current_w/4, displayInfo.current_h/4), 100, 0) #filled
    pygame.display.update()

    time.sleep(10)

    reset_screen(screen)

    time.sleep(3)

    circ1 = pygame.draw.circle(screen, green, (3 * displayInfo.current_w/4, 3 * displayInfo.current_h/4), 50, 0) #filled
    pygame.display.update()

    time.sleep(2)

    reset_screen(screen)
    time.sleep(5)

    ##### Event script ENDS HERE!

    pygame.quit();
    os._exit(0);



#Global vars
displayInfo = 0
eventName = 0

main()
