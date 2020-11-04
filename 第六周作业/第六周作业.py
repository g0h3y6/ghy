from PIL import Image
from PIL import ImageColor
from PIL import ImageFilter
from PIL import ImageEnhance
import matplotlib.pyplot as plt
class Filter:
    def __init__(self,image,*args):
        """
        进行初始化，引入图片和其他参量，图片为Image类的对象
        """
        self.image=image#使用相对路径，此处保存的是文件名
        self.args=args#可用参数，因各个子类的方法而异
    def filter(self):
        """
        不要求细化，等后续子类进行继承，然后改写
        """
        pass
class ImageLig(Filter):
    """
    借助ImageEnhance模块实现调整图形亮度操作
    """
    def __init__(self,image,*args):
        Filter.__init__(image,*args)
    def filter(self,image,light_num):
        return ImageEnhance.Brightness(image).enhance(light_num)
class ImageShp(Filter):
    """
    借助ImageFilter模块实现锐化/模糊化图形操作
    """
    def __init__(self,image,*args):
        Filter.__init__(image,*args)
    def filter(self,image,C=True):
        if C:
            return ImageEnhance(image)
class ImageCol(Filter):
    """
    借助ImageEnhance模块实现图形调色功能
    """
    def __init__(self,image,*args):
        Filter.__init__(image,*args)
class ImageControl(Filter):
    """
    借助Image模块实现图形的合并等控制
    """
    def __init__(self,image,*args):
        Filter.__init__(image,*args)
class ImageShop:
    def __init__(self):
        self.imlist=[]#用以存储Image实例
        self.pathlist=[]#用以存储图片文件的目录
        self.imformat=[]#用以存储图片文件的格式
        self.pimlist=[]#用以存储处理过的Image实例
    def load_images(self):
        pass
    def __batch_ps(self,filter):
        """
        根据filter操作名生成相应的子类进行操作，是一个批处理方法
        """
        pass
    def display(self,row,column):
        """
        依照输入的行列参数对图形进行展示
        """
        self.__batch_ps()
        plt.subplot()
    def save_result(self):
        pass
class TestImageShop:
    """
    测试类，对ImageShop的方法进行测试
    """

if __name__=='__main__':One_test=TestImageShop()