import psutil as p 

virtual = p.virtual_memory()
swop = p.swap_memory()

print(virtual.total)