from celery import task


@task
def add(a, b):
    print('执行加函数')
    return a+b
