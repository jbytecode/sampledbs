import gc 

gc.set_debug(gc.DEBUG_STATS)

a = [i ** 2 for i in range(1000000)]

b = [i ** 2 for i in range(1000000)]

c = [i ** 2 for i in range(1000000)]

a = None
b = None
c = None

gc.collect()


