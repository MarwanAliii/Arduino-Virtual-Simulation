import serial
from visual import * 

MyScene = display( title = "My Virtual World" )
MyScene.width = 800
MyScene.height = 800
MyScene.autoscale = False
MyScene.range = (12, 12, 12)

target = box(length = .1, width = 10, height = 5, pos = (-6, 0, 0))
myBoxEnd = box(length = .1, width = 10, height = 5, pos = (-8.5, 0, 0))
myTube2 = cylinder(color = color.blue, pos = (-8.5, 0, -2.5), radius = 1.5, length = 2.5)
myTube3 = cylinder(color = color.blue, pos = (-8.5, 0, 2.5), radius = 1.5, length = 2.5)
myBall = sphere(color = color.red, radius = .3)

sensorData = serial.Serial('com11', 115200)

while True:
  rate(25)
  while(sensorData.inWaiting()==0):
    pass
  textline = sensorData.readline()
  dataNums = textline.split(',')
  red = float(dataNums[0])
  green = float(dataNums[1])
  blue = float(dataNums[2])
  dist = float(dataNums[3])
  
  blue = blue * .7
  
  if(dist >= 1.5 and dist <= 2.25):
    target.color = (red/225., green/225., blue/225.)
    
   target.pos = vector(-6+dist, 0, 0)
