from twitter.api import Twitter
from twitter import *
import oauth
from secrets import *
import requests
import Algorithmia


client = Algorithmia.client(ALGO_CLIENT)
algo = client.algo('besirkurtulmus/talk2city/0.1.0')


auth = OAuth(
    consumer_key=C_KEY,
    consumer_secret=C_SECRET,
    token=A_TOKEN,
    token_secret=A_TOKEN_SECRET
)

twitter_service = Twitter(auth=auth)
twitter_userstream = TwitterStream(auth=auth, domain='userstream.twitter.com')



def get_target_handle(text):
    print("Sending to Algorithmia")
    input = {
        "tweet": text
    }
    return algo.pipe(input).result['twitter_handle'].split("/")[-1]

def limit_to_140(text):
    return text[:140]

def create_reply_text(text, tgt_handle):
    return "Your message will be passed to @%s" % tgt_handle

def create_post_text(text, sender_handle, tgt_handle):
    return limit_to_140("@%s - %s says: %s" % (tgt_handle, sender_handle, text))

print("loaded module")

if __name__ == '__main__':

    print("Starting Twitter bot")

    for msg in twitter_userstream.user():
        if 'direct_message' in msg:
            try:
                msg = msg['direct_message']

                sender_handle = msg['sender']['screen_name']
                sender_id = msg['sender']['id']
                text = msg['text']

                twitter_service.direct_messages.new(user=sender_handle, text='Let me see who can help us. Wait a moment...')

                tgt_handle = get_target_handle(text)

                reply_text = create_reply_text(text, tgt_handle)
                status_text = create_post_text(text, sender_handle, tgt_handle)

                print("Posting status: `%s`" % status_text)
                twitter_service.statuses.update(status=status_text)

                print("Replying to the user @%s:`%s`" % (sender_handle, reply_text))
                twitter_service.direct_messages.new(user=sender_handle, text=reply_text)

            except Exception as e:
                print(e)

