import tweepy
import time

auth = tweepy.OAuthHandler('','')
auth.set_access_token('', '')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

busca = 'Busque por tweet'
numTweets = 5

for tweet in tweepy.Cursor(api.search, busca).items(numTweets):
    try:
        if(len(tweet.text) <= 130):
            api.update_status('@' + tweet.user.screen_name + ' ' + tweet.text, in_reply_to_status_id = tweet.id)
            print('operação com sucesso')
            print(len(tweet.text))
            time.sleep(60)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break