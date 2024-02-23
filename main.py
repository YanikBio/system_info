'''
Программа, которая будет в реальном времени показывать загруженность процессоров в процентном виде и в простейшем графическом
представлении (предстваить как  |*n), а также запущенные на данный момент процессы на данном компьютере + если будет возможность
познакомится ближе с библиотеками, что помогают визуализировать полученную информаци.

Как создать обновление в реальном времени в терминале?

*** Добавить декоратор, который добавляет собранную информацию в файл 
'''

from show_info import show_cpu, show_memory, show_proc, show_user, iiiiiiiiiitS_SHOW_TIMEEEEE


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


