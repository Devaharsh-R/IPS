import mysql.connector
def connectToDb():
    try:
        db=mysql.connector.connect(host='localhost',user='root',password='',database='test')
    except:
        print('Database connection Failed')
        exit()
connectToDb()