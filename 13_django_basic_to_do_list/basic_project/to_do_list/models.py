from django.db import models

# Create your models here.
class Thing(models.Model):
    title = models.CharField(max_length=100,verbose_name="待办事项")
    class Meta:
        verbose_name = '待办事项'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.title
