import MysqldbHelper
import os

class writeMysqlToTxt:
    def __init__(self):
        pathList = os.listdir(os.chdir(os.getcwd()+'/txt'))    #新目录下文件list
        if os.path.exists('channels.txt' in pathList):
            os.remove('channels.txt')
        if os.path.exists('props.txt' in pathList):
            os.remove('props.txt')
        self.mysqldb = MysqldbHelper.MysqldbHelper()

    def __writeProp(self):
        self.mysqldb.update('''select * from oa_prop_table into outfile 'E:/codewyan/savemysql/OA/txt/props.txt' fields terminated by ',' lines terminated by '\r\n';''')

    def __writeChannel(self):
        self.mysqldb.update('''select * from oa_channel_table into outfile 'E:/codewyan/savemysql/OA/txt/channels.txt' fields terminated by ',' lines terminated by '\r\n';''')
    def writeAllToTxt(self):
        self.__writeProp()
        self.__writeChannel()
      




