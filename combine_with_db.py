import  ImgDownload
import  googlevision
import  db_api
import sys

def whole(twitter_account):
	ImgDownload.get_all_tweets(twitter_account)
	googlevision.generate_video()
	db_api.mysql_input()
	db_api.mangodb_input()

if __name__=='__main__':
	try:
	    inputAccount = sys.argv[1]

	    print("please input a keyowrd:")
	    keyword = input()

	    whole(inputAccount)
	    db_api.mysql_search_kw(keyword)
    	db_api.mysql_pics_feed()
    	db_api.mysql_popular()

    	db_api.mangodb_search_kw(keyword)
   	 	db_api.mangodb_pics_feed()
    	db_api.mangodb_popular()

	except:
	    print("Oops! There is no twitter account!")
	
	    