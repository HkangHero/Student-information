from django.db import models

#学生信息
class Students(models.Model):
    student_id=models.CharField(max_length=12,primary_key=True) #账号
    name=models.CharField(max_length=16) #姓名
    photo=models.CharField(default=None,max_length=200,null=True) #照片
    college=models.CharField(max_length=30,null=True) #学院
    major=models.CharField(max_length=20,null=True) #专业
    phone_number=models.CharField(max_length=11,null=True)#手机号码 
    idCard=models.CharField(max_length=19,null=True)#身份证号码
    power=models.CharField(max_length=2,default=0)#该学生是否有权利查看义工审核情况
    student_token=models.CharField(max_length=300,default=None)#缓冲token
    password=models.CharField(max_length=20)#用户密码
    Pass=models.CharField(max_length=10,default='未审核')#义工是否审核
class Teacher(models.Model):
    teacher_id=models.CharField(max_length=12,primary_key=True) #老师id
    teacher_name=models.CharField(max_length=16) #姓名
    teacher_work=models.CharField(max_length=10,null=True)#负责实验室/图书馆
    teacher_token=models.CharField(max_length=300)#缓冲token
class VoluntaryLabor(models.Model):
    ud=models.AutoField(primary_key=True)#编号
    work_id=models.CharField(max_length=12)#学生号
    teacher_id=models.CharField(max_length=12)#老师号
    date=models.CharField(max_length=10) #日期
    time=models.IntegerField()#义工时间
    addres=models.CharField(max_length=30) #实验室/还是图书馆

class Master(models.Model):
    username=models.CharField(max_length=12,primary_key=True)#账号
    password=models.CharField(max_length=20)#密码



#state =peopl 的时候
class bill(models.Model):
    ud=models.AutoField(primary_key=True)#编号
    title=models.CharField(max_length=20)#标题 /打扫还是干啥 老师自己写
    demand=models.CharField(max_length=20,default='无要求')#男/女/无要求
    time=models.CharField(max_length=35) #准确日期
    work_tepy=models.CharField(max_length=10) #实验室/图书馆
    work_time=models.CharField(max_length=6)#工作几小时
    teacher_name=models.CharField(max_length=20)#老师姓名
    Impatient=models.CharField(max_length=10,default='普')#是否着急
    photos=models.CharField(max_length=10)#哪栋楼
    address=models.CharField(max_length=30)#详细地点
    phone_number=models.CharField(max_length=15)#手机号 联系方式
    state=models.IntegerField(default=0)#完成一个人 就加一 为的是可以在凌晨之前删除订单
    number_peoplr=models.IntegerField(default=0)# 报名人数
    peoples=models.IntegerField() #需要多少学生
    
class Cash(models.Model):
    ud=models.AutoField(primary_key=True)
    cid=models.CharField(max_length=5)#bill的ud
    student_id=models.CharField(max_length=16)#学号的id
    pass_time=models.CharField(max_length=20,default=None)#时间 方便删除
    