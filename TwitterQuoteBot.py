import re
from GetTweets import getTweets
from sentence_generator import buildMapping, genSentence, main
words = "".join(getTweets())
words = words.replace('\r', '').replace('\n', '').replace('T.','').replace('D.','')
main(words,1)
