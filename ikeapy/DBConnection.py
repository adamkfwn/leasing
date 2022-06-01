import pymysql
#making static class for sql connection
class DBConnection():

    @staticmethod
    def getConnection():
        try:
            conn = pymysql.connect(host='localhost', user='root', password='Kimojimmi1', db='ikea')
        #cursor

            return conn
        except Exception as e:
            print(e)