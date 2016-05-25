import time
import picamera
import cv2
import numpy as np

Filename = 'Test_image'

exposure = 100 + 7*np.linspace(0,100,11)
#exposure = 500*np.ones(20)
count = 0
print exposure
for i in exposure:
    print int(i)
    with picamera.PiCamera() as camera:
        camera.resolution = (500, 500)
        camera.framerate = 30
        # Wait for the automatic gain control to settle
        time.sleep(1)
        # Now fix the values
        #camera.shutter_speed = camera.exposure_speed
        camera.shutter_speed = int(i)
        camera.exposure_mode = 'off'
        g = camera.awb_gains
        camera.awb_mode = 'off'
        #camera.awb_gains = g
        camera.awb_gains = [0.96, 2.8]
        camera.iso = 100
        # Finally, take several photos with the fixed settings
        # camera.capture_sequence(['image%02d.jpg' % i for i in range(10)])
        camera.capture(Filename+'_'+str(int(i))+'_'+str(count)+'.png')
	count += 1


