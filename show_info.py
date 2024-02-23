'''
 оставляю почти без изменений
'''

from get_info import get_cpu, get_memory, get_proceses, get_time, get_user
import time as t

def show_user():
    users = get_user()
    epoch_time = t.time()
    show_users = ""
    n = 1
    for user in users:
        s = int((epoch_time - user.started) % 60)
        m = int(((epoch_time - user.started) % 3600) // 60)
        h = int((epoch_time - user.started) // 3600)
        show_users += f"ПОЛЬЗОВАТЕЛЬ №{n}: {user.name} ТЕРМИНАЛ: {user.terminal} ВРЕМЯ СЕАНСА: {h}:{m:02}:{s:02} HOST: {user.host}\n"
        n += 1

    return show_users

def show_cpu():
    cpu:dict = get_cpu()
    show_info = "Загруженность ядер: \n"

    for key in cpu:
        show_info += (f" Ядро №{key}: {cpu[key]:4}% " + '|' * int((cpu[key])//5) + '\n')  # here I make an string with answer
    return show_info

def show_proc():
    proceses = get_proceses()
    _ = ''
    show_info = f"PROCESESS:\nUsername:{_:20} |Name of process:{_:14} |PID:{_:1}  \n"
    n = 0
    for proc in proceses:
        show_info += f"{proceses[proc].info['username']:30}| {proceses[proc].info['name']:30}| {proceses[proc].info['pid']:5}\n"
        n += 1
        if n == 30:
            break

    return show_info

def show_memory():
    virtual, swop = get_memory()
    v_total = virtual.total / 1024 / 1024  # make mb view
    v_avail = virtual.available / 1024 / 1024
    v_percent = virtual.percent

    s_total = swop.total / 1024 / 1024
    s_free = swop.free / 1024 / 1024
    s_percent = swop.percent

    mb = "Mb"

    show_vsmemory = f"ВИРТУАЛЬНАЯ ПАМЯТЬ:{" ":30}SWOP ПАМЯТЬ (ПОДКАЧКА):\n" + \
    f"|Объём:{" ":5}|Доступная:{" ":5}|Используется:{" ":8}" + f"|Объём:{" ":5}|Доступная:{" ":5}|Используется:\n" + \
    f"|{v_total:1}{" Mb":4}|{v_avail:1.3f}{" Mb":7}|{v_percent} %{" ":15}" + f"|{s_total:1}{" Mb":4}|{s_free:1.3f}{" Mb":8}|{s_percent:<} %\n"


    return show_vsmemory

def iiiiiiiiiitS_SHOW_TIMEEEEE():
    seconds_time = get_time()
    
    h = seconds_time // 3600
    m = (seconds_time % 3600) // 60
    s = seconds_time % 60
    show_time = f"ВРЕМЯ ДАННОЙ СЕССИИ: {h}{':'}{m:02}{':'}{s:02}\n"

    return show_time