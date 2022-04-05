#!/usr/bin/env pybricks-micropython
from ev3dev2.motor import MediumMotor, OUTPUT_D, MoveTank, OUTPUT_A, OUTPUT_B
from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
import math
from time import sleep

#เซตค่าตัวแปร
L = Motor(Port.A)
R = Motor(Port.B)
gyro = GyroSensor(Port.S1)
#Lcolor=ColorSensor(Port.S1)
#Rcolor=ColorSensor(Port.S2)
Mcolor = ColorSensor(Port.S2)
BL_color=ColorSensor(Port.S3)
BR_color=ColorSensor(Port.S4)
M = MediumMotor(OUTPUT_D)
tank_pair = MoveTank(OUTPUT_A, OUTPUT_B)
wheel_diameter = 56
axle_track = 110
robot = DriveBase( L, R,  wheel_diameter, axle_track)

#เซตโหมด
color1.mode = 'COL-COLOR'
color2.mode = 'COL-COLOR'
B1.mode = 'COL-COLOR'
B2.mode = 'COL-COLOR'
gyro.mode = 'GYRO-ANG'

#รีเซตค่า
L.reset_angle(0)
R.reset_angle(0)
gyro.reset_angle(0)

#ฟังก์ชั่น
def start() :
    '''while not any(brick.buttons()):
        wait(10)'''
    while any(brick.buttons()):
        wait(10)
def endstart() :
    L.reset_angle(0)
    R.reset_angle(0)  
    while True :
        color1=BL_color.color()
        color2=BR_color.color()
        robot.drive(-400,0)
        if color1 == 5 or color2 == 5 :
                robot.stop(Stop.BRAKE)
                wait(100)
                L.reset_angle(0)
                R.reset_angle(0)
                break
def push_item() :
    M.on_for_degrees(speed=-100,degrees=100)
    wait(400)
    M.on_for_degrees(speed=100,degrees=100)
    sleep(0.5)
def green() :
    L.reset_angle(0)
    R.reset_angle(0)  
    while True :
        color1=Lcolor.color()
        color2=Rcolor.color()
        robot.drive(-350,0)
        if color1 == 3 or color2 == 3 : 
            robot.stop(Stop.BRAKE)
            wait(500)
            L.reset_angle(0)
            R.reset_angle(0)
            push_item()
            tank_pair.on_for_rotations(left_speed=50,right_speed=50,rotations=1.3);
            break 
def forward() :
    L.reset_angle(0)
    R.reset_angle(0)  
    while True :
        color1=Mcolor.color()
        robot.drive(-300,0)
        if color1 == 1 :
                robot.stop(Stop.BRAKE)
                wait(100)
                L.reset_angle(0)
                R.reset_angle(0)
                break
    robot.drive (150, 0)
    while L.angle()< 80:
        pass
    robot.stop(Stop.BRAKE)
def backward() :
    while True :
        B1=BL_color.color()
        B2=BR_color.color()
        L.run(350)
        R.run(280)
        if B1 == 1 :
            break
    while True :
        B1=BL_color.color()
        B2=BR_color.color()
        L.run(-80)
        R.run(140)
        if B2 == 1 :
            break
    robot.stop(Stop.BRAKE)
def fw() :
    robot.drive(-100,0)
    wait(500)
def bw() :
    robot.drive(100,0)
    wait(500)
def backward_green() :
    while True :
        B1=BL_color.color()
        B2=BR_color.color()
        L.run(350)
        R.run(280)
        if B1 == 3 :
            break
    while True :
        B1=BL_color.color()
        B2=BR_color.color()
        L.run(-80)
        R.run(140)
        if B2 == 3 :
            break
    robot.stop(Stop.BRAKE)
def forward_on_blackhole() :
    L.reset_angle(0)
    R.reset_angle(0)  
    while True :
        color1=Mcolor.color()
        robot.drive(-300,0)
        if color1 == 1 :
                robot.stop(Stop.BRAKE)
                wait(100)
                L.reset_angle(0)
                R.reset_angle(0)
                break
    robot.stop(Stop.BRAKE)
def backward_on_blackhole() :
    L.reset_angle(0)
    R.reset_angle(0)  
    while True :
        color1=BL_color.color()
        color2=BR_color.color()
        robot.drive(300,0)
        if color1 == 1 or color2 == 1 :
                robot.stop(Stop.BRAKE)
                wait(100)
                L.reset_angle(0)
                R.reset_angle(0)
                break
    robot.stop(Stop.BRAKE)
def forward_1block() :
    robot.drive(-600,0)
    wait(1000)
    robot.stop(Stop.BRAKE)
def forward_2block() :
    robot.drive(-600,0)
    wait(2000)
    robot.stop(Stop.BRAKE)
def forward_3block() :
    robot.drive(-600,0)
    wait(3000)
    robot.stop(Stop.BRAKE)
def normal_left() :
    robot.drive_time(0, 100, 500) 
    robot.stop(Stop.BRAKE)
    wait(100)
def normal_right() :
    robot.drive_time(0, -100, 500) 
    robot.stop(Stop.BRAKE)
    wait(100)
def angle_left() :
    L.reset_angle(0)
    R.reset_angle(0)
    L.run(200)
    R.run(0)
    while L.angle()>= 30:
        pass
def angle_right() :
    L.reset_angle(0)
    R.reset_angle(0)
    L.run(0)
    R.run(200)
    while R.angle()>= 30:
        pass
def gyro_left() :
    gyro.reset_angle(0)
    L.run(200)
    R.run(0)
    while gyro.angle()>= -80:
        pass
def gyro_right() :
    gyro.reset_angle(0)
    L.run(0)
    R.run(200)
    while gyro.angle()>= 80:
    #while gyro.value()>= 80:
        pass

#start()
#endstart()