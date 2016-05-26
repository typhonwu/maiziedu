# -*- utf-8 -*-
from django.contrib import admin
from blog.models import *
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
	#决定哪些是展开显示，哪些合并在一起
	fieldsets = (
		#这些展开
		(None, {
				'fields': ('title','desc','content',)
			}
		),
		#这些默认合并
		('高级设置',{
				'classes':('collapse',),
				'fields':('click_count','is_recommend',)
			}
		),
	)

admin.site.register(User)
admin.site.register(Tag)
#改成自定义形式注册
admin.site.register(Article,ArticleAdmin)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Links)
admin.site.register(Ad)
