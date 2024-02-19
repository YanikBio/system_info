'''
Программа, которая будет в реальном времени показывать загруженность процессоров в процентном виде и в простейшем графическом
представлении (предстваить как  |*n), а также запущенные на данный момент процессы на данном компьютере + если будет возможность
познакомится ближе с библиотеками, что помогают визуализировать полученную информаци.

Как создать обновление в реальном времени в терминале?

*** Добавить декоратор, который добавляет собранную информацию в файл 
'''

#поменял имя ветки
import psutil as p
import time as t


def take_from(func):
    def take_info():

        data = func()

        with open('file.txt', 'a') as file:
            for user in data:
                file.write(str(user) + '\n')

            file.write('\n')

        return data
    
    return take_info

def take_from_processes(func):
    def take_info():
        proceses = func()

        with open('file.txt', 'a') as file:
            show_info = ''
            n = 0
            for proc in proceses:
                show_info += f"{proc.info['username']:30}| {proc.info['name']:30}| {proc.info['pid']:5}\n"
                n += 1
                if n == 30:
                    break
            file.write(show_info)

        return proceses

    return take_info


@take_from
def get_user():
    users = p.users()

    return users

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

@take_from
def get_cpu():
    cpu_stat = p.cpu_percent(interval=1, percpu=True)
    return cpu_stat

def show_cpu():
    cpu = get_cpu()
    show_info = "Загруженность ядер: \n"

    for n in range(len(cpu)):
        show_info += (f" Ядро №{n+1}: {cpu[n]:4}% " + '|' * int((cpu[n])//5) + '\n')  # here I make an string with answer
    return show_info

@take_from_processes
def get_proceses():
    proceses = p.process_iter(['pid', 'name', 'username'])
        
    return proceses

def show_proc():
    proceses = get_proceses()
    _ = ''
    show_info = f"PROCESESS:\nUsername:{_:20} |Name of process:{_:14} |PID:{_:1}  \n"
    n = 0
    for proc in proceses:
        show_info += f"{proc.info['username']:30}| {proc.info['name']:30}| {proc.info['pid']:5}\n"
        n += 1
        if n == 30:
            break

    return show_info

@take_from
def get_memory():
    virtual = p.virtual_memory()
    swop = p.swap_memory()
    return virtual, swop
    
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


def get_time():
    boot_time = int(p.boot_time())
    epoch_time = int(t.time())

    seconds_time = epoch_time - boot_time

    return seconds_time

def iiiiiiiiiitS_SHOW_TIMEEEEE():
    seconds_time = get_time()
    
    h = seconds_time // 3600
    m = (seconds_time % 3600) // 60
    s = seconds_time % 60
    show_time = f"ВРЕМЯ ДАННОЙ СЕССИИ: {h}{':'}{m:02}{':'}{s:02}\n"

    return show_time


def clear_terminal():
    print("\033c\033[3J", end="")  # \033c - сбрасывает состояние терминала, а \033[3J - очищает буфер прокрутки

def show_all_info():
    while True:
        user_showing = show_user()
        time_showing = iiiiiiiiiitS_SHOW_TIMEEEEE()
        cpu_showing = show_cpu()
        memory_showing = show_memory()
        proc_showing = show_proc()
        
        clear_terminal()
        
        print(user_showing)
        print(time_showing)
        print(cpu_showing)
        print(memory_showing)
        print(proc_showing)

def main():
    show_all_info()

        
if __name__ == '__main__':
    main()


