class Contact:
    """
    包括联系人编号，姓名，电话，邮件，头像等属性，以及更新属性，获取属性的方法
    """
    No_contact=0
    def __init__(self,num,name,email,Profile_photo):
        self.num=Contact.No_contact
        self.name=name
        self.email=email
        self.Profile_photo=Profile_photo
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
    def update_email(self,Nemail):
        """
        更新联系人电子邮件
        """
        if Nemail==self.email:
            print('The contact email has already been this!')
        else:
            self.email=Nemail
            print('The contact eamil has been changed to {}.'.format(Nemail))
    def update_Profile_photo(self,NProfile_photo):
        """
        更新联系人头像
        """
        if NProfile_photo==self.Profile_photo:
            print("The contact's photo has already been this!")
        else:
            self.Profile_photo=NProfile_photo
            print('The contact eamil has been changed to {}.'.format(NProfile_photo))        
class Profile_photo:
    """
    包含图片路径，长，宽等属性，以及更新属性，获取属性的方法
    """
    def __init__(self,path,length,width):
        self.path=path
        self.length=length
        self.width=width
class Note(self,ab,c):
    """
    包含联系人数目，联系人列表（包含联系人加入时间，更新时间）等属性，以及加入新联系人（注意重复的电话或邮件不应加入），更新联系人（如果不存在应该提醒），搜索联系人（可按姓名，电话，邮件来分别搜索），联系人排序输出（可按姓名，电话，邮件来进行升降序排列）等行为
    """
    def __init__(self):
        pass
class Unit_test(self,Contact,c):
    """
    进行测试，建立通信簿并进行各类操作
    """