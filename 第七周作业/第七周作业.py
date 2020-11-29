import xlrd
import matplotlib.pyplot as plt
import random
#print(float('nan'))
#用以下方法获得各个数据表的表名，确认各表名完全一致后作为数据处理类的类属性regions
"""
for i in range(1997,2016):
    wb=xlrd.open_workbook("Province sectoral CO2 emissions {}.xlsx".format(i))
    print(wb.sheet_names())
"""
#用以下方法获得其一数据表的各个sheet的列名，确认完全一致之后作为数据处理类的类属性CO2_types
"""
wb=xlrd.open_workbook("Province sectoral CO2 emissions 2003.xlsx")
for i in ['Sum', 'Beijing', 'Tianjin', 'Hebei', 'Shanxi', 'InnerMongolia', 'Liaoning', 'Jilin', 'Heilongjiang', 'Shanghai', 'Jiangsu', 'Zhejiang', 'Anhui', 'Fujian', 'Jiangxi', 'Shandong', 'Henan', 'Hubei', 'Hunan', 'Guangdong', 'Guangxi', 'Hainan', 'Chongqing', 'Sichuan', 'Guizhou', 'Yunnan', 'Shaanxi', 'Gansu', 'Qinghai', 'Ningxia', 'Xinjiang']:
    ws=wb.sheet_by_name(i)
    print(ws.row_values(0))
"""
#用以下方法获得其一数据表的各个sheet的行名，确认完全一致(除Sum外)之后作为数据处理类的类属性CO2_industries
"""
wb=xlrd.open_workbook("Province sectoral CO2 emissions 2003.xlsx")
for i in ['Sum', 'Beijing', 'Tianjin', 'Hebei', 'Shanxi', 'InnerMongolia', 'Liaoning', 'Jilin', 'Heilongjiang', 'Shanghai', 'Jiangsu', 'Zhejiang', 'Anhui', 'Fujian', 'Jiangxi', 'Shandong', 'Henan', 'Hubei', 'Hunan', 'Guangdong', 'Guangxi', 'Hainan', 'Chongqing', 'Sichuan', 'Guizhou', 'Yunnan', 'Shaanxi', 'Gansu', 'Qinghai', 'Ningxia', 'Xinjiang']:
    ws=wb.sheet_by_name(i)
    print(ws.col_values(0))
"""
"""
['Total Consumption', 'Farming, Forestry, Animal Husbandry, Fishery and Water Conservancy      ', 'Coal Mining and Dressing                                 ', 'Petroleum and Natural Gas Extraction                     ', 'Ferrous Metals Mining and Dressing                       ', 'Nonferrous Metals Mining and Dressing                    ', 'Nonmetal Minerals Mining and Dressing                    ', 'Other Minerals Mining and Dressing                       ', 'Logging and Transport of Wood and Bamboo                 ', 'Food Processing                                          ', 'Food Production ', 'Beverage Production', 'Tobacco Processing                                       ', 'Textile Industry               ', 'Garments and Other Fiber Products                        ', 'Leather, Furs, Down and Related Products      ', 'Timber Processing, Bamboo, Cane, Palm Fiber & Straw Products', 'Furniture Manufacturing', 'Papermaking and Paper Products                           ', 'Printing and Record Medium Reproduction                  ', 'Cultural, Educational and Sports Articles                ', 'Petroleum Processing and Coking                          ', 'Raw Chemical Materials and Chemical Products             ', 'Medical and Pharmaceutical Products                      ', 'Chemical Fiber                                  ', 'Rubber Products                                          ', 'Plastic Products                         ', 'Nonmetal Mineral Products                                ', 'Smelting and Pressing of Ferrous Metals                  ', 'Smelting and Pressing of Nonferrous Metals               ', 'Metal Products                                           ', 'Ordinary Machinery', 'Equipment for Special Purposes                           ', 'Transportation Equipment                                 ', 'Electric Equipment and Machinery                         ', 'Electronic and Telecommunications Equipment              ', 'Instruments, Meters, Cultural and Office Machinery         ', 'Other Manufacturing Industry                             ', 'Scrap and waste', 'Production and Supply of Electric Power, Steam and Hot Water   ', 'Production and Supply of Gas                    ', 'Production and Supply of Tap Water                       ', 'Construction                                             ', 'Transportation, Storage, Post and Telecommunication Services    ', 'Wholesale, Retail Trade and Catering Services            ', 'Others  ', 'Urban', 'Rural']
"""
class TimeAnalysis:
    """
    提供数据的读取及基本的时间分析方法
    类的参数为：地区、碳排放项目、碳排放行业、起始年份（默认为1997）、截前年份（默认为2016）和间隔年数（默认为1年一统计），以据此进行时间连续分析
    """
    def __init__(self,region,CO2_type,CO2_industry,start_year=1997,end_year=2016,interval=1):
        self.regions=['Sum', 'Beijing', 'Tianjin', 'Hebei', 'Shanxi', 'InnerMongolia', 'Liaoning', 'Jilin', 'Heilongjiang', 'Shanghai', 'Jiangsu', 'Zhejiang', 'Anhui', 'Fujian', 'Jiangxi', 'Shandong', 'Henan', 'Hubei', 'Hunan', 'Guangdong', 'Guangxi', 'Hainan', 'Chongqing', 'Sichuan', 'Guizhou', 'Yunnan', 'Shaanxi', 'Gansu', 'Qinghai', 'Ningxia', 'Xinjiang']
        if region in self.regions:
            self.region=region
        else:
            print('Region parameter Wrong!')
            return None
        self.CO2_types=['Raw Coal', 'Cleaned Coal', 'Other Washed Coal', 'Briquettes', 'Coke', 'Coke Oven Gas', 'Other Gas', 'Other Coking Products', 'Crude Oil', 'Gasoline', 'Kerosene', 'Diesel Oil', 'Fuel Oil', 'LPG', 'Refinery Gas', 'Other Petroleum Products', 'Natural Gas', 'Process', 'Total']
        if CO2_type in self.CO2_types:
            self.CO2_type=CO2_type
        else:
            print('Type parameter Wrong!')
            return None
        self.CO2_Sum=['Beijing', 'Tianjin', 'Hebei', 'Shanxi', 'InnerMongolia', 'Liaoning', 'Jilin', 'Heilongjiang', 'Shanghai', 'Jiangsu', 'Zhejiang', 'Anhui', 'Fujian', 'Jiangxi', 'Shandong', 'Henan', 'Hubei', 'Hunan', 'Guangdong', 'Guangxi', 'Hainan', 'Chongqing', 'Sichuan', 'Guizhou', 'Yunnan', 'Shaanxi', 'Gansu', 'Qinghai', 'Ningxia', 'Xinjiang', 'Sum-CO2']
        self.CO2_industries=['Total Consumption', 'Farming, Forestry, Animal Husbandry, Fishery and Water Conservancy      ', 'Coal Mining and Dressing                                 ', 'Petroleum and Natural Gas Extraction                     ', 'Ferrous Metals Mining and Dressing                       ', 'Nonferrous Metals Mining and Dressing                    ', 'Nonmetal Minerals Mining and Dressing                    ', 'Other Minerals Mining and Dressing                       ', 'Logging and Transport of Wood and Bamboo                 ', 'Food Processing                                          ', 'Food Production ', 'Beverage Production', 'Tobacco Processing                                       ', 'Textile Industry               ', 'Garments and Other Fiber Products                        ', 'Leather, Furs, Down and Related Products      ', 'Timber Processing, Bamboo, Cane, Palm Fiber & Straw Products', 'Furniture Manufacturing', 'Papermaking and Paper Products                           ', 'Printing and Record Medium Reproduction                  ', 'Cultural, Educational and Sports Articles                ', 'Petroleum Processing and Coking                          ', 'Raw Chemical Materials and Chemical Products             ', 'Medical and Pharmaceutical Products                      ', 'Chemical Fiber                                  ', 'Rubber Products                                          ', 'Plastic Products                         ', 'Nonmetal Mineral Products                                ', 'Smelting and Pressing of Ferrous Metals                  ', 'Smelting and Pressing of Nonferrous Metals               ', 'Metal Products                                           ', 'Ordinary Machinery', 'Equipment for Special Purposes                           ', 'Transportation Equipment                                 ', 'Electric Equipment and Machinery                         ', 'Electronic and Telecommunications Equipment              ', 'Instruments, Meters, Cultural and Office Machinery         ', 'Other Manufacturing Industry                             ', 'Scrap and waste', 'Production and Supply of Electric Power, Steam and Hot Water   ', 'Production and Supply of Gas                    ', 'Production and Supply of Tap Water                       ', 'Construction                                             ', 'Transportation, Storage, Post and Telecommunication Services    ', 'Wholesale, Retail Trade and Catering Services            ', 'Others  ', 'Urban', 'Rural']
        if region=='Sum':
            if CO2_industry in self.CO2_Sum:
                self.CO2_industry=CO2_industry
            else:
                print('Sum parameter Wrong!')
                return None
        else:
            if CO2_industry in self.CO2_industries:
                self.CO2_industry=CO2_industry
            else:
                print('Industry parameter Wrong!')
                return None        
        if start_year<1997 or not isinstance(start_year,int) or start_year>2015:
            print('Start Year Wrong!')
            return None
        else:
            self.start_year=start_year
        if end_year<1997 or not isinstance(end_year,int) or end_year>2016:
            print('End Year Wrong!')
            return None
        else:        
            self.end_year=end_year
        if isinstance(interval,int) and interval>=1:
            self.interval=interval
        else:
            print('Interval Wrong!')
            return None
    def data_process(self):
        """
        通过数据的读取和处理，返回存有标题、年份、以及对于碳排放数值的列表
        """
        Analysis_title='TimeAnalysis from {} to {}(interval of {} year(s)),{} of {}, in{}'.format(self.start_year,self.end_year,self.interval,self.CO2_type,self.CO2_industry,self.region)
        results=[Analysis_title,[i for i in range(self.start_year,self.end_year,self.interval)]]#Analysis title,[xlabel],.append([data])
        result=[]
        for i in range(self.start_year,self.end_year,self.interval):
            wb=xlrd.open_workbook("Province sectoral CO2 emissions {}.xlsx".format(i))
            ws=wb.sheet_by_name(self.region)
            for k in range(ws.nrows):
                if ws.row_values(0)[k]==self.CO2_type:
                    break
            for j in range(ws.ncols):
                if ws.col_values(0)[j]==self.CO2_industry:
                    break
            value=ws.col_values(k)[j]
            if value==float('nan'):
                raise NotNumError(i,self.region,self.CO2_industry,self.CO2_type)
            else:
                result.append(value)
        results.append(result)
        return results
class SpaceAnalysis:
    """
    提供数据的读取及基本的地区分析方法
    类的参数为：碳排放项目、碳排放行业、分析年份（默认为在1997到2015之间的随机数）以据此进行全国各地分析
    """
    def __init__(self,CO2_type,CO2_industry,year=random.randint(1997,2015)):
        self.regions=['Beijing', 'Tianjin', 'Hebei', 'Shanxi', 'InnerMongolia', 'Liaoning', 'Jilin', 'Heilongjiang', 'Shanghai', 'Jiangsu', 'Zhejiang', 'Anhui', 'Fujian', 'Jiangxi', 'Shandong', 'Henan', 'Hubei', 'Hunan', 'Guangdong', 'Guangxi', 'Hainan', 'Chongqing', 'Sichuan', 'Guizhou', 'Yunnan', 'Shaanxi', 'Gansu', 'Qinghai', 'Ningxia', 'Xinjiang']
        self.CO2_types=['Raw Coal', 'Cleaned Coal', 'Other Washed Coal', 'Briquettes', 'Coke', 'Coke Oven Gas', 'Other Gas', 'Other Coking Products', 'Crude Oil', 'Gasoline', 'Kerosene', 'Diesel Oil', 'Fuel Oil', 'LPG', 'Refinery Gas', 'Other Petroleum Products', 'Natural Gas', 'Process', 'Total']
        if CO2_type in self.CO2_types:
            self.CO2_type=CO2_type
        else:
            print('Type parameter Wrong!')
            return None
        self.CO2_industries=['Total Consumption', 'Farming, Forestry, Animal Husbandry, Fishery and Water Conservancy      ', 'Coal Mining and Dressing                                 ', 'Petroleum and Natural Gas Extraction                     ', 'Ferrous Metals Mining and Dressing                       ', 'Nonferrous Metals Mining and Dressing                    ', 'Nonmetal Minerals Mining and Dressing                    ', 'Other Minerals Mining and Dressing                       ', 'Logging and Transport of Wood and Bamboo                 ', 'Food Processing                                          ', 'Food Production ', 'Beverage Production', 'Tobacco Processing                                       ', 'Textile Industry               ', 'Garments and Other Fiber Products                        ', 'Leather, Furs, Down and Related Products      ', 'Timber Processing, Bamboo, Cane, Palm Fiber & Straw Products', 'Furniture Manufacturing', 'Papermaking and Paper Products                           ', 'Printing and Record Medium Reproduction                  ', 'Cultural, Educational and Sports Articles                ', 'Petroleum Processing and Coking                          ', 'Raw Chemical Materials and Chemical Products             ', 'Medical and Pharmaceutical Products                      ', 'Chemical Fiber                                  ', 'Rubber Products                                          ', 'Plastic Products                         ', 'Nonmetal Mineral Products                                ', 'Smelting and Pressing of Ferrous Metals                  ', 'Smelting and Pressing of Nonferrous Metals               ', 'Metal Products                                           ', 'Ordinary Machinery', 'Equipment for Special Purposes                           ', 'Transportation Equipment                                 ', 'Electric Equipment and Machinery                         ', 'Electronic and Telecommunications Equipment              ', 'Instruments, Meters, Cultural and Office Machinery         ', 'Other Manufacturing Industry                             ', 'Scrap and waste', 'Production and Supply of Electric Power, Steam and Hot Water   ', 'Production and Supply of Gas                    ', 'Production and Supply of Tap Water                       ', 'Construction                                             ', 'Transportation, Storage, Post and Telecommunication Services    ', 'Wholesale, Retail Trade and Catering Services            ', 'Others  ', 'Urban', 'Rural']
        if CO2_industry in self.CO2_industries:
            self.CO2_industry=CO2_industry
        else:
            print('Industry parameter Wrong!')
            return None     
        self.year=year
    def data_process(self):
        """
        通过数据的读取和处理，返回存有标题、地区、以及对于碳排放数值的列表
        """
        Analysis_title='SpaceAnalysis in {}, {} of {}'.format(self.year,self.CO2_type,self.CO2_industry)
        results=[Analysis_title,[i for i in self.regions]]#Analysis title,[xlabel],.append([data])
        result=[]
        wb=xlrd.open_workbook("Province sectoral CO2 emissions {}.xlsx".format(self.year))
        for i in self.regions:
            ws=wb.sheet_by_name(i)
            for k in range(ws.nrows):
                if ws.row_values(0)[k]==self.CO2_type:
                    break
            for j in range(ws.ncols):
                if ws.col_values(0)[j]==self.CO2_industry:
                    break
            value=ws.col_values(k)[j]
            if value==float('nan'):
                raise NotNumError(self.year,i,self.CO2_industry,self.CO2_type)
            elif value==0:
                results[1].remove(i)
                raise ZeroDivisonError(self.year,i,self.CO2_industry,self.CO2_type)
            else:
                result.append(value)
        results.append(result)
        return results
class VisualResults:
    """
    基于matplotlib库，根据上述两类返回的参数对分析结果进行可视化
    """
    def __init__(self,results):
        self.title=results[0]
        self.label=results[1]
        self.result=results[2]
        self.visualization()
    def visualization(self):
        """
        时间分析用条形图，空间分析用饼图
        """
        if self.title.split(' ')[0]=='SpaceAnalysis':
            plt.pie(self.result,labels=self.label)
            plt.title(self.title)
            plt.legend()
            plt.show()
        if self.title.split(' ')[0]=='TimeAnalysis':
            plt.bar(self.label,self.result)
            plt.title(self.title)
            plt.show()
class NotNumError(ValueError):
    """
    对数据进行检测，抛出异常
    """
    def __init__(self,year,region,industry,CO2_type):
        self.year=year
        self.region=region
        self.industry=industry
        self.CO2_type=CO2_type
        self.message="The data in {}, {} of {}, in {} is not a number!".format(self.region,self.CO2_type,self.industry,self.year)
        print("NotNumError:"+self.message)        
class ZeroDivisonError(Exception):
    """
    计算比例时，若总量为0则抛出异常
    """
    def __init__(self,year,region,industry,CO2_type):
        self.year=year
        self.region=region
        self.industry=industry
        self.CO2_type=CO2_type
        self.message="The data in {}, {} of {}, in {} is zero!".format(self.region,self.CO2_type,self.industry,self.year)
        print("ZeroDivisonError:"+self.message)
if __name__=='__main__':
    rs=['Sum', 'Beijing', 'Tianjin', 'Hebei', 'Shanxi', 'InnerMongolia', 'Liaoning', 'Jilin', 'Heilongjiang', 'Shanghai', 'Jiangsu', 'Zhejiang', 'Anhui', 'Fujian', 'Jiangxi', 'Shandong', 'Henan', 'Hubei', 'Hunan', 'Guangdong', 'Guangxi', 'Hainan', 'Chongqing', 'Sichuan', 'Guizhou', 'Yunnan', 'Shaanxi', 'Gansu', 'Qinghai', 'Ningxia', 'Xinjiang']
    C_t=['Raw Coal', 'Cleaned Coal', 'Other Washed Coal', 'Briquettes', 'Coke', 'Coke Oven Gas', 'Other Gas', 'Other Coking Products', 'Crude Oil', 'Gasoline', 'Kerosene', 'Diesel Oil', 'Fuel Oil', 'LPG', 'Refinery Gas', 'Other Petroleum Products', 'Natural Gas', 'Process', 'Total']
    C_i=['Total Consumption', 'Farming, Forestry, Animal Husbandry, Fishery and Water Conservancy      ', 'Coal Mining and Dressing                                 ', 'Petroleum and Natural Gas Extraction                     ', 'Ferrous Metals Mining and Dressing                       ', 'Nonferrous Metals Mining and Dressing                    ', 'Nonmetal Minerals Mining and Dressing                    ', 'Other Minerals Mining and Dressing                       ', 'Logging and Transport of Wood and Bamboo                 ', 'Food Processing                                          ', 'Food Production ', 'Beverage Production', 'Tobacco Processing                                       ', 'Textile Industry               ', 'Garments and Other Fiber Products                        ', 'Leather, Furs, Down and Related Products      ', 'Timber Processing, Bamboo, Cane, Palm Fiber & Straw Products', 'Furniture Manufacturing', 'Papermaking and Paper Products                           ', 'Printing and Record Medium Reproduction                  ', 'Cultural, Educational and Sports Articles                ', 'Petroleum Processing and Coking                          ', 'Raw Chemical Materials and Chemical Products             ', 'Medical and Pharmaceutical Products                      ', 'Chemical Fiber                                  ', 'Rubber Products                                          ', 'Plastic Products                         ', 'Nonmetal Mineral Products                                ', 'Smelting and Pressing of Ferrous Metals                  ', 'Smelting and Pressing of Nonferrous Metals               ', 'Metal Products                                           ', 'Ordinary Machinery', 'Equipment for Special Purposes                           ', 'Transportation Equipment                                 ', 'Electric Equipment and Machinery                         ', 'Electronic and Telecommunications Equipment              ', 'Instruments, Meters, Cultural and Office Machinery         ', 'Other Manufacturing Industry                             ', 'Scrap and waste', 'Production and Supply of Electric Power, Steam and Hot Water   ', 'Production and Supply of Gas                    ', 'Production and Supply of Tap Water                       ', 'Construction                                             ', 'Transportation, Storage, Post and Telecommunication Services    ', 'Wholesale, Retail Trade and Catering Services            ', 'Others  ', 'Urban', 'Rural']
    random.shuffle(rs)
    random.shuffle(C_t)
    random.shuffle(C_i)
    A=TimeAnalysis(rs[0],C_t[0],C_i[0])
    try:
        VisualResults(A.data_process())
    except NotNumError as n:
        print(n.message)
    B=SpaceAnalysis(C_t[1],C_i[1])
    try:
        VisualResults(B.data_process())
    except NotNumError as n:
        print(n.message)
    except ZeroDivisionError as z:
        print(z.message)