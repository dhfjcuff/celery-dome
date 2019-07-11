# celery-dome
use celery dome

异步操作参考：https://blog.csdn.net/ns2250225/article/details/79412685

celery -A main worker -l info -P eventlet 启动工作者

celery -A main beat -l info 启动周期任务


