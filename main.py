'''
Программа, которая будет в реальном времени показывать загруженность процессоров в процентном виде и в простейшем графическом
представлении (предстваить как  |*n), а также запущенные на данный момент процессы на данном компьютере + если будет возможность
познакомится ближе с библиотеками, что помогают визуализировать полученную информаци.

Как создать обновление в реальном времени в терминале?
'''

import psutil as p
from os import system
import time as t

# here I get information about from cpu
def get_cpu():
    cpu_stat = p.cpu_percent(interval=1, percpu=True)
    return cpu_stat

# here I show information about cpu status
def show_cpu():
    cpu = get_cpu()
    show_info = "Загруженность ядер: \n"

    for n in range(len(cpu)):
        show_info += (f" Ядро №{n+1}: {cpu[n]:4}% " +  '|' * int((cpu[n]//10) + 1) + '\n')  # here I make an string with answer
    return show_info

# get info about computer process
def get_proceses():
    proceses = p.process_iter(['pid', 'name', 'username'])
        
    return proceses

# show info apout computer process
def show_proc():
    proceses = get_proceses()
    _ = ''
    show_info = f"Username:{_:20} |Name of process:{_:14} |PID:{_:1}  \n"
    n = 0
    for proc in proceses:
        show_info += f"{proc.info['username']:30}| {proc.info['name']:30}| {proc.info['pid']:5}\n"
        n += 1
        if n == 30:
            break

    return show_info

def get_memory():
    virtual = p.virtual_memory()
    swop = p.swap_memory()
    return virtual, swop
    
def show_memory():
    virtual, swop = get_memory()
    


def clear_terminal():
    print("\033c\033[3J", end="")  # \033c - сбрасывает состояние терминала, а \033[3J - очищает буфер прокрутки

def show_all_info():
    while True:
        cpu_showing = show_cpu()
        memory_showing = show_memory()
        proc_showing = show_proc()
        
        clear_terminal()
        
        print(cpu_showing)
        print(memory_showing)
        print(proc_showing)

def main():
    show_all_info()

        
if __name__ == '__main__':
    main()


