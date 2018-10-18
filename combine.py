
#!/usr/bin/env python3
# encoding: utf-8
#Author - Bowen Jia


import tweepy #https://github.com/tweepy/tweepy
import urllib.request
import io,os,sys,ffmpeg

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

import PIL
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# Twitter API credentials
consumer_key = ""                      #"Enter the consumer_key"
consumer_secret = ""                   #"Enter the consumer_secret"
access_key = ""                        #"Enter the access_key"
access_secret = ""                     #"Enter the access_secret"


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

def convert_video_with_label():
    # Instantiates a client
    client = vision.ImageAnnotatorClient()
    for i in range(1,16):
    # The name of the image file to annotate
        file_name = os.path.join(os.path.dirname(__file__),'%d.jpg'%(i))

    # Loads the image into memory
        with io.open(file_name, 'rb') as image_file:
            content = image_file.read()

        image = types.Image(content=content)

    # Performs label detection on the image file
        response = client.label_detection(image=image)
        labels = response.label_annotations

        print('image%dlabels:'%i)
        for label in labels:
            print(label.description)
    #       print(label.score)


        font=ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeMono.ttf", 30)

        im1=Image.open(file_name)


        draw=ImageDraw.Draw(im1)

        j=0

        for label in labels:

            draw.text((0,j),label.description,(255,255,0),font=font)

            j+=30
        
        draw=ImageDraw.Draw(im1)

        im1.save("%d.jpg"%(i))


if __name__ == '__main__':
    #pass in the username of the account you want to downloadc
    get_all_tweets("@BostonDotCom")

    convert_video_with_label()

    #generate Labeled video
    os.system("ffmpeg -r 1 -f image2 -i %d.jpg  Boston.mp4")
