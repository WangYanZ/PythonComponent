import MysqldbHelper
import readExcel

class saveDB:
    
    def __init__(self):
        self.readexc = readExcel.readExcel()
        self.mysqldb = MysqldbHelper.MysqldbHelper()

        
       
    def saveProps(self):
        
        truncate1 = self.mysqldb.update(''' truncate table oa_prop_channel_table''')
        print("truncate: "+str(truncate1))

        truncate2 = self.mysqldb.updateForeignKey(''' SET FOREIGN_KEY_CHECKS = 0''','''truncate table oa_prop_table ''',''' SET FOREIGN_KEY_CHECKS = 1 ''')
        print("truncate: "+str(truncate2))

        
        prop = self.readexc.read_prop_xls_file()
        hero = self.readexc.read_hero_xls_file()
        micro = self.readexc.read_microcosm_xls_file()
        other = self.readexc.read_other_prop()
        #切片合并list
        prop[len(prop):len(prop)] = hero
        prop[len(prop):len(prop)] = micro
        prop[len(prop):len(prop)] = other

        #props插入数据
        sql3 = '''
        insert into oa_prop_table(prop_id,prop_name,prop_typeid,prop_typename,prop_desc,type)
        values(%s,%s,%s,%s,%s,%s);
       '''
        self.mysqldb.updateRaws(sql3,prop)
    def saveChannels(self):
        truncate1 = self.mysqldb.update(''' truncate table oa_prop_channel_table''')
        print("truncate: "+str(truncate1))

        truncate3 = self.mysqldb.updateForeignKey(''' SET FOREIGN_KEY_CHECKS = 0''','''truncate table oa_channel_table ''',''' SET FOREIGN_KEY_CHECKS = 1 ''')
        print("truncate: "+str(truncate3))
         
        
        channel = self.readexc.read_channel_xls_file()
        other = self.readexc.read_other_channel()

        channel[len(channel):len(channel)] = other

        #channels插入数据
        sql4 = '''insert into oa_channel_table(channel_name)
        values(%s);
       '''
        self.mysqldb.updateRaws(sql4,channel)


        