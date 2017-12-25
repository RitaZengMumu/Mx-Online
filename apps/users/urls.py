# _*_ coding:utf-8 _*_
__author__ = 'Rita'
__date__ = '2017/12/3 10:58'


from django.conf.urls import url,include
from .views import UserinfoView,UploadImageView,UpdatePwdView,SendEmailView,UpdateEmailView,MyCourseView,MyFavOrgView
from .views import MyFavTeacherView,MyFavCourseView,MyMessageView

urlpatterns = [
    url(r'^info/$',UserinfoView.as_view(),name="user_info"),# 用户信息
    url(r'^image/upload/$',UploadImageView.as_view(),name="image_upload"),# 修改头像
    url(r'^update/pwd/$',UpdatePwdView.as_view(),name="update_pwd"), # 个人中心修改密码
    url(r'^sendemail_code/$', SendEmailView.as_view(), name="sendemail_code"),  # 邮箱发送验证码
    url(r'^update_email/$', UpdateEmailView.as_view(), name="update_email"), # 修改邮箱
    url(r'^mycourse/$', MyCourseView.as_view(), name="mycourse"), # 我的课程
    url(r'^myfav/org/$', MyFavOrgView.as_view(), name="myfav_org"),# 我收藏的机构
    url(r'^myfav/teacher/$', MyFavTeacherView.as_view(), name="myfav_teacher"),# 我收藏的讲师
    url(r'^myfav/course/$', MyFavCourseView.as_view(), name="myfav_course"),# 我收藏的课程
    url(r'^mymessage/$', MyMessageView.as_view(), name="mymessage"),# 我的消息
]