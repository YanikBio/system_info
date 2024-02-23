"""
Декораторы для файлов
"""

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

        with open('file.txt', 'w') as file:
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