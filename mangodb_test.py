import pymongo
#search keyword

conn = pymongo.MongoClient('localhost', 27017)

db = conn.mini3test

dt = db.userinfo

for info in dt.find({"$or":[{"id":keyword},{"desc":keyword}]}):

    print(info)
