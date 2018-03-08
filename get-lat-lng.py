#!/usr/bin/python
import os
import pygame, sys
from pygame.locals import *
import serial

#initialise serial port on /ttyUSB0
ser = serial.Serial('/dev/ttyS0',9600,timeout = None)
# set font size MAX 100
fontsize = 50
