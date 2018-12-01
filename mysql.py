import pymysql  

db= pymysql.connect(host="localhost",user="debian-sys-maint",
     password="bu",db="mini3_test",port=3306)
cur = db.cursor()
sql = "select id from twi_info;"

try:
    cur.execute(sql)     
    results = cur.fetchall()    
    for i in results:
        print(i)
    print('done!')

except Exception as e:
    raise e

finally:
    db.close()    
