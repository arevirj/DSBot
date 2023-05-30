import tweepy
import gspread
import random
gc = gspread.service_account('credentials.json')

# Open a sheet from a spreadsheet in one go
wks = gc.open("testingspreadhsheet").sheet1

client_ID = "1"
client_secret = ""
bearer = ""
apikey = ""
apisecret = ""

access_token = ""
access_secret = ""


auth = tweepy.OAuth1UserHandler(apikey, apisecret, access_token, access_secret)
api = tweepy.API(auth)

client = tweepy.Client(bearer_token= bearer, consumer_key= apikey, consumer_secret= apisecret, access_token= access_token, access_token_secret= access_secret)

tweets = wks.col_values(1)
tweetindex = random.randint(0, len(tweets)-1)
next_quote = tweets[tweetindex]
print(next_quote)
client.create_tweet(text= next_quote)