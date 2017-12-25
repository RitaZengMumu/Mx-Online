# _*_ coding:utf-8 _*_
__author__ = 'Rita'
__date__ = '2017/5/31 20:25'

import xadmin
from .models import Course,Lesson,Video,CourseResource,BannerCourse
from organization.models import CourseOrg

class LessonInline(object):
    model = Lesson
    extra = 0


class CourseResourceInline(object):
    model = CourseResource
    extra = 0


class CourseAdmin(object):
    list_display = ['name','desc','detail','degree','learn_times','students','fav_nums','image','click_nums','add_time',
                    'get_zj_nums','go_to']
    search_fields = ['name','desc','detail','degree','learn_times','students','fav_nums','image','click_nums']
    list_filter = ['name','desc','detail','degree','learn_times','students','fav_nums','image','click_nums','add_time']
    readonly_field = ['click_nums','students']
    list_editable = ['desc','detail','degree']
    inlines = [LessonInline, CourseResourceInline]
    style_fields = {"detail": "ueditor"}  # style_fields 指明某个字段，采用的样式是什么，这里表示 detail这个字段采用 ueditor样式
    import_excel = True
    refresh_times = [3,5]

    def queryset(self):
        qs = super(CourseAdmin,self).queryset()
        qs = qs.filter(is_banner=True)
        return qs

    def save_models(self):
        # save the courses nums of orgnazition when save the course
        obj = self.new_obj
        obj.save()
        if obj.course_org is not None:
            course_org = obj.course_org
            course_org.course_nums = Course.objects.filter(course_org = course_org).count()
            course_org.save()

    def post(self, request, *args, **kwargs):
        if 'excel' in request.Files:
            pass
        return super(CourseAdmin, self).post(request, args, kwargs)



class BannerCourseAdmin(object):
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'image',
                    'click_nums', 'add_time']
    search_fields = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'image',
                     'click_nums']
    list_filter = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'image', 'click_nums',
                   'add_time']
    readonly_field = ['click_nums', 'students']
    inlines = [LessonInline, CourseResourceInline]

    def queryset(self):
        qs = super(BannerCourseAdmin,self).queryset()
        qs = qs.filter(is_banner=True)
        return qs


class LessonAdmin(object):
    list_display = ['course', 'name', 'add_time']
    search_fields = ['course', 'name', 'add_time']
    list_filter = ['course__name', 'name', 'add_time']


class VideoAdmin(object):
    list_display = ['lesson', 'name', 'add_time']
    search_fields = ['lesson', 'name']
    list_filter = ['lesson__name', 'name', 'add_time']


class CourseResourceAdmin(object):
    list_display = ['course', 'name','download', 'add_time']
    search_fields = ['course', 'name','download',]
    list_filter = ['course__name', 'name','download', 'add_time']


xadmin.site.register(Course,CourseAdmin)
xadmin.site.register(BannerCourse,BannerCourseAdmin)
xadmin.site.register(Lesson,LessonAdmin)
xadmin.site.register(Video,VideoAdmin)
xadmin.site.register(CourseResource,CourseResourceAdmin)