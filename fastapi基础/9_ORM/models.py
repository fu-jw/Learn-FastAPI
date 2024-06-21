"""
选课系统
"""
from tortoise.models import Model
from tortoise import fields


# 学生
class Student(Model):
    # id 整型，主键
    id = fields.IntField(pk=True)
    # name 字符串，最大长度32
    name = fields.CharField(max_length=32, description="学生姓名")
    pwd = fields.CharField(max_length=32, description="密码")
    sno = fields.IntField(description="学号")
    # 一对多关系，一个班级有多个学生
    clas = fields.ForeignKeyField("models.Clas", related_name="students")
    # 多对多关系，一个学生有多门课程，一门课程有多个学生
    course = fields.ManyToManyField("models.Course", related_name="students")


# 教师
class Teacher(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=32, description="教师名称")
    pwd = fields.CharField(max_length=32, description="密码")
    sno = fields.IntField(description="教师编号")


# 班级
class Clas(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=32, description="班级名称")


# 课程
class Course(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=32, description="课程名称")
    # 一对多，一门课程有多个教师
    teacher = fields.ForeignKeyField("models.Teacher", related_name="courses")
    # 添加一个新的字段
    addr = fields.CharField(max_length=32, description="教室", default="")
