import mysql.connector

class Conexion:
    
    user="pmauser"
    passw="ortizcalderon"
    #hos="localhost"
    hos="18.222.117.126"
    db="ovaeducativa"
    mydb=None
    
    def __init__(self):
        self.connect()

    def connect(self):
        self.mydb = mysql.connector.connect(host=self.hos, user=self.user, passwd=self.passw , database=self.db)

    def modify(self, sql , data):
        try:
            self.connect()
            ins=self.mydb.cursor()
            ins.execute(sql,data)
            self.mydb.commit()
            return True
        except:
            self.mydb.rollback()
            return False
        if self.mydb:
            self.mydb.close()

    def find(self,sql,data):
        try:
            self.connect()
            ins=self.mydb.cursor()
            ins.execute(sql,data)
            return ins.fetchall()
        except:
            self.mydb.rollback()
        if self.mydb:
            self.mydb.close()

    def many(self,sql,data):
        try:
            self.connect()
            ins=self.mydb.cursor()
            ins.executemany(sql,data)
            self.mydb.commit()
            return True
        except:
            self.mydb.rollback()
            return False
        finally:
            if (self.mydb.is_connected()):
                ins.close()
                self.mydb.close()
                print("MySQL connection is closed")