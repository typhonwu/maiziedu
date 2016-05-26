from django.contrib import admin
from blog.models import *
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
	#决定后台只显示哪些字段
	exclude = ('title','desc','content',)

admin.site.register(User)
admin.site.register(Tag)
#改成自定义形式注册
admin.site.register(Article,ArticleAdmin)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Links)
admin.site.register(Ad)
