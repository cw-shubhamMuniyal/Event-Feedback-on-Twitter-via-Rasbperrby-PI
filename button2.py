import RPi.GPIO as GPIO
import time
import file1
import file2
import cam
import popup2
def but():
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
            cam.camera()
            print('camera pressed')
            popup2.pop2()
            file1.start(i)
            i=i+1
            time.sleep(0.2)

        if input_state2 == False:
            print('Button2 Pressed')
            cam.camera()
            print('camera pressed')
            popup2.pop2()
            file2.start(j)
            j=j+1
            time.sleep(0.2)
if __name__=='__main__' :
    but()