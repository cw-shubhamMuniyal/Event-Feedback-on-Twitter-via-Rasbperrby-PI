import time
import picamera

def camera():
    # Explicitly open a new file called my_image.jpg
    my_file = open('my_image.jpg', 'wb')
    with picamera.PiCamera() as camera:
        camera.resolution =(480,480)
        camera.start_preview(fullscreen=False,window=(100,200,640,480))
        time.sleep(2)
        camera.capture(my_file)
    # At this point my_file.flush() has been called, but the file has
    # not yet been closed
    my_file.close()
