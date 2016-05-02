import os

os.system('sudo ifconfig eth0 down')
os.system('sudo ifconfig eth0 192.168.1.10')
os.system('sudo ifconfig eth0 up')
