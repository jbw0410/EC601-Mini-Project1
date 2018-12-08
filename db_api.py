
import pymysql
import pymongo
from time import time,localtime,asctime

########
########
# mysql

def mysql_input(twi_id,num,desc):

        db= pymysql.connect(host="localhost",user="debian-sys-maint",password="bu",db="mini3_test",port=3306)   

        cursor = db.cursor()

        sql = """INSERT INTO twi_info VALUES (null,default,"""+'"'+twi_id+'"'+","+str(num)+',"'+desc+'");'   

        db.commit()

        db.close()


def mysql_search_kw(keyword):

    db= pymysql.connect(host="localhost",user="debian-sys-maint",password="bu",db="mini3_test",port=3306)   

    cursor = db.cursor()

    sql = "SELECT * FROM twi_info WHERE `twi_id` = '"+keywords+"' or `desc` = '"+keywords+"';"   
    
    cursor.execute(sql)

    result = cursor.fetchall()

    for i in result:

        print(i)

    db.close()


def mysql_pics_feed():

    db= pymysql.connect(host="localhost",user="debian-sys-maint",password="bu",db="mini3_test",port=3306)   

    cursor = db.cursor()

    sql = "SELECT AVG(Pictures) FROM twi_info;"

    cursor.execute(sql)

    result = cursor.fetchall()

    for i in range(0,len(result)):

        print(result[i])

    db.close()


def mysql_popular():

    db= pymysql.connect(host="localhost",user="debian-sys-maint",password="bu",db="mini3_test",port=3306)   

    cursor = db.cursor()

    sql = "SELECT `desc`,COUNT(*)a FROM twi_info GROUP BY `desc` ORDER BY COUNT(*) DESC"

    cursor.execute(sql)

    result = cursor.fetchall()
  
    for i in range(0,len(result)):

        print(result[i])

    db.close()

########
########
# mangodb

def mangodb_input(twi_id,num,desc):

    conn = pymongo.MongoClient('localhost', 27017)

    db = conn.mini3test

    dt = db.userinfo

    dt.insert({"id":twi_id,"login_date":asctime(localtime(time())),"pics_feed":num,"desc":desc})


def mangodb_search_kw(keyword):

    conn = pymongo.MongoClient('localhost', 27017)

    db = conn.mini3test

    dt = db.userinfo

    for info in dt.find({"$or":[{"twi_id":keyword},{"desc":keyword}]}):

        print(info)


def mangodb_pics_feed():

    conn = pymongo.MongoClient('localhost', 27017)

    db = conn.mini3test

    dt = db.userinfo

    avg = dt.aggregate([{"$group":{"twi_id":"average","value":{"$avg":"$pics_num"}}}])

    print(list(avg))


def mangodb_popular():

    conn = pymongo.MongoClient('localhost', 27017)

    db = conn.mini3test

    dt = db.userinfo

    most = dt.aggregate([{"$group":{"twi_id": desc}}])

    print(list(most))

    
if __name__ == '__main__':

    # mysql
    mysql_input(twi_id,num,desc)
    mysql_search_kw(keyword)
    mysql_pics_feed()
    mysql_popular()
    # mangodb
    mangodb_input(twi_id,num,desc)
    mangodb_search_kw(keyword)
    mangodb_pics_feed()
    mangodb_popular()