from line_profiler import LineProfiler
import time
from memory_profiler import profile
import os
from functools import wraps
from pygame import mixer
def wraps_path(path):
    def decorator(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            folder=os.path.exists(path)
            if not folder:
                print('The folder path "{}" does not exist! It is to be created.')
                os.makedirs(path)
            else:
                print('The folder path exists!')
            return func(*args,**kwargs)
        return wrapper
    return decorator
class Fib:
    """
    用递归生成斐波那契数列，耗时耗空间，以测试如下的装饰器
    """
    path='results'
    def __init__(self):
        self.nums=[]
        self.path='results'
    #@profile(precision=4)
    def time_consume(self,num):
        """
        使用非常耗时的算法求斐波那契数列
        """
        if num==1:
            return 1
        elif num==2:
            return 2
        else:
            return self.time_consume(num-1)+self.time_consume(num-2)
    @profile(precision=4)
    def space_consume(self,num):
        """
        使用非常耗空间的算法求斐波那契数列
        """
        self.nums=[0 for i in range(num)]
        for i in range(num):
            if i==0:
                self.nums[i]=1
            elif i==1:
                self.nums[i]=1
            else:
                self.nums[i]=self.nums[i-1]+self.nums[i-2]
        return self.nums[num-1]
    @wraps_path(path)
    def save_result(self,result):
        with open('./{}/result.txt'.format(Fib.path),'a',encoding='UTF-8') as w:
            w.write(str(result))
class Wrap_sound:
    """
    装饰器类，发送音乐通知
    """
    def __init__(self,sound='叮咚.mp3'):
        self.sound=sound
    def __call__(self,func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            mixer.init()
            mixer.music.load(self.sound)
            mixer.music.play()
            time.sleep(3)
            mixer.music.stop()
            return func(*args,**kwargs)
        return wrapper
def main():
    a=Fib()
    lp1=LineProfiler()
    a1=lp1(a.time_consume)
    a.save_result(a1(30))
    lp1.print_stats()
    print(a.space_consume(1000))
    return 1
@Wrap_sound()
def end_judge(num):
    return None
if __name__=="__main__":
    end=main()
    end_judge(end)