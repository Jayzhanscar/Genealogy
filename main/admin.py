from django.contrib import admin
from main.models import User, Admin, Jiaxun, IMG, Lineage, MiContent
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'father_id', 'generation', 'line', 'sex', 'content', 'device_create_date')

    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 50

    # ordering设置默认排序字段，负号表示降序排序
    ordering = ('device_create_date',)

    # fk_fields 设置显示外键字段
    # fk_fields = ('user',)

    # list_editable 设置默认可编辑字段
    # list_editable = ['title']

    # 设置哪些字段可以点击进入编辑界面
    list_display_links = ('id', 'name', 'father_id', 'generation', 'line', 'sex', 'content', 'device_create_date')

    list_filter = ('name', 'father_id')  # 过滤器
    search_fields = ('name', 'father_id', 'generation', 'line')  # 搜索字段
    # date_hierarchy = 'create_date'  # 详细时间分层筛选　


class JiaxunAdmin(admin.ModelAdmin):
    """
    家谱
    """
    list_display = ('id', 'chapter', 'content', 'create_time')
    list_display_links = ('id', 'chapter', 'create_time')


class IMGAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'img')

    list_per_page = 10

    list_display_links = ('name', 'img')


class MiContentAdmin(admin.ModelAdmin):
    """
    修谱记叙章节
    """
    list_display = ('id', 'chapter', 'content', 'create_time')

    list_per_page = 10

    list_display_links = ('id', 'chapter')


class LineageAdmin(admin.ModelAdmin):
    """
    世系分行字图
    """
    list_display = ('id', 'img', 'content', 'create_time')

    list_per_page = 20

    list_display_links = ('id', 'img', 'content', 'create_time')

admin.site.register(User, UserAdmin),
admin.site.register(MiContent, MiContentAdmin)
admin.site.register(Lineage, LineageAdmin)
admin.site.register(Jiaxun, JiaxunAdmin),
admin.site.register(IMG, IMGAdmin),
admin.site.site_header = '吴氏家族'
admin.site.site_title = '后台管理'
