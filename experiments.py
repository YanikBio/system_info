import psutil as p 

virtual = p.virtual_memory()
v_show = virtual.total / 1024 / 1024 / 1024

print(f'{v_show}')