import tweepy
import schedule
import time
import random
import tokens as tk

#choice of different messages
choices = []

def authorize():
    auth = tweepy.OAuthHandler(tk.token, tk.token_secret)
    auth.set_access_token(tk.access_token, tk.access_token_secret)
    api = tweepy.API(auth)
    return api

#sends dm to every friend(followed people by bot)
def send_dm():
    api = authorize()
    friends = api.friends_ids()
    for i in friends:
        print(f'id= {i}, username= {api.get_user(i).screen_name}')
        usr = api.get_user(i)
        tweet = random.choice(choices)
        api.send_direct_message(recipient_id=usr.id, text=tweet)
        print(f'DM Sent to {api.get_user(i).screen_name}')

#sends tweet, tweet context can be changed by editing this function
def send_tweet():
    global count
    api = authorize()
    api.update_status(count)
    print('Tweet sent.')
    count = count + 1

count = 1

schedule.every().day.at("00:00").do(send_dm)
schedule.every().day.at("00:00").do(send_tweet)

while True:
    schedule.run_pending()
    time.sleep(1)