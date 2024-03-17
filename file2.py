from TwitterAPI import TwitterAPI

import time
import cam
import picamera

# Twitter App access keys for @user
def start(j):
    
    # Consume:
    CONSUMER_KEY    = 'phiNHlqS5FVTpydlxy7acPueP'
    CONSUMER_SECRET = '1vI5A6qHe1T3R0Q8M3Fcg5h0Dm3T0uVFM4JubvKeMCxxahzBKL'

      # Access:
    ACCESS_TOKEN  = "1002604131385688064-TNumnPutuact3cekqVXS01jemg0Bet"
    ACCESS_SECRET = "sHvnoREjBBEsvbxKhHmveNKk29yPdJ1Q8RJvNF36gVlvg"

    
    api = TwitterAPI(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
    file = open('my_image.jpg', 'rb')
    print()
    data = file.read()
    r = api.request('statuses/update_with_media', {'status':'4 stars'}, {'media[]':data})
    print(r.status_code)