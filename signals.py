from django.dispatch import Signal

# signal sent when users successfully recover their passwords
#     user_recovers_password = Signal(
# TypeError: __init__() got an unexpected keyword argument 'providing_args'

# Django 弃用了在 Django 3.1 中使用 providing_args 参数到 django.dispatch.Signal 的能力。请参阅 3.1 发行说明的 杂项部分 中的项目符号。
#它被删除是因为这个参数除了作为文档之外没有做任何事情。如果这看起来很奇怪，那是因为它很奇怪。参数应指示数据已通过。这可能就是它被弃用的原因。
#user_recovers_password = Signal(
#    providing_args=['user', 'request']
#)

user_recovers_password = Signal(
    ['user', 'request']
)