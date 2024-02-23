"""
Сделаю так, чтобы каждая функция возвращала однотипные данные в виде словарей
"""

import psutil as p
import time as t
import d_in_file
from d_in_json import json_decorator

@json_decorator('./info/user_info.json')
def get_user():
    users = p.users()
        
    return users

@json_decorator('./info/cpu_info.json')
def get_cpu():
    get_cpu_stat = p.cpu_percent(interval=1, percpu=True)
    cpu_stat = {}
    n = 1
    for cpu in get_cpu_stat:
        cpu_stat[n] = cpu
        n+=1

    return cpu_stat


def get_proceses():
    from_proceses = p.process_iter(['pid', 'name', 'username'])
    #choose = ['pid', 'name', 'username']
    proceses = {}
    n = 1
    for proc in from_proceses:
        proceses[n] = proc
        n += 1
        
    return proceses

@json_decorator('./info/memory_info.json')
def get_memory():
    virtual = p.virtual_memory()
    swop = p.swap_memory()
    return virtual, swop

@json_decorator('./info/time_info.json')
def get_time():
    boot_time = int(p.boot_time())
    epoch_time = int(t.time())

    seconds_time = epoch_time - boot_time

    return seconds_time

def train():

    print(get_user())
    print(get_cpu())
    print(get_proceses())
    print(get_memory())
    print(get_time())

if __name__ == '__main__':
    train()