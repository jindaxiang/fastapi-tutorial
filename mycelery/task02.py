import time
from mycelery.celery import cel
@cel.task
def send_msg(name):
    print("发短信")
    time.sleep(5)
    return "完成向%s发送短信任务"%name