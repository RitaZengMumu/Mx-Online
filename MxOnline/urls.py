# _*_ encoding:utf-8 _*_
"""MxOnline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url,include,patterns
from django.contrib import admin
from django.views.generic import TemplateView
import xadmin
from django.views.static import serve  #处理静态文件的
from xadmin.plugins import xversion
from users.views import LoginView,RegisterView,ActiveUserView,ForgetPwdView,ResetView,ModifyPwdView,LogoutView,IndexView
from organization.views import OrgView
from MxOnline.settings import MEDIA_ROOT
# from MxOnline.settings import STATIC_ROOT



xversion.register_models()

urlpatterns = [
    url(r'^xadmin/', include(xadmin.site.urls),name='xadmin'),

    url('^$',IndexView.as_view(),name="index"),
url(r'^login/$',LoginView.as_view(),name="login"),
    url(r'^logout/$',LogoutView.as_view(),name="logout"),
    url(r'^register/$',RegisterView.as_view(),name="register"),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^active/(?P<active_code>.*)/$',ActiveUserView.as_view(),name="user_active"),
    url(r'^forget/$',ForgetPwdView.as_view(),name="forget_pwd"),
    url(r'^reset/(?P<active_code>.*)/$',ResetView.as_view(),name="reset_pwd"),
    url(r'^modify_pwd/$', ModifyPwdView.as_view(), name="modify_pwd"),
    url(r'^org_list/$', OrgView.as_view(), name="org_list"),#课程机构首页
    url(r'^media/(?P<path>.*)$', serve, {"document_root":MEDIA_ROOT}), #配置上传文件的处理函数
    # 当 settings 中的DEBUG = False，默认为生产环境，系统不会去自动取static的静态文件，需要配置static的url才能读取
    # url(r'^static/(?P<path>.*)$', serve, {"document_root":STATIC_ROOT}),

    url(r'^org/', include('organization.urls',namespace='org')),#课程机构Url配置
    url(r'^course/', include('courses.urls',namespace='course')),#课程相关Url配置

    url(r'^users/', include('users.urls', namespace='users')),  # 用户相关Url配置

    url(r'^ueditor/',include('DjangoUeditor.urls')), # ueditor 富文本编辑器插件

]

#全局404页面配置
handler404 = 'users.views.page_not_found'
handler500 = 'users.views.page_error'