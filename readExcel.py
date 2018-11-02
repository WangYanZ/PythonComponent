import xlrd
import numpy as np

class readExcel:
    __path = "data_xls"
    def getDataset(self,src):
        dataset = []
        workbook = xlrd.open_workbook(src)
        table = workbook.sheets()[0]
        print(table.nrows)
        for row in range(table.nrows-1):
            dataset.append(table.row_values(row+1))
        return dataset
      #读道具表
    def read_prop_xls_file(self):
        src = self.__path+"/道具/道具配置表.xlsx"
        dataset = self.getDataset(src)
        propList = []
        for g in dataset:
            if g[0] == "":
                continue
            else:
                propList.append((np.int(g[0]),g[1],int(1),str('物品道具'),g[9],g[5]))
        return propList
        #读英雄配置表
    def read_hero_xls_file(self):
        src = self.__path+"/英雄/Y英雄配置表.xlsx" 
        dataset = self.getDataset(src)
        heroList = []
        for g in dataset:
            heroList.append((np.int(g[0]),g[1],int(5),str('物品英雄'),g[12],g[18]))
        return heroList
        #读小宇宙配置表
    def read_microcosm_xls_file(self):
        src = self.__path+"/小宇宙/小宇宙配置.xlsx" 
        dataset = self.getDataset(src)
        microList = []
        for g in dataset:
            microList.append((np.int(g[0]),g[3],int(14),str('物品小宇宙'),g[3],g[4]))
        return microList
    #读其他道具
    def read_other_prop(self):
        otherList = [[3,"物品体力",3,"物品体力","物品体力","物品体力"],[4,"物品钻石",4,"物品钻石","物品钻石","物品钻石"],[7,"物品玩家经验",7,"物品玩家经验","物品玩家经验","物品玩家经验"],[103,"高级星石",103,"高级星石","高级星石","高级星石"]]
        return otherList

    #读渠道表
    def read_channel_xls_file(self):
        src = self.__path+"/掉落底层/掉落集合表.xlsx"
        dataset = self.getDataset(src)
        channelList = []
         #对掉落表里的类型去重
        for g in dataset:
            if not g[18] in channelList:
                if g[18] is not '':
                    channelList.append(g[18])
        #存为[[],[]...]格式
        channelList2 = []
        for g in channelList:
            temp = []
            temp.append(g)
            channelList2.append(temp)
        return channelList2
     #其他6个渠道表
    def read_other_channel(self):
        otherList = [["C场景付费商店关联表"],["军团副本击杀奖励"],["军团副本伤害排名奖励"],["矿石配置表"],["P排行榜奖励内容表"],["H活动进度配置"]]
        return otherList

   



    