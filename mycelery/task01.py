import time
from mycelery.celery import cel

@cel.task
def send_email(res):
    print("发邮件")
    time.sleep(5)
    return "完成向%s发送邮件任务"%res