import matplotlib.pyplot as plt
import time as t
import os
import random
import re

class Contact:
    """
    包括联系人编号，姓名，电话，邮件，头像等属性，以及更新属性，获取属性的方法
    """
    No_contact=0
    def __init__(self,name,phone_num,email,photo):
        self.num=Contact.No_contact
        self.name=name
        self.phone_num=phone_num
        self.email=email
        self.photo=photo
        self.update_time=t.time()
        Contact.No_contact+=1
    def update_name(self,Nname):
        """
        更新联系人姓名
        """
        if Nname==self.name:
            print('The contact name has already been this!')
        else:
            self.name=Nname
            print('The contact name has been changed to {}.'.format(Nname))
    def update_phone_num(self,Nphone_num):
        """
        更新联系人电话
        """
        if Nphone_num==self.phone_num:
            print('The contact phone number has already been this!')
        else:
            self.phone_num=Nphone_num
            self.update_time=t.time()
            print('The contact phone number has been changed to {}.'.format(Nphone_num))
    def update_email(self,Nemail):
        """
        更新联系人电子邮件
        """
        if Nemail==self.email:
            print('The contact email has already been this!')
        else:
            self.email=Nemail
            self.update_time=t.time()
            print('The contact eamil has been changed to {}.'.format(Nemail))
    def update_photo(self,NProfile_photo):
        """
        更新联系人头像
        """
        if NProfile_photo==self.photo:
            print("The contact's photo has already been this!")
        else:
            self.Profile_photo=photo
            self.update_time=t.time()
            print("The contact's photo path has been changed to {}.".format(NProfile_photo.path))        

class Profile_photo:
    """
    包含图片路径，长，宽等属性，以及更新属性，获取属性的方法
    """
    def __init__(self,path,length=10,width=10):
        self.path=path
        self.length=length
        self.width=width
    def update_path(self,Npath):
        """
        更新照路径
        """
        if Npath==self.path:
            print('The photo path has already been this!')
        else:
            self.path=Npath
            print('The photo path has been changed to {}.'.format(Npath))    
    def update_width(self,Nwidth):
        """
        更新照片宽度
        """
        if Nwidth==self.width:
            print('The photo width has already been this!')
        else:
            self.width=Nwidth
            print('The photo width name has been changed to {}.'.format(Nwidth))
    def update_length(self,Nlength):
        """
        更新照片长度
        """
        if Nlength==self.length:
            print('The photo length has already been this!')
        else:
            self.length=Nlength
            print('The photo has been changed to {}.'.format(Nlength))

class Note:
    """
    包含联系人数目，联系人列表（包含联系人加入时间，更新时间）等属性，以及加入新联系人（注意重复的电话或邮件不应加入），更新联系人（如果不存在应该提醒），搜索联系人（可按姓名，电话，邮件来分别搜索），联系人排序输出（可按姓名，电话，邮件来进行升降序排列）等行为
    """
    def __init__(self):
        self.C_list=[]
        self.email=[]
        self.phone_num=[]
        self.name=[]
    def add_contact(self,New_Contact):
        """
        添加新的联系人，并对联系人的更新时间进行更改，但是默认联系人可能出现重名、头像相同的情况所以不做相应的筛查
        """
        if New_Contact.email not in self.email and New_Contact.phone_num not in self.phone_num:
            self.C_list.append(New_Contact)
            self.email.append(New_Contact.email)
            self.phone_num.append(New_Contact.phone_num)
            self.name.append(New_Contact.name)
            New_Contact.update_time=t.time()
        else:
            print('Duplicate Contact information!')
    def update_contact(self,attr_s,item_s,attr,New_item):
        """
        按照联系人的属性进行更新，而不是更新整个联系人，依赖search_contact实现
        """
        c=self.search_contact(attr_s,item_s)
        if c!=None:
            for i in c:
                exec('i.{}=New_item'.format(attr))
    def search_contact(self,attr_s,item):
        """
        按照第一个参数进行索引，按照第二个参数进行查找
        """
        result=[]
        if attr_s not in ['name','phone_num','email']:
            print('Attributor ERROR!')
        else:
            for i in self.C_list:
                if attr_s=='name':
                    a=i.name
                if attr_s=='phone_num':
                    a=i.phone_num
                if attr_s=='email':
                    a=i.email
                if a==item:
                    result.append(i)
            if result!=[]:
                return result
            else:
                print('Can not find the contact subject to the given condition!')
    def sort_contact(self,attr,c=True):
        """
        按照选定的参数（姓名、电话、邮件）进行排序操作，可以选择降序排序和升序排序，默认为升序
        """
        if attr not in ['name','phone_num','email']:
            print('Attributor ERROR!')
        else:
            if c:
                if attr=='name':
                    a=self.name
                if attr=='phone_num':
                    a=self.phone_num
                if attr=='email':
                    a=self.email
                for j in range(len(a)-1):#升序排序
                    for i in range(len(a)-1-j):
                        if a[i]>a[i+1]:
                            a[i],a[i+1]=a[i+1],a[i]
                            self.C_list[i],self.C_list[i+1]=self.C_list[i+1],self.C_list[i]
                self.email=[self.C_list[i].email for i in range(len(self.C_list))]
                self.phone_num=[self.C_list[i].phone_num for i in range(len(self.C_list))]
                self.name=[self.C_list[i].name for i in range(len(self.C_list))]
            else:
                if attr=='name':
                    b=self.name
                if attr=='phone_num':
                    b=self.phone_num
                if attr=='email':
                    b=self.email
                for j in range(len(b)-1):#降序排序
                    for i in range(len(b)-1-j):
                        if b[i]<b[i+1]:
                            self.C_list[i],self.C_list[i+1]=self.C_list[i+1],self.C_list[i]
                self.email=[self.C_list[i].email for i in range(len(self.C_list))]
                self.phone_num=[self.C_list[i].phone_num for i in range(len(self.C_list))]
                self.name=[self.C_list[i].name for i in range(len(self.C_list))]
    def del_contact(self,attr_s,item):
        """
        根据搜索的参数值查找相应的联系人并删除，依赖search_contact实现
        """
        c=self.search_contact(attr_s,item)
        del_num=[]
        if c!=None:
            for i in range(len(self.C_list)):
                if self.C_list[i] in c:
                    del_num.append(i)
            for j in del_num:
                self.C_list.pop(j)
                self.phone_num.pop(j)
                self.email.pop(j)
                self.name.pop(j)
            print('{} contact(s) had been deleted.'.format(len(c)))
    def print_contact(self,contact):
        """
        依照联系人类打印联系人
        """
        print("NO.{}Contact\n Name:{}\n Phone number:{}\n Email:{}\n Update time:{}\n".format(contact.num,contact.name,contact.phone_num,contact.email,contact.update_time))
        plt.figure(figsize=(contact.photo.width,contact.photo.length))
        z=plt.imread(contact.photo.path)
        plt.imshow(z)
        plt.show()
    def print_note(self):
        """
        打印目前全部通讯录
        """
        for i in self.C_list:
            self.print_contact(i)

class Unit_test:
    """
    进行测试，建立通信簿并进行各类操作
    """
    def __init__(self,num):
        """
        依据随机生成的联系人个数测试
        """
        self.Note=Note()
        self.random_contact(num)
        while not self.input_contact():
            print('Failed to input!')
        self.Note.print_note()
        sample=self.Note.C_list[0]
        sample.photo.update_length(10)
        sample.photo.update_path(r"D:/Files/影音像文件/壁纸/桌面放映/1.jpg")
        sample.photo.update_width(8)
        sample.update_phone_num(13948240323)
        sample.update_email('Sdad@163.com')
        sample.update_photo(sample.photo)
        sample.update_name('Sdad')
        self.Note.print_note()
        self.Note.update_contact('name','Sdad','name','Ghy')
        self.Note.print_note()
        self.Note.del_contact('name','Ghy')
        self.Note.print_note()
        self.Note.sort_contact('name')
        self.Note.print_note()
        self.Note.sort_contact('email',False)
        self.Note.print_note()
        self.Note.sort_contact('phone_num',False)
        self.Note.print_note()
    def input_contact(self):
        """
        输入手动创建的联系人对象
        """
        print("Please input the Contact's name:")
        name=input()
        print("Please input the Contact's phone number:")
        phone_num=int(input())
        if phone_num<10000000000 or phone_num >20000000000 or not isinstance(phone_num,int):
            print('Invalid phone number!')
            return False
        print("Please input the Contact's email:")
        email=input()
        p=re.compile(r"[^@]+@[^@]+\.[^@]+")
        if not p.match(email):
            print('Invalid email!')
            return False
        print("Please input the path of Contact's photo:")
        photo_path=input()
        print("Please input the width of Contact's photo:(Default as 10)")
        photo_width=input()
        print("Please input the length of Contact's photo:(Default as 10)")              
        photo_length=input()
        if not isinstance(photo_width,float) or not isinstance(photo_length,float):
            p=Profile_photo(photo_path)
        else:
            p=Profile_photo(photo_path,photo_length,photo_width)
        self.Note.add_contact(Contact(name,phone_num,email,p))
        print('Add a new contact to note successfully!')
        return True
    def random_contact(self,num):
        """
        随机按照个数生成联系人并且导入通讯簿类
        """
        #指定文件夹的照片，将在这里随机选取头像
        photo_path="D:\Files\影音像文件\壁纸\桌面放映"
        photo_paths=[]
        for i in os.listdir(photo_path):
            photo_paths.append(os.path.join(photo_path,i))
        for j in range(num):
            phone_num=random.randint(10000000000,19999999999)
            name=str(chr(random.randint(65,90))+chr(random.randint(97,122))+chr(random.randint(97,122))+chr(random.randint(97,122)))
            email_temp=['{}@buaa.edu.cn'.format(name),'{}@qq.com'.format(name),'{}@163.com'.format(name),'{}@sohu.com'.format(name),'{}@pku.edu.cn'.format(name),'{}@thu.edu.cn'.format(name)]
            random.shuffle(email_temp)
            random.shuffle(photo_paths)
            self.Note.add_contact(Contact(name,phone_num,email_temp[0],Profile_photo(photo_paths[0])))

a=int(input())
Unit_test(a)