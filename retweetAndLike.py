import tweepy
import time

auth = tweepy.OAuthHandler('','')
auth.set_access_token('', '')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

busca = 'busque algo aqui'
numTweets = 10

for tweet in tweepy.Cursor(api.search, busca).items(numTweets):
    try:
        print('operação com sucesso')
        tweet.retweet()
        tweet.favorite()
        time.sleep(60)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break