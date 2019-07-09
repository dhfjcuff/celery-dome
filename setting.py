CELERY_BROKER_URL = 'redis://auth:password@ip:6379/0'
CELERY_RESULT_BACKEND = 'redis://auth:password@ip:6379/0'
force = True  # 很重要，没有的话不会加载settin.py中的部分配置
CELERYD_ACKS_LATE = True  # 设置失败允许重试
CELERYD_TASK_TIME_LIMIT = 5  # 单个任务的最大运行时间，超时会被杀死
CELERYD_CONCURRENCY = 3  # 设置并发的worker数量

CELERY_BEAT_SCHEDULE = {
    # 周期性任务
    'task-one': {
        'task': 'dome.tasks.add',
        'schedule': 10,  # 每天执行一次
        'args': (1, 2)
    },

}