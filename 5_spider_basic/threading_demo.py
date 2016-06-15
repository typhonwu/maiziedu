# -*- coding: utf-8 -*-
import threading
import random
import time

def worker_func():
    print('worker thread started in %s' % (threading.current_thread()))
    # 改变随机数生成器的种子
    random.seed()
    # 让线程睡眠s随机一段时间
    time.sleep(random.random())
    print('worker thread finished in %s' % (threading.current_thread()))

def simple_thread_demo():
    # 创建十个线程来进行测试
    for i in range(10):
        # 每个线程都执行worker_func这个方法，注意这里不需要带括号
        threading.Thread(target=worker_func).start()



if __name__ == '__main__':
    simple_thread_demo()