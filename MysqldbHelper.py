#-*-coding: utf-8 -*-
import pymysql
 
class MysqldbHelper:
    # def getMysql(self):
    #     return MysqldbHelper()
    #获取数据库连接
    def __getCon(self):
        try:
            conn = pymysql.connect(host='127.0.0.1', user='root', password='root@123', db='db_oa',charset="utf8")
            return conn
        except Exception as e:
            print("Mysqldb Error:%s",e)
    #查询方法，返回结果为字典    
    def select(self,sql):
        try:
            con=self.__getCon()
            cur = con.cursor()
            cur.execute(sql)
            fc=cur.fetchall()
            return fc
        except Exception as e:
            print("Mysqldb Error:%s",e)
        finally:
            cur.close()
            con.close()
    #带参数的更新方法,eg:sql='insert into pythontest values(%s,%s,%s,now()',params=(6,'C#','good book')
    def updateByParam(self,sql,params):
        try:
            con=self.__getCon()
            cur=con.cursor()
            count=cur.execute(sql,params)
            con.commit()
            return count
        except Exception as e:
            con.rollback()
            print("Mysqldb Error:%s",e)
        finally:
            cur.close()
            con.close()
    #不带参数的更新方法
    def update(self,sql):
        try:
            con=self.__getCon()
            cur=con.cursor()
            count=cur.execute(sql)
            con.commit()
            return count
        except Exception as e:
            con.rollback()
            print("Mysqldb Error:%s",e)
        finally:
            cur.close()
            con.close()
    
    #更新多行数据
    def updateRaws(self,sql,raws):
      
        con=self.__getCon()
        cur=con.cursor()
        try:
            for raw in raws:
                cur.execute(sql,raw)
                con.commit()
        except Exception as e:
            con.rollback()
            print("Mysqldb Error:%s",e)
        finally:
            cur.close()
            con.close()

        #不带参数的更新方法
    def updateForeignKey(self,sql1,sql2,sql3):
        try:
            con=self.__getCon()
            cur=con.cursor()
            cur.execute(sql1)
            con.commit()
            cur.execute(sql2)
            con.commit()
            count = cur.execute(sql3)
            con.commit()
            print(count)
        except Exception as e:
            con.rollback()
            print("Mysqldb Error:%s",e)
        finally:
            cur.close()
            con.close()
    