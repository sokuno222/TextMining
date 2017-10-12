filePath = "C:/Users/sokuno/TextMining"
import os
import pickle
import twitter
from TwitterKeys import *


def PickleBuddy():
    files = os.listdir(filePath)  # make a list of all the files that already exist
    if not "cachedData.pickle" in files:
        api = twitter.Api(consumer_key=CONSUMER_KEY,
                          consumer_secret=CONSUMER_SECRET,
                          access_token_key=ACCESS_TOKEN_KEY,
                          access_token_secret=ACCESS_TOKEN_SECRET)
        fullTweet = api.GetSearch(term='#inspirationalquotes', raw_query=None, geocode=None, since_id=None, max_id=None, until=None, since=None, count=100, lang=None, locale=None, result_type='recent', include_entities=None)
        pickles = open('cachedData.pickle', 'wb')
        pickle.dump(fullTweet, pickles)
        pickles.close

def unPickleBuddy():
    unpickles = open(filePath+'/cachedData.pickle', 'rb')
    untest = pickle.load(unpickles)
    return untest






PickleBuddy()
unPickleBuddy()
  #try:
    #cache = open('cachedData.txt')
  #except:
