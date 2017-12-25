# _*_ coding:utf-8 _*_
__author__ = 'Rita'
__date__ = '2017/12/18 10:24'

import xadmin
from xadmin.views import BaseAdminPlugin,ListAdminView
from django.template import loader

# excel 导入功能
class ListImportExcelPlugin(BaseAdminPlugin):
    import_excel = False

    def init_request(self, *args, **kwargs):
        return bool(self.import_excel) #返回True才加载插件

    def block_top_toolbar(self, context, nodes):  # 显示自己的html文件
        nodes.append(loader.render_to_string('xadmin/excel/model_list.top_toolbar.import.html', context_instance=context))


xadmin.site.register_plugin(ListImportExcelPlugin, ListAdminView)