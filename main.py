import tweepy
api_key = ""
api_key_secret = ""
api_access_token = ""
api_access_token_secret = ""
 
auth = tweepy.OAuthHandler(api_key,api_key_secret)
auth.set_access_token(api_access_token, api_access_token_secret)
 
api = tweepy.API(auth)
 
try:
    api.verify_credentials()
    print('Successful connection')
except:
    print('Failed connection')
