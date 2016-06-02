'''
模版是一个用django模版语言标记过的python字符串。模版可以包含模版标签和变量。
模版标签是在一个模版里起作用的标记。比如，一个模版标签可以产生控制结构的内容(if或者for)，可以获取数据库内容或者访问其它模版标签。
一个标签块被{%%}包围
变量标签被{{}}包围
context是一个传递给模版的key-value对。
模版渲染是通过从context获取值来替换模版中变量并执行所有的模版标签。

'''
from django import template
from datetime import datetime
# 用来注册自定义标签
register = template.Library()


class AllenDateNode(template.Node):
	# 初始化日期格式
	def __init__(self, format_string):
		self.format_string = format_string

	# 自定义标签主要就是实现这个函数
	def render(self,context):
		return datetime.now().strftime(self.format_string)

# 创建编译函数，主要用于获取模板中的参数，并实例化相应的标签类


# 可以直接用装饰器注册，如果把name参数去掉，那就默认注册为函数名
@register.tag
def dateAllen(parse,token):
	try:
		# 解析传入的token
		tagname,format_string = token.split_contents()
	except ValueError:
		raise TemplateSyntaxError("invalid args")
	# 最后返回我们自定义的标签类,最后的节选是为了去掉模板渲染中两边的引号
	return AllenDateNode(format_string[1:-1])
# 最后注册一下自定义标签
# register.tag(name="dateAllen",compile_function=dateAllen)