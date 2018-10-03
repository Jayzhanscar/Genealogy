from django.db import models
import datetime
# Create your models here.


Sex_choices = (("男", '男'), ('女', '女'))
Shi_choices = (
    ('壹', '壹'),
    ('贰', '贰'),
    ('叁', '叁'),
    ('肆', '肆'),
    ('伍', '伍'),
    ('陆', '陆'),
    ('柒', '柒'),
    ('捌', '捌'),
    ('玖', '玖'),
    ('拾', '拾'),
    ('拾壹', '拾壹'),
('拾贰', '拾贰'),
('拾叁', '拾叁'),
('拾肆', '拾肆'),
('拾伍', '拾伍'),
('拾陆', '拾陆'),
('拾柒', '拾柒'),
('拾捌', '拾捌'),
('拾玖', '拾玖'),
('贰拾', '贰拾'),
            ('贰壹', '贰壹'),
    ('贰拾贰', '贰拾贰'),
    ('贰拾叁', '贰拾叁'),
    ('贰拾肆', '贰拾肆'),
    ('贰拾伍', '贰拾伍'),
    ('贰拾陆', '贰拾陆'),
    ('贰拾柒', '贰拾柒'),
    ('贰拾捌', '贰拾捌'),
    ('贰拾玖', '贰拾玖'),
    ('叁拾', '叁拾')
)
Hang_choices = (
    ('壹', '壹'),
    ('贰', '贰'),
    ('叁', '叁'),
    ('肆', '肆'),
    ('伍', '伍'),
    ('陆', '陆'),
    ('柒', '柒'),
    ('捌', '捌'),
    ('玖', '玖'),
    ('拾', '拾'),
    ('拾壹', '拾壹'),
('拾贰', '拾贰'),
('拾叁', '拾叁'),
('拾肆', '拾肆'),
('拾伍', '拾伍'),
('拾陆', '拾陆'),
('拾柒', '拾柒'),
('拾捌', '拾捌'),
('拾玖', '拾玖'),
('贰拾', '贰拾')
)


class User(models.Model):
    """
    吴氏家谱数据表
    """
    # 标签id

    # id = models.IntegerField( )
    id = models.AutoField(int, primary_key=True)
    # uuid = models.CharField(max_length=30, primary_key=True, default=True)

    # 用户名
    name = models.CharField(max_length=30, verbose_name='姓名')
    # father_id
    father_id = models.CharField(max_length=30, verbose_name='父名')
    # 世
    generation = models.CharField(max_length=10, verbose_name='世', choices=Shi_choices)
    # 行
    line = models.CharField(max_length=10, verbose_name='行', choices=Hang_choices)
    # 性别
    sex = models.CharField(max_length=5, verbose_name='性别', choices=Sex_choices)
    # 行字辈
    line_str = models.CharField(max_length=30, verbose_name='行字辈', null=True)
    # son 个数
    son_num = models.CharField(max_length=10, verbose_name="儿子个数", choices=Hang_choices, null=True)
    # girl num
    girl_num = models.CharField(max_length=10, verbose_name='女儿个数', choices=Hang_choices, null=True)
    # 房
    house = models.CharField(max_length=10, verbose_name='房', choices=Hang_choices, null=True)
    # 描述
    content = models.TextField(verbose_name='简介')
    # 创建时间
    device_create_date = models.DateTimeField(default=datetime.datetime.utcnow, db_column='user_create_date', verbose_name='创建时间')

    class Meta:

        app_label = 'main'
        db_table = "user"
        verbose_name_plural = '家族姓名'


class Admin(models.Model):
    """
    管理员账号管理
    """
    id = models.AutoField(primary_key=True)
    # 用户名
    name = models.CharField(max_length=100)
    # 密码
    password = models.CharField(max_length=300)

    class Meta:
        app_label = 'main'
        db_table = "admin"


class Jiaxun(models.Model):
    """
    家训管理表
    """
    id = models.AutoField(primary_key=True, verbose_name='唯一标识')
    # 章节数
    chapter = models.CharField(verbose_name='章节', max_length=30)
    # 具体内容
    content = models.TextField(verbose_name='具体内容')
    # 添加时间
    create_time = models.DateTimeField(default=datetime.datetime.utcnow, db_column='chapter_create_date', verbose_name='创建时间')

    class Meta:
        verbose_name_plural = '家训'


class IMG(models.Model):
    """
    圣旨跟祠堂照片文件保存
    """
    id = models.IntegerField(primary_key=True, verbose_name='唯一标识')
    # 图片保存路径
    img = models.ImageField(upload_to='img', verbose_name='图片文件(不超过3')
    # 图片名字 不超过20字节
    name = models.CharField(max_length=20, verbose_name='图片名字')

    class Meta:

        verbose_name_plural = '谱例'


class MiContent(models.Model):
    """
    修谱记叙章节
    """
    id = models.AutoField(primary_key=True, max_length=30)
    # 章节
    chapter = models.CharField(max_length=10)
    # 具体内容
    content = models.TextField(null=True)
    # 创建时间
    create_time = models.DateTimeField(default=datetime.datetime.utcnow, db_column='chapter_create_date',
                                       verbose_name='创建时间')

    class Meta:

        verbose_name_plural = '修谱记叙章节'


class Lineage(models.Model):
    """
    世系分行字图
    """
    id = models.AutoField(primary_key=True, max_length=30)
    # 图片文件
    img = models.ImageField(upload_to='img', verbose_name='图片文件(不超过3')
    # 文字描述
    content = models.TextField()
    # 创建时间
    create_time = models.DateTimeField(default=datetime.datetime.utcnow, db_column='chapter_create_date',
                                       verbose_name='创建时间')

    class Meta:
        verbose_name_plural = '世系分行字图'
