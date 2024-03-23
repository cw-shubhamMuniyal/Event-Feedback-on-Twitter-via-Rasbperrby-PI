from TwitterAPI import TwitterAPI
import time
import cam
import picamera

# Twitter App access keys for @user
def start(j):
    
    # Consume: get these keys from twiter handle
    CONSUMER_KEY    = ''
    CONSUMER_SECRET = ''

    # Access:  get these keys from twiter handle
    ACCESS_TOKEN  = ""
    ACCESS_SECRET = ""

    
    api = TwitterAPI(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
    file = open('my_image.jpg', 'rb')
    print()
    data = file.read()
    r = api.request('statuses/update_with_media', {'status':'4 stars'}, {'media[]':data})
    print(r.status_code)