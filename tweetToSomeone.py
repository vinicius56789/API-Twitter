import tweepy
import time

auth = tweepy.OAuthHandler('','')
auth.set_access_token('', '')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

try:
    api.update_status(status = '@user aqui' + ' mensagem aqui')
    print('operação com sucesso')
except tweepy.TweepError as e:
    print(e.reason)
