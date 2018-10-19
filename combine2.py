import  ImgDownload
import  googlevision
import sys

def whole(twitter_account):
	ImgDownload.get_all_tweets(twitter_account)
	googlevision.generate_video()

if __name__=='__main__':
	try:
	    inputAccount = sys.argv[1]
	    whole(inputAccount)

	except:
	    print("Oops! There is no twitter account!")
	
	    