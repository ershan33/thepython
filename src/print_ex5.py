import time

for _ in range(10):
    print('.', end='', flush=True)
    time.sleep(.1)

print('\ndone')
