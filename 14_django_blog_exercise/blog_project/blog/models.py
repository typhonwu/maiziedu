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
