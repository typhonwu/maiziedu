from django.db import models

# Create your models here.
class Tag(models.Model):
	name = models.CharFiels(max_length = 30,verbose_name='标签名称')

	#方便在admin中查看名字
    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name
        ordering = ['id']

    #调用时返回自身的一些属性，注意python3用这个，python2用__unicode__
    def __str__(self):
    	#必须返回字符串类型，str(self.id)
        return self.name

# 文章分类
class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name='分类名称')
    #排序属性
    index = models.IntegerField('显示顺序(从小到大)',default=999,verbose_name='分类的排序')

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name
        #按照index和id属性排序
        ordering = ['index', 'id']

    def __unicode__(self):
        return self.name