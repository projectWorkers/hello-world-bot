import tweepy # for tweeting
import secrets # shhhh
import re #Regular expression
from random import randint #For randomizing

def insult():
    vFile = open("verb.txt", "r")
    ingList = []
    insult = ""
    for word in vFile.readlines():
    	if re.match(".*ing(.|\n)$", word):
	    	ingList.append(word)
    insult = insult + ingList[randint(1, len(ingList))]
    vFile.close()


    aFile = open("adj.txt", "r")
    aList = []
    for word in aFile.readlines():
	    aList.append(word)
    insult = insult + aList[randint(1, len(aList))]
    aFile.close()

    nFile= open("noun.txt", "r")
    nList = []
    for word in nFile.readlines():
	    nList.append(word)
    insult = insult + nList[randint(1, len(nList))]
    nFile.close()
    return insult

def tweet(message):
  auth = tweepy.OAuthHandler(secrets.consumer_key, secrets.consumer_secret)
  auth.set_access_token(secrets.access_token, secrets.access_token_secret)
  api = tweepy.API(auth)
  auth.secure = True
  print("Posting message {}".format(message))
  api.update_status(status=message)

if __name__ == '__main__':
  tweet(insult())
