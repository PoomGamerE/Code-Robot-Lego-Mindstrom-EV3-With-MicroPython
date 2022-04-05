#!/usr/bin/env pybricks-micropython
from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
import math
from time import sleep
from ev3dev2.motor import MoveTank, OUTPUT_A ,OUTPUT_B,OUTPUT_D,MediumMotor
color_NL=ColorSensor(Port.S1)
color_NR=ColorSensor(Port.S2)
color_LL=ColorSensor(Port.S3)
color_LR=ColorSensor(Port.S4)
si1 = color_NL.color()
si2 = color_NR.color()
si3 = color_LL.color()
si4 = color_LR.color()
wheel_diameter = 54
axle_track = 141
Lmotor = Motor(Port.A)
Rmotor = Motor(Port.B)
#Smotor = Motor(Port.C)
S_motor = MediumMotor(OUTPUT_D)
# 1 == black
# 3 == green

robot = DriveBase(Lmotor , Rmotor, wheel_diameter, axle_track)
tankpair = MoveTank(OUTPUT_A,OUTPUT_B)
def tank_Move(m):
        tankpair.on_for_rotations(left_speed = m,right_speed = m, rotations = 0.55)
       # tankpair.on_for_rotations(left_speed = -20,right_speed = -20, rotations = 1.55)
        tankpair.stop()
        wait(100)
def nah2():
    while True:
        si1 = color_NL.color()
        si2 = color_NR.color()
        si3 = color_LL.color()
        si4 = color_LR.color()
        if si1 == 1 or si2 == 1:
                robot.drive_time(100,0,200)
                wait(100)
                robot.stop(Stop.BRAKE)
                break
        elif si2 == 1 and si1 != 1:
            Lmotor.run(-200)
            Rmotor.run(50)
        elif si1 == 1 and si2 != 1:
            Lmotor.run(50)
            Rmotor.run(-200)
        else :
         robot.drive(-200,0)
def nah4():
    tank_Move
    angle_M(1556)
    while True:
        si1 = color_NL.color()
        si2 = color_NR.color()
        si3 = color_LL.color()
        si4 = color_LR.color()
        if si1 == 1 or si2 == 1:
            robot.drive_time(100,0,200)
            wait(100)
            robot.stop(Stop.BRAKE)
            break
        elif si2 == 1 and si1 != 1:
            Lmotor.run(-200)
            Rmotor.run(0)
        elif si1 == 1 and si2 != 1:
            Lmotor.run(0)
            Rmotor.run(-200)
        else :
             robot.drive(-200,0)
def nahR():
    tank_Move
    angle_M(1636)
    while True:
        si1 = color_NL.color()
        si2 = color_NR.color()
        si3 = color_LL.color()
        si4 = color_LR.color()
        if si1 == 5 or si2 == 5:
                robot.drive_time(200,0,550)
                wait(100)
                robot.stop(Stop.BRAKE)
                break
        elif si2 == 1 and si1 != 1:
            Lmotor.run(-250)
            Rmotor.run(-100)
        elif si1 == 1 and si2 != 1:
            Lmotor.run(-100)
            Rmotor.run(-250)
        else :
             robot.drive(-200,0)
def nah3():
        angle_M(1300)
        while True:
                si1 = color_NL.color()
                si2 = color_NR.color()
                si3 = color_LL.color()
                si4 = color_LR.color()
                if si1 == 1 or si2 == 1:
                        robot.drive_time(100,0,200)
                        wait(100)
                        robot.stop(Stop.BRAKE)
                        wait(200)
                        break
                elif si2 == 1 and si1 != 1:
                        Lmotor.run(-100)
                        Rmotor.run(0)
                elif si1 == 1 and si2 != 1:
                        Lmotor.run(0)
                        Rmotor.run(-100)
                else :
                 robot.drive(-200,0)
def toyL():
        
        robot.stop() 
        wait(100)       
        robot.drive_time(0,90,1000)
        wait(100)
        Lmotor.run(0)
        Rmotor.run(0)
        sleep(1)
        while True:
                si1 = color_NL.color()
                si2 = color_NR.color()
                si3 = color_LL.color()
                si4 = color_LR.color()
                if si3 == 1 and si4 == 1:
                        robot.stop(Stop.BRAKE)
                        wait(200)
                        break
                elif si4 == 1 and si3 != 1:
                        Lmotor.run(0)
                        Rmotor.run(-200)
                        sleep(0.1)
                elif si3 == 1 and si4 != 1:
                        Lmotor.run(-200)
                        Rmotor.run(0)
                        sleep(0.1)
                else :
                 robot.drive(100,0)
def toyR():
        robot.drive_time(150,0,450)
        wait(100)       
        robot.drive_time(0,-90,1000)
        wait(100)
        Lmotor.run(0)
        Rmotor.run(0)
        while True:
                si1 = color_NL.color()
                si2 = color_NR.color()
                si3 = color_LL.color()
                si4 = color_LR.color()
                if si3 == 1 and si4 == 1:
                        robot.stop(Stop.BRAKE)
                        wait(200)
                        break
                elif si4 != 1 and si3 == 1:
                        Rmotor.run(0)
                        Lmotor.run(-150)
                elif si3 != 1 and si4 == 1:
                        Rmotor.run(-150)
                        Lmotor.run(0)
                else :
                        robot.drive(100,0)
def toyQ():
        robot.stop()
        wait(100)       
        robot.drive_time(0,-90,1000)
        wait(100)
        Lmotor.run(0)
        Rmotor.run(0)
        while True:
                si1 = color_NL.color()
                si2 = color_NR.color()
                si3 = color_LL.color()
                si4 = color_LR.color()
                if si3 == 1 and si4 == 1:
                        robot.stop(Stop.BRAKE)
                        wait(200)
                        break
                elif si4 != 1 and si3 == 1:
                        Rmotor.run(0)
                        Lmotor.run(-150)
                        sleep(0.08)
                elif si3 != 1 and si4 == 1:
                        Rmotor.run(-150)
                        Lmotor.run(0)
                        sleep(0.08)
                else :
                        robot.drive(100,0)
def toyR2():

        robot.drive_time(150,0,250)
        wait(100)       
        robot.drive_time(0,-90,1000)
        wait(100)
        Lmotor.run(0)
        Rmotor.run(0)
        while True:
                si1 = color_NL.color()
                si2 = color_NR.color()
                si3 = color_LL.color()
                si4 = color_LR.color()
                if si3 == 1 and si4 == 1:
                        robot.stop(Stop.BRAKE)
                        wait(200)
                        break
                elif si4 != 1 and si3 == 1:
                        Rmotor.run(0)
                        Lmotor.run(-100)
                        sleep(0.08)
                elif si3 != 1 and si4 == 1:
                        Rmotor.run(-100)
                        Lmotor.run(0)
                        sleep(0.08)
                else :
                        robot.drive(100,0)
def toyR3():
        robot.drive_time(100,0,200)
        wait(100)       
        robot.drive_time(0,-90,1000)
        wait(100)
        Lmotor.run(0)
        Rmotor.run(0)
        while True:
                si1 = color_NL.color()
                si2 = color_NR.color()
                si3 = color_LL.color()
                si4 = color_LR.color()
                if si3 == 1 and si4 == 1:
                        robot.stop(Stop.BRAKE)
                        wait(200)
                        break
                elif si4 != 1 and si3 == 1:
                        Rmotor.run(0)
                        Lmotor.run(-200)
                        sleep(0.1)
                elif si3 != 1 and si4 == 1:
                        Rmotor.run(-200)
                        Lmotor.run(0)
                        sleep(0.1)
                else :
                        robot.drive(100,0)
def toyRN():
        while True:
                si1 = color_NL.color()
                si2 = color_NR.color()
                si3 = color_LL.color()
                si4 = color_LR.color()
                if si3 == 1 and si4 == 1:
                        robot.stop()
                        wait(100)
                        robot.drive_time(-200,0,300)
                        wait(100)
                        sleep(0.1)
                        robot.drive_time(0,-100,1000)
                        wait(100)
                        robot.stop(Stop.BRAKE)
                        wait(200)
                        break
                elif si4 != 1 and si3 == 1:
                        Rmotor.run(0)
                        Lmotor.run(-150)
                        sleep(0.1)
                elif si3 != 1 and si4 == 1:
                        Rmotor.run(-150)
                        Lmotor.run(0)
                        sleep(0.1)
                else :
                        robot.drive(100,0)
def sr():
    while True:
        si1 = color_NL.color()
        si2 = color_NR.color()
        si3 = color_LL.color()
        si4 = color_LR.color()
        Lmotor.run(-250)
        Rmotor.run(250)
        if si2 == 1:
            robot.stop()
            break
def sl():
        robot.stop()
        wait(100)       
        robot.drive_time(0,92,1100)
        wait(100)
        Lmotor.run(0)
        Rmotor.run(0)
def angle_M(A):      
        Lmotor.reset_angle(0)
        Rmotor.reset_angle(0)
        while Lmotor.angle()>-A and Rmotor.angle()>-A :
                robot.drive(-220,0)
                si1 = color_NL.color()
                si2 = color_NR.color()
                si3 = color_LL.color()
                si4 = color_LR.color()
                if si2 == 1 :
                        Rmotor.run(-550)
                        Lmotor.run(-200)
                elif si1 == 1 :
                        Lmotor.run(-550)
                        Rmotor.run(-200)
        robot.stop()
def angle_MB(A):      
        Lmotor.reset_angle(0)
        Rmotor.reset_angle(0)
        while Lmotor.angle()<A and Rmotor.angle()<A :
                robot.drive(200,0)
                si1 = color_NL.color()
                si2 = color_NR.color()
                si3 = color_LL.color()
                si4 = color_LR.color()
                if si4 == 1 :
                        Rmotor.run(550)
                        Lmotor.run(200)
                elif si3 == 1 :
                        Lmotor.run(550)
                        Rmotor.run(200)


        robot.stop()
def bh():
        while True:
                si1 = color_NL.color()
                si2 = color_NR.color()
                si3 = color_LL.color()
                si4 = color_LR.color()
                robot.drive(-200,0)
                if si3 != 1 or si4 != 1:
                        break
                else :
                 robot.drive(-850,0)
        '''while True:
                si1 = color_NL.color()
                si2 = color_NR.color()
                si3 = color_LL.color()
                si4 = color_LR.color()
                robot.drive(-200,0)
                if si3 != 1 or si4 != 1:
                        robot.stop(Stop.BRAKE)
                        break
                else :
                 robot.drive(-800,0)'''
def chekN(): 
        while True :
                si1 = color_NL.color()
                si2 = color_NR.color()
                si3 = color_LL.color()
                si4 = color_LR.color()
                if si1 == 1 and si2 == 1:
                        robot.drive_time(100,0,200)
                        wait(100)
                        robot.stop(Stop.BRAKE)
                        wait(200)
                        break
                elif si2 != 1 and si1 == 1:
                        Rmotor.run(0)
                        Lmotor.run(230)
                        sleep(0.05)
                elif si1 != 1 and si2 == 1:
                        Rmotor.run(230)
                        Lmotor.run(0)
                        sleep(0.05)
                else :
                        robot.drive(-150,0)
def chekB():
        while True:
                si1 = color_NL.color()
                si2 = color_NR.color()
                si3 = color_LL.color()
                si4 = color_LR.color()
                if si3 == 1 and si4 == 1:
                        robot.stop(Stop.BRAKE)
                        wait(200)
                        break
                elif si4 != 1 and si3 == 1:
                        Rmotor.run(0)
                        Lmotor.run(-100)
                        sleep(0.08)
                elif si3 != 1 and si4 == 1:
                        Rmotor.run(-100)
                        Lmotor.run(0)
                        sleep(0.08)
                else :
                        robot.drive(100,0)
def chek2(): 
        sleep(0.5)  
        robot.drive_time(0,-90,1000)
        wait(100)
        while True :
                si1 = color_NL.color()
                si2 = color_NR.color()
                si3 = color_LL.color()
                si4 = color_LR.color()
                if si1 == 1 and si2 == 1:
                        robot.stop(Stop.BRAKE)
                        wait(200)
                        break
                elif si2 != 1 and si1 == 1:
                        Rmotor.run(0)
                        Lmotor.run(200)
                        sleep(0.05)
                elif si1 != 1 and si2 == 1:
                        Rmotor.run(200)
                        Lmotor.run(0)
                        sleep(0.05)
                else :
                        robot.drive(-100,0)
def press():
        angle_M(550)
        while True :
                si1 = color_NL.color()
                si2 = color_NR.color()
                si3 = color_LL.color()
                si4 = color_LR.color()
                if si1 == 3 or si2 == 3 :
                        robot.stop()
                        sleep(0.5)
                        S_motor.on_for_degrees(speed=80,degrees=850)
                        wait(100)
                        S_motor.on_for_degrees(speed=-100,degrees=700)
                        wait(600)
                        angle_MB(100)
                        robot.stop()
                        break
                else:
                        robot.drive(-100,0)
def ar():
        robot.stop()
        wait(100)
        robot.drive_time(0,-90,1000)
        wait(100)
        robot.stop()
        wait(100)
        robot.drive_time(0,-90,1000)
        wait(100)
        Lmotor.run(0)
        Rmotor.run(0)
def AS():
        Lmotor.run(500)
        Rmotor.run(-500)
        wait(500)
        Lmotor.run(0)
        Rmotor.run(0)
        sleep(1) 
def ssr():
        robot.stop()
        wait(100)       
        robot.drive_time(0,-92.5,1100)
        wait(100)
        Lmotor.run(0)
        Rmotor.run(0)


brick.sound.beep()
wait(150)
S_motor.on_for_degrees(speed=-50,degrees=500)
'''nah4()
toyR()
nah3()
toyR2()
nah2()
toyR2()
nah2()
robot.drive_time(100,0,250)
wait(100)
toyL() 
angle_M(350)
press()
sleep(0.1)
angle_MB(320)
toyL()
nah2()
robot.drive_time(0,-5,650)'''
robot.drive_time(-800,0,1600)
nah3()
robot.drive_time(100,0,250)
wait(100)
chek2()
toyR3()
press()
toyRN()
sleep(0.5)
angle_M(1230)
toyQ()
nah3()
robot.drive(200,0)
wait(250)
sl()
press()
ar()
angle_M(700)
press()
angle_MB(845)
ssr()
chekB()
sleep(0.1)
chekN()
sleep(0.1)
sl()
sleep(0.1)
angle_M(460)
sleep(0.1)
ssr()
nah3()
robot.drive_time(-500,0,1000)
chekN()
robot.drive_time(500,0,100)
ssr()
nah2()
chekN()
toyR3()
nah2()
toyL()
nah2()
toyL()
nah3()
toyL()
nahR()