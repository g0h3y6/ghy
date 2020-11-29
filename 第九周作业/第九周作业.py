import random
from collections.abc import Iterable
from PIL import Image
import numpy as np
import os
def random_walk(mu,X,sigma,N):
    for i in range(N):
        w_t=random.normalvariate(0,sigma)
        X=X+w_t+mu
        yield X
class FaceDataset:
    """
    利用迭代器实现图片数据的加载
    """
    def __init__(self,path='./Images'):
        self.path=path
        self.path_list=os.listdir(path)
        self.__max=len(self.path_list)
        self.i=0
    def __next__(self):
        if self.i<=self.__max-1:
            I=Image.open("{}/{}".format(self.path,self.path_list[self.i]))
            self.i+=1
            return np.array(I)
        else:
            raise StopIteration("该目录下的图片已经读取完毕！")
    def __iter__(self):
        return self
def main():
    #1、测试随机游走的封装
    print("请输入随机游走序列的均值，初值，标准差，变量数目，序列个数：")
    mu,X,sigma,N,n=map(str,input().split(' '))
    X,N,n=map(int,(X,N,n))
    mu,sigma=map(float,(mu,sigma))
    A=zip(*[random_walk(mu,sigma,X,N) for i in range(n)])
    for i in A:
        for j in i:
            print(j,end=' ')
        print('')
    #2、测试迭代器读取图片
    test_i=FaceDataset()
    j=0
    for i in test_i:
        j+=1
        print(j)
        continue
    if j==len(test_i.path_list):
        print('Finished!')
if __name__=="__main__":main()