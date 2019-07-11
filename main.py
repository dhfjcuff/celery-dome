# from celery import Celery
from __future__ import absolute_import, unicode_literals
import setting
from celery import Celery
import time

# 我们这里案例使用redis作为broker
app = Celery('dome')  # 绑定app名字，名字随意无其他意义
app.config_from_object(setting, namespace='CELERY')  # 导入配置文件，并指明配置项的前缀

# 发现任务
# 1.指定tasks文件路径
app.autodiscover_tasks(['dome.tasks'])  # 自动发现函数


# 2.文件内定义
@app.task
def add(a, b):
    print('执行加函数')
    print('执行完加函数')
    return a + b
