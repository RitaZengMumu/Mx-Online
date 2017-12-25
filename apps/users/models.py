# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50,verbose_name="昵称",default="")
    birthday = models.DateField(verbose_name="生日",null=True,blank = True)
    gender = models.CharField(max_length=6,choices=(("male",u"男"),("female",u"女")),default="female")
    address = models.CharField(max_length=100,null=True,blank=True)
    mobile = models.CharField(max_length=11,null=True,blank=True)
    image = models.ImageField(upload_to="image/%Y/%m",default=u'image/default.png',max_length=100)

    USERNAME_FIELD = 'username'
    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username

    def get_unread_nums(self):
        #获取用户未读消息数量
        from operation.models import UserMessage  #这里import 需要放到这个方法里面，调用的时候才会import进来
        return UserMessage.objects.filter(user=self.id,has_read=False).count()




class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20,verbose_name=u"验证码")
    email = models.EmailField(max_length=50,verbose_name=u"邮箱")
    send_type = models.CharField(max_length=20,choices=(("register",u"注册"),("forget","找回密码"),("update_email", u"修改邮箱")),verbose_name=u"验证码类型")
    send_time = models.DateField(default=datetime.now,verbose_name=u"发送时间") #这里的datetime.now 后面不能加括号，如果加括号，获取的是当前编译的时间

    class Meta:
        verbose_name = u"邮箱验证码"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return '{0}({1})'.format(self.code,self.email)


class Banner(models.Model):
    title = models.CharField(max_length=100,verbose_name=u"标题")
    image = models.ImageField(upload_to="banner/%Y/%m",verbose_name=u"轮播图")
    url = models.URLField(max_length=200,verbose_name=u"访问地址")
    index = models.IntegerField(default=100,verbose_name=u"顺序")
    add_time =models.DateField(default=datetime.now,verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"轮播图"
        verbose_name_plural = verbose_name

