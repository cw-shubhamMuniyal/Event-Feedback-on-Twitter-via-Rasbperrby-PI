import RPi.GPIO as GPIO
import time
import twitterUtility
import file2
import cameraModule
import userInput
def pressButton():
    i = 1
    j = 1
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    while True:
        input_state = GPIO.input(18)
        input_state2 = GPIO.input(15)
        
        if input_state == False:
            print('Button1 Pressed')
            cameraModule.camera()
            print('camera pressed')
            userInput.inputImage()
            twitterUtility.start(i, '3 stars')
            i=i+1
            time.sleep(0.2)

        if input_state2 == False:
            print('Button2 Pressed')
            cameraModule.camera()
            print('camera pressed')
            userInput.inputImage()
            file2.start(j, '4 stars')
            j=j+1
            time.sleep(0.2)
if __name__=='__main__' :
    pressButton()