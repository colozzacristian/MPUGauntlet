class Gyroscope:
    


    def __init__(self):

        self.gyro = [0]*3        #define an arry to store gyroscope data

        self.angles=[0.0]*3      #deve andare da -180 a +180

        self.offsetGyro=[0.0]*3  #Calibration result

        self.tresholdGyro=0

    def setRotation(self):
        global gyro
        global angles

        treshold=0.04
        if(abs(self.gyro[0]) > abs(self.treshold)):
            self.angles[0]=(self.gyro[0]-self.treshold)#*sleepTime

        if(abs(self.gyro[1])>abs(self.treshold)):
            self.angles[1]=(self.gyro[1]-self.treshold)#*sleepTime

        if(abs(self.gyro[2])>abs(self.treshold)):
            self.angles[2]=(self.gyro[2]-self.treshold)#*sleepTime
