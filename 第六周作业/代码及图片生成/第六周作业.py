from PIL import Image
from PIL import ImageColor
from PIL import ImageFilter
from PIL import ImageEnhance
import matplotlib.pyplot as plt
import os
import math

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
    def filter(self,light_num):
        image=self.image
        return ImageEnhance.Brightness(image).enhance(light_num)
class ImageShp(Filter):
    """
    借助ImageEnhance模块实现锐化/模糊化图形操作
    """
    def filter(self,sharpeness_num):
        """
        由于模糊度和锐化度的指标上（下）限分别为0.0和2.0，合并为一行代码
        """
        image=self.image
        return ImageEnhance.Sharpness(image).enhance(sharpeness_num)
class ImageCol(Filter):
    """
    借助ImageEnhance模块实现图形调色功能
    """
    def filter(self,color_num):
        image=self.image
        return ImageEnhance.Color(image).enhance(color_num)
class ImageControl(Filter):
    """
    借助Image模块实现图形的合并等控制
    """
    def blend(self,image_1,image_2,blend_num,C=True):
        """
        默认以图片1的尺寸为最终合并尺寸，如果参数为False则以图片2的尺寸为合并尺寸，同时需要输入混合度参数
        """
        if C:
            temp=image_2.resize(image_1.size)
            return Image.blend(image_1,temp,blend_num)
        else:
            temp=image_1.resize(image_2.size)
            return Image.blend(temp,image_2,blend_num)
    def paste(self,image_1,paste_image,position=(0,0)):
        image_1.paste(paste_image,position)
        return image_1
class ImageEdge(Filter):
    """
    借助ImageFilter模块找图片的边缘
    """
    def filter(self):
        image=self.image
        return image.filter(ImageFilter.FIND_EDGES())
class ImageResize(Filter):
    def filter(self,size_tuple):
        image=self.image
        return image.resize(size_tuple)
class ImageShop:
    """
    生成以上Filter类的子类，对图片进行批处理
    """
    def __init__(self,pro_filter):
        self.imlist=[]#用以存储Image实例
        self.pathlist=[]#用以存储图片文件的目录
        self.imformat=['.bmp','.jpg','.png','.tif','.tiff','.jpeg','.gif','.tga','.ico','.cdr,','.ai','.wmf','.eps']#用以存储图片文件的格式
        self.pimlist=[]#用以存储处理过的Image实例
        self.pro_filter=pro_filter
        self.name=str()
        self.mutiplist=[]#用以存储多参数filter处理后的Image实例
    def load_image(self,path):
        return Image.open(path)
    def load_images(self,path=".."):
        pre=os.listdir(path)#预读取文件名
        for i in pre:
            if os.path.splitext(i)[1] in self.imformat:
                self.pathlist.append('../'+i)
        for j in self.pathlist:
            self.imlist.append(Image.open(j))
    def __batch_ps(self,one_filter):
        """
        根据filter操作名生成相应的子类进行操作，是一个批处理方法，因而排除了以上的ImageControl类
        """
        if self.imlist==[]:
            self.load_images()
        p_images=[]
        if one_filter=='Lig':
            print("Please input a lightness degree(0~1):")
            light_num=float(input())
            self.name='{}Lig_by_{}'.format(self.name,light_num)
            for image in self.imlist:
                p_images.append(ImageLig(image).filter(light_num))
        elif one_filter=='Shp':
            print("Please input a sharpness degree(0~2,0 for the most bur image, 2 for the most sharp image):")
            sharpness_num=float(input())
            self.name='{}Shp_by_{}'.format(self.name,sharpness_num)
            for image in self.imlist:
                p_images.append(ImageShp(image).filter(sharpness_num))
        elif one_filter=='Col':
            print("Please input a color degree(0~1,0 for the black-and-white image, 1 for the original image):")
            color_num=float(input())
            self.name='{}Col_by_{}'.format(self.name,color_num)
            for image in self.imlist:
                p_images.append(ImageCol(image).filter(color_num))
        elif one_filter=='Edge':
            self.name="{}Edge".format(self.name)
            for image in self.imlist:
                p_images.append(ImageEdge(image).filter())
        elif one_filter=='Resize':
            print("Please input new width and height of the image(example:width,height):")
            x,y=map(int,input().split(','))
            size_tuple=(x,y)
            self.name='{}Resize_by_({},{})'.format(self.name,x,y)
            for image in self.imlist:
                p_images.append(ImageResize(image).filter(size_tuple))
        else:
            print('Attributor Error!')
            return None
        return p_images          
    def batch_ps(self,*filters):
        """
        对外显示的图片处理方式，接受多个参数，返回一个包含所有多次处理后Image实例的列表
        """
        for i in filters:
            j=self.__batch_ps(i)
            if j!=None:
                self.imlist=j
        return self.imlist
    def image_control(self,im1,im2):
        """
        对ImageControl类进行单独处理、显示、保存
        """
        print('Please input the degree of blending(0~1):')
        blend_num=float(input())
        result1=ImageControl(image=im1).blend(im1,im2,blend_num)
        result2=ImageControl(image=im2).blend(im1,im2,blend_num,False)
        result3=ImageControl(image=im1).paste(im1,im2)
        result4=ImageControl(image=im2).paste(im2,im1)
        plt.subplot(2,2,1)
        plt.imshow(result1)
        plt.subplot(2,2,2)
        plt.imshow(result2)
        plt.subplot(2,2,3)
        plt.imshow(result3)
        plt.subplot(2,2,4)
        plt.imshow(result4)
        plt.title('Contorlled images')
        plt.show()
        result1.save('result1.jpg')
        result2.save('result2.jpg')
        result3.save('result3.jpg')
        result4.save('result4.jpg')
    def display(self,images=[]):
        """
        对图形进行展示，如不输入包含Image实例的列表，则按照默认情况读取图片进行单因素处理
        """
        if images==[]:
            one_filter=self.pro_filter
            self.pimlist=self.__batch_ps(one_filter)#多写一步，便于保存函数save_result的运行
            p_images=self.pimlist
        elif len(images)>=1 and isinstance(images,list):
            self.pimlist=images#方便调用save_result函数的操作
            p_images=images
        else:
            print("Attributor error!")
            return None
        row_num=math.floor(len(p_images)**0.5)+1#尽量以正方形排布，故开根号后向上取整，作为绘图的行列数
        for i in range(len(p_images)):
            plt.subplot(row_num,row_num,i+1)
            plt.imshow(p_images[i])
        plt.show()
    def save_result(self):
        for i in range(len(self.pimlist)):
            self.pimlist[i].save('{}_{}.jpg'.format(self.name,i+1))
class TestImageShop:
    """
    测试类，对ImageShop的方法进行测试
    """
    def __init__(self):
        A=ImageShop('Lig')
        A.display()
        A.save_result()
        B=ImageShop('Shp')
        B.display()
        B.save_result()
        C=ImageShop('Col')
        C.display()
        C.save_result()
        D=ImageShop('Edge')
        D.display()
        D.save_result()
        E=ImageShop(' ')
        E1=E.load_image('../6.jpg')
        E2=E.load_image('../20.jpg')
        E.image_control(E1,E2)
        F=ImageShop('Shp')#锐化和钝化各试一次
        F.display()
        F.save_result()
        G=ImageShop('Resize')
        G.display()
        G.save_result()
        H=ImageShop(' ')
        H1=H.batch_ps('Lig','Col')
        H.display(H1)
        H.save_result()
        I=ImageShop(' ')
        I1=I.batch_ps('Edge','Shp')
        I.display(I1)
        I.save_result()
if __name__=='__main__':One_test=TestImageShop()