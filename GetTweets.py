import twitter
from TwitterKeys import *
from Pickling import PickleBuddy, unPickleBuddy

def cleanTweet(unsorted):
    textList = []
    cleanList = []
    for tweet in unsorted:
        textList.append(tweet.text)
    for text in textList:
        if text[0] == 'R':
            cleaned = (text.split(':')[1])
        if '#' in cleaned:
            cleaned = cleaned.split("#")[0]
        if cleaned != '':
            cleanList.append(cleaned)
    return cleanList


def getTweets():
    PickleBuddy()
    unfilteredTweet = unPickleBuddy()
    niceTweet = cleanTweet(unfilteredTweet)
    return niceTweet
