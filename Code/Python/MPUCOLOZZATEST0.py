#!/usr/bin/env python3
########################################################################
# Filename    : MPU6050RAW.py
# Description : Read data of MPU6050.
# auther      : www.freenove.com
# modification: 2021/1/1
########################################################################
import MPU6050 
import time

mpu = MPU6050.MPU6050()     # instantiate a MPU6050 class object
accel = [0]*3               # define an arry to store accelerometer data
gyro = [0]*3                # define an arry to store gyroscope data

angles=[0.0]*3 #deve andare da -180 a +180

offsetAccel=[0.0]*3
offsetGyro=[0.0]*3

gyroConst = 131.0
accelConst = 16384.0
calibrationLoop=100
sleepTime=0.1

tresholdGyro=0.0

def setup():
    mpu.dmp_initialize()    # initialize MPU6050

def calibration():
    print("calibrating ... ")

    for i in range(calibrationLoop):
        accel = mpu.get_acceleration()      # get accelerometer data
        gyro = mpu.get_rotation()           # get gyroscope data
        for j in range(3):         
            offsetAccel[j]+=(accel[j]/accelConst)
            offsetGyro[j]+=(gyro[j]/gyroConst)
        time.sleep(sleepTime)

    # trovo la media dividendo per i valori di prova
    for j in range(3):         
        offsetAccel[j]/=calibrationLoop
        offsetGyro[j]/=calibrationLoop

def getDirection(): #deve ritornare una stringa con le varie direzioni concatenate, è un PoC
    global gyro
    direction=""
    treshold=0.04
    if(gyro[0]>treshold):
        direction+="sinistra "
    elif(gyro[0]< -treshold):
        direction+="destra "
    else:
        direction+="neutrale "
    
    if(gyro[1]>treshold):
        direction+="indietro "
    elif(gyro[1]< -treshold):
        direction+="avanti "
    else:
        direction+="neutrale "

    if(gyro[2]>treshold):
        direction+="antiorario "
    elif(gyro[2]< -treshold):
        direction+="orario "
    else:
        direction+="neutrale "

    return direction

def setRotation():
    global gyro
    global angles

    treshold=0.04
    if(abs(gyro[0]) > abs(treshold)):
        angles[0]=(gyro[0]-treshold)#*sleepTime

    if(abs(gyro[1])>abs(treshold)):
        angles[1]=(gyro[1]-treshold)#*sleepTime

    if(abs(gyro[2])>abs(treshold)):
        angles[2]=(gyro[2]-treshold)#*sleepTime

  

    
def loop():
    
    global gyro
    global angles
    
    print("starting...")    
    while(True):
        accel = mpu.get_acceleration()      # get accelerometer data
        gyro =  mpu.get_rotation()          # get gyroscope data

        for j in range(3):         
                    accel[j]=(accel[j]/accelConst)-offsetAccel[j]
                    gyro[j] =(gyro [j]/gyroConst )-offsetGyro [j]
        
        direction=getDirection()
        setRotation()

        if(abs(gyro[0]) > tresholdGyro or abs(gyro[1]) > tresholdGyro or abs(gyro[2]) > tresholdGyro):
            print("a/g:%.2f g\t%.2f g\t%.2f g\t%.2f d/s\t%.2f d/s\t%.2f d/s\t%s\t%.2f d\t%.2f d\t%.2f d\t"
            %(accel[0],accel[1],accel[2],gyro[0],gyro[1],gyro[2],direction,angles[0],angles[1],angles[2]),end="\r")
        time.sleep(sleepTime)
        
if __name__ == '__main__':     # Program entrance
    
    setup()
    try:
        calibration()
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        pass

