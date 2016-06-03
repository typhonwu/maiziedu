from django import template

register = template.Library()

# 定义一个过滤器用于去掉空格
def cut_filter(value, arg):
	return value.replace(arg, '')


# 注册这个自定义过滤器，名字可以随便起，主要是指定调用哪个函数
register.filter(name="cut_filter", filter_func=cut_filter)
