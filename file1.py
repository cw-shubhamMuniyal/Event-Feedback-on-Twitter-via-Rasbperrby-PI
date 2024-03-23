from TwitterAPI import TwitterAPI
from twython import Twython
import time
import cam
import picamera

# Twitter App access keys for @user
def start(i):
    
    # Consume: get these keys from twiter handle
    CONSUMER_KEY    = ''
    CONSUMER_SECRET = ''

    # Access:  get these keys from twiter handle
    ACCESS_TOKEN  = ""
    ACCESS_SECRET = ""

    
    api = TwitterAPI(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
    file = open('my_image.jpg', 'rb')
    
    data = file.read()
    print()
    r = api.request('statuses/update_with_media', {'status':'3 stars'}, {'media[]':data})
    print(r.status_code)

    
    print('Tweet successful')


