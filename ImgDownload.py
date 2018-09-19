#!/usr/bin/env python3
# encoding: utf-8
#Author - Bowen Jia


import tweepy #https://github.com/tweepy/tweepy
import urllib.request


# Twitter API credentials
consumer_key = ""                                               #"Enter the consumer_key"
consumer_secret = ""                   #"Enter the consumer_secret"
access_key = ""                        #"Enter the access_key"
access_secret = ""                          #"Enter the access_secret"


def get_all_tweets(screen_name):    
    #authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    
    #initialize a list to hold all the tweepy Tweets
    alltweets = []    
    #make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name = screen_name,count=20)
    
    #save most recent tweets
    alltweets.extend(new_tweets)
    
    imgName=0

    for tweet in new_tweets:
        media = tweet.entities.get('media', [])
    
        if(len(media) > 0):
            imgName+=1
            imgPath = media[0]['media_url']
            #download the pics to a specified path
            f = open('./'+ str(imgName)+".jpg", 'wb')
            f.write((urllib.request.urlopen(imgPath)).read())

if __name__ == '__main__':
    #pass in the username of the account you want to downloadc
    get_all_tweets("@BostonDotCom")
