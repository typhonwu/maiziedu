'''
作者模型：一个作者有姓名。
作者详情模型：把作者的详情放到详情表，包含性别、email
地址和出生日期，作者详情模型和作者模型之间是一对一的关系（OneToOneField）
出版商模型：出版商有名称，地址，所在城市、省，国家，网站。
书籍模型：书籍有书名和出版日期。
一本书可能会有多个作者，一个作者也可以写多本书，所以作者和书籍的关系是多对多的关联关系[many-to-many]，
一本书只应该由一个出版商出版，所以出版商和书籍是一对多的关联关系[one-to-many]，也被称作外键[ForeignKey]。
'''
from django.db import models

class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

class Author(models.Model):
    name = models.CharField(max_length=30)

class AuthorDetail(models.Model):
    sex = models.BooleanField(max_length=1, choices=((0, '男'),(1, '女'),))
    email = models.EmailField()
    address = models.CharField(max_length=50)
    birthday = models.DateField()
    author = models.OneToOneField(Author)

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()
