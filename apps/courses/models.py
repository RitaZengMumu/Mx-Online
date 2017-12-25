# _*_ encoding:utf-8 _*_


from __future__ import unicode_literals

from datetime import datetime

from django.db import models
from organization.models import CourseOrg,Teacher
from DjangoUeditor.models import UEditorField

# Create your models here.


class Course(models.Model):
    course_org = models.ForeignKey(CourseOrg,verbose_name=u"课程机构",null=True,blank=True)
    name = models.CharField(max_length=50,verbose_name=u"课程名")
    desc = models.CharField(max_length=300,verbose_name=u"课程描述")
    # detail = models.TextField(verbose_name=u"课程详情")
    detail = UEditorField(verbose_name=u'课程详情', width=600, height=300,
                          imagePath="courses/ueditor/", filePath="courses/ueditor/",default='')
    is_banner = models.BooleanField(default=False,verbose_name=u"是否轮播")
    teacher = models.ForeignKey(Teacher,verbose_name=u"授课讲师",null=True,blank=True)
    degree = models.CharField(max_length=10,choices=(("cj",u"初级"),("zj",u"中级"),("gj",u"高级")),verbose_name=u"难度")
    learn_times = models.IntegerField(default=0,verbose_name=u"学习时长数(分钟数)")
    students = models.IntegerField(default=0,verbose_name=u"学习人数")
    fav_nums = models.IntegerField(default=0,verbose_name=u"收藏人数")
    image = models.ImageField(upload_to="courses/%Y/%m",verbose_name=u"封面")
    click_nums = models.IntegerField(default=0,verbose_name=u"点击数")
    category = models.CharField(default=u"后端开发",max_length=20,verbose_name=u"课程类别")
    tag = models.CharField(default="",max_length=10,verbose_name=u"课程标签")
    youneed_know = models.CharField(default="", max_length=300, verbose_name=u"课程需知")
    teacher_tell = models.CharField(default="", max_length=300, verbose_name=u"老师告诉你")
    add_time = models.DateField(default=datetime.now,verbose_name=u"添加时间")

    class Meta:
        verbose_name=u"课程"
        verbose_name_plural = verbose_name

    def get_zj_nums(self):
        #获取课程章节数
       return self.lesson_set.all().count()  #当model有外键指向 course表的话，可以用set方法反向取指向表的项，再调用count方法取数目
    get_zj_nums.short_description = u"章节数"

    def go_to(self):
        from django.utils.safestring import mark_safe
        return mark_safe("<a href='http://www.baidu.com'>跳转</>")
    go_to.short_description = u"跳转"

    def get_learn_users(self):
        #获取学习课程的用户
       return self.usercourse_set.all()[:5]

    def get_course_lesson(self):
        #获取课程的章节
        return  self.lesson_set.all()


    def __unicode__(self):
        return self.name


class Lesson(models.Model):
    course = models.ForeignKey(Course,verbose_name=u"课程")
    name = models.CharField(max_length=100,verbose_name=u"章节名")
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"章节"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name

    def get_lesson_video(self):
        #获取课程的章节视频
        return  self.video_set.all()


class Video(models.Model):
    lesson = models.ForeignKey(Lesson,verbose_name=u"章节")
    name = models.CharField(max_length=100,verbose_name=u"视频名")
    learn_times = models.IntegerField(default=0,verbose_name=u"学习时长数(分钟数)")
    url = models.CharField(max_length=200,default="",verbose_name=u"访问地址")  # 这里url的数据类型也可以用UrlField类型
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"视频"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class CourseResource(models.Model):
    course = models.ForeignKey(Course,verbose_name=u"课程")
    name = models.CharField(max_length=100,verbose_name=u"名称")
    download = models.FileField(upload_to="course/resource/%Y/%m",verbose_name=u"资源文件",max_length=100)
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"课程资源"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class BannerCourse(Course):
    class Meta:
        verbose_name = u"轮播课程"
        verbose_name_plural = verbose_name
        proxy = True

