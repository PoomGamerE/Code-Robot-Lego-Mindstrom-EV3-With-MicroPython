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
L = Motor(Port.A)
R = Motor(Port.B)
color_1P=ColorSensor(Port.S1)
color_2P=ColorSensor(Port.S2)
color_B1P=ColorSensor(Port.S3)
color_B2P=ColorSensor(Port.S4)
B1=color_B1P.color()
B2=color_B2P.color()
M_motor=MediumMotor(OUTPUT_D)
tank_pair = MoveTank(OUTPUT_A, OUTPUT_B)
wheel_diameter = 56
axle_track = 110
robot = DriveBase( L, R,  wheel_diameter, axle_track)

brick.sound.beep()
wait(150)
brick.sound.beep()
wait(150)


def takeb() :
    robot.drive(500,0)
    wait(2000)
def forward_on_blackhole() :
    L.reset_angle(0)
    R.reset_angle(0)  
    while True :
        color1=color_1P.color()
        color2=color_2P.color()
        robot.drive(-300,0)
        if color1 == 1 or color2 == 1 :
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
        color1=color_B1P.color()
        color2=color_B2P.color()
        robot.drive(300,0)
        if color1 == 1 or color2 == 1 :
                robot.stop(Stop.BRAKE)
                wait(100)
                L.reset_angle(0)
                R.reset_angle(0)
                break
    robot.stop(Stop.BRAKE)
def forward_wow() :
    L.reset_angle(0)
    R.reset_angle(0)  
    while True :
        color1=color_B1P.color()
        color2=color_B2P.color()
        robot.drive(-300,0)
        if color1 == 1 or color2 == 1 :
                robot.stop(Stop.BRAKE)
                wait(100)
                L.reset_angle(0)
                R.reset_angle(0)
                break
        '''if color1 != 1 and color2 == 1 :
                robot.drive_time(0, -50, 300) 
                robot.drive (500, 0)
                wait(500)
                forward()
                break 
        if color1 == 1 and color2 != 1 :
                robot.drive_time(0, 50, 300)
                robot.drive (500, 0)
                wait(500)
                forward()
                break'''
    robot.drive (-150, 0)
    while L.angle()< -80:
        pass
    robot.stop(Stop.BRAKE)
def forward() :
    L.reset_angle(0)
    R.reset_angle(0)  
    while True :
        color1=color_1P.color()
        color2=color_2P.color()
        robot.drive(-300,0)
        if color1 == 1 or color2 == 1 :
                robot.stop(Stop.BRAKE)
                wait(100)
                L.reset_angle(0)
                R.reset_angle(0)
                break
        '''if color1 != 1 and color2 == 1 :
                robot.drive_time(0, -50, 300) 
                robot.drive (500, 0)
                wait(500)
                forward()
                break 
        if color1 == 1 and color2 != 1 :
                robot.drive_time(0, 50, 300)
                robot.drive (500, 0)
                wait(500)
                forward()
                break'''
    robot.drive (150, 0)
    while L.angle()< 80:
        pass
    robot.stop(Stop.BRAKE)
def backward() :
    while True :
        B1=color_B1P.color()
        B2=color_B2P.color()
        L.run(350)
        R.run(280)
        if B1 == 1 :
            break
    while True :
        B1=color_B1P.color()
        B2=color_B2P.color()
        L.run(-80)
        R.run(140)
        if B2 == 1 :
            break
    robot.stop(Stop.BRAKE)
def dum_check() :
    while True :
        B1=color_1P.color()
        B2=color_2P.color()
        L.run(-350)
        R.run(-280)
        if B2 == 1 :
            break
    while True :
        B1=color_B1P.color()
        B2=color_B2P.color()
        L.run(140)
        R.run(-80)
        if B2 == 1 and B1 == 1:
            break
        elif B2 == 1 and B1 != 1:
            dw_antibug()
            backward()
            break
    robot.stop(Stop.BRAKE)
def fw_backward() :
    while True :
        F1=color_1P.color()
        F2=color_2P.color()
        L.run(-350)
        R.run(-280)
        if F1 == 1 :
            break
    while True :
        F1=color_1P.color()
        F2=color_2P.color()
        L.run(80)
        R.run(-140)
        if F2 == 1 :
            break
    robot.stop(Stop.BRAKE)
def backward_green() :
    while True :
        B1=color_B1P.color()
        B2=color_B2P.color()
        L.run(250)
        R.run(180)
        if B1 == 3 :
            break
    while True :
        B1=color_B1P.color()
        B2=color_B2P.color()
        L.run(-70)
        R.run(150)
        if B2 == 3 :
            break
    robot.stop(Stop.BRAKE)
def left_abug() :
    robot.drive_time(0, 140, 2000) 
    robot.stop(Stop.BRAKE)
    wait(100)
def right_abug() :
    robot.drive_time(0, -140, 2000) 
    robot.stop(Stop.BRAKE)
    wait(100)
def right_a2bug() :
    robot.drive_time(0, -130, 2000) 
    robot.stop(Stop.BRAKE)
    wait(100)
def right_aabug() :
    robot.drive_time(0, -140, 1600) 
    robot.stop(Stop.BRAKE)
    wait(100)
def right_max() :
    robot.drive_time(0, -150, 1000) 
    robot.stop(Stop.BRAKE)
    wait(100)
def left_max() :
    robot.drive_time(0, 150, 1000) 
    robot.stop(Stop.BRAKE)
    wait(100)
def right() :
    robot.drive_time(0, -160, 1000) 
    robot.stop(Stop.BRAKE)
    wait(100)
def right_bug() :
    robot.drive_time(0, -130, 1000) 
    robot.stop(Stop.BRAKE)
    wait(100)
def right_bbug() :
    robot.drive_time(0, -100, 1000) 
    robot.stop(Stop.BRAKE)
    wait(100)
def right_gg() :
    robot.drive_time(0, -140, 1000) 
    robot.stop(Stop.BRAKE)
    wait(100)
def left_agg() :
    robot.drive_time(0, 210, 1000) 
    robot.stop(Stop.BRAKE)
    wait(100)
def right_agg() :
    robot.drive_time(0, -210, 1000) 
    robot.stop(Stop.BRAKE)
    wait(100)
def left() :
    robot.drive_time(0, 160, 1000) 
    robot.stop(Stop.BRAKE)
    wait(100)
def left_bug() :
    robot.drive_time(0, 130, 1000) 
    robot.stop(Stop.BRAKE)
    wait(100)
def left_gg() :
    robot.drive_time(0, 140, 1000) 
    robot.stop(Stop.BRAKE)
    wait(100)
def push() :
    M_motor.on_for_degrees(speed=-100,degrees=100)
    wait(400)
    M_motor.on_for_degrees(speed=100,degrees=100)
    sleep(0.5)  
def green() :
    L.reset_angle(0)
    R.reset_angle(0)  
    while True :
        color1=color_1P.color()
        color2=color_2P.color()
        robot.drive(-350,0)
        if color1 == 3 or color2 == 3 : 
            robot.stop(Stop.BRAKE)
            wait(500)
            L.reset_angle(0)
            R.reset_angle(0)
            push()
            tank_pair.on_for_rotations(left_speed=50,right_speed=50,rotations=1.3);
            break 
def confirm() :
    while not any(brick.buttons()):
        wait(10)
    while any(brick.buttons()):
        wait(10)
def blackhole_end() :
    tank_pair.on_for_rotations(left_speed=-100, right_speed=-100, rotations=1.1);
def blackhole_end2() :
    tank_pair.on_for_rotations(left_speed=100, right_speed=100, rotations=1.1);
def bypass() :
    tank_pair.on_for_rotations(left_speed=-100, right_speed=-100, rotations=3.5);
def fw_antibug() :
    robot.drive(-100,0)
    wait(500)
def bw_antibug() :
    robot.drive(100,0)
    wait(500)
def forward_blackhole() :
    tank_pair.on_for_rotations(left_speed=-70,right_speed=-70,rotations=3.7);
    tank_pair.on_for_rotations(left_speed=-100,right_speed=-0,rotations=1.3);
    wait(100)
    backward()
def forward_block() :
    robot.drive(-600,0)
    wait(1000)
    robot.stop(Stop.BRAKE)
def forward_green() :
    robot.drive(-500,0)
    wait(1300)
    robot.stop(Stop.BRAKE)
def backward_block() :
    robot.drive(400,0)
    wait(500)
    robot.stop(Stop.BRAKE)
def endstart() :
    L.reset_angle(0)
    R.reset_angle(0)  
    while True :
        color1=color_B1P.color()
        color2=color_B2P.color()
        robot.drive(-400,0)
        if color1 == 5 or color2 == 5 :
                robot.stop(Stop.BRAKE)
                wait(100)
                L.reset_angle(0)
                R.reset_angle(0)
                break   

#start
brick.sound.beep()
wait(150)
forward()
right()
backward()
forward()
right()
backward()
forward()
right()
backward()
forward()
left()
backward()
green()
left_bug()
left_bug()
left_bug()
backward_block()
fw_antibug()
backward_on_blackhole()
robot.drive(600,0)
wait(2700)
right()
backward()
forward()
right_bug()
green()
right_abug()
backward_block()
backward_block()
backward()
green()
backward_block()
left()
backward()
forward()
left_bug()
forward()
right()
backward()
green()
right()
backward()
forward()
forward()