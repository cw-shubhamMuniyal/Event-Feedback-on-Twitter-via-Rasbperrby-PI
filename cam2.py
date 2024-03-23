from TwitterAPI import TwitterAPI
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
r = api.request('statuses/update_with_media', {'status':'username'}, {'media[]':data})
print(r.status_code)
