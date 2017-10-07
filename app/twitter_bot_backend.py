from twitter.api import Twitter
from twitter import *
import oauth
from secrets import *

auth = OAuth(
    consumer_key=C_KEY,
    consumer_secret=C_SECRET,
    token=A_TOKEN,
    token_secret=A_TOKEN_SECRET
)

twitter_service = Twitter(auth=auth)
twitter_userstream = TwitterStream(auth=auth, domain='userstream.twitter.com')


def logic(msg):
    screen_name = msg['sender']['screen_name']
    text = msg['text']
    new_text = "User %s says: %s" % (screen_name, text)
    return new_text

print("loaded module")

if __name__ == '__main__':

    print("Starting Twitter bot")

    for msg in twitter_userstream.user():
        if 'direct_message' in msg:
            try:
                new_text = logic(msg['direct_message'])

                print("Posting status: `%s`" % new_text)
                twitter_service.statuses.update(status=new_text)
            except Exception as e:
                print(e)

