from django.db import models
import datetime
# Create your models here.


class User(models.Model):
    """
    吴氏家谱数据表
    """
    # 标签id
    id = models.IntegerField(primary_key=True)
    # 用户名
    name = models.CharField(max_length=30)
    # father_id
    father_id = models.CharField(max_length=30, default=0)
    # 世
    generation = models.CharField(max_length=10)
    # 行
    line = models.CharField(max_length=10)
    # 性别
    sex = models.CharField(max_length=5)
    # 描述
    content = models.CharField(max_length=1000)
    # 创建时间
    device_create_date = models.DateTimeField(default=datetime.datetime.utcnow, db_column='user_create_date')

    def __str__(self):
        return self.name, self.father_id, self.line

    class Meta:
        app_label = 'main'
        db_table = "user"


class Admin(models.Model):
    """
    管理员账号管理
    """
    id = models.IntegerField(primary_key=True)
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
    id = models.IntegerField(primary_key=True)
    # 章节数
    chapter = models.IntegerField()
    # 具体内容
    content = models.TextField()
    # 添加时间
    create_time = models.DateTimeField(default=datetime.datetime.utcnow, db_column='chapter_create_date')


class IMG(models.Model):
    """
    圣旨跟祠堂照片文件保存
    """
    id = models.IntegerField(primary_key=True)
    # 图片保存路径
    img = models.ImageField(upload_to='img')
    # 图片名字 不超过20字节
    name = models.CharField(max_length=20)