import socket
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(0.5)

try:
  s.connect(('192.168.1.2', 3306))
  print 'Connected'
  # ip addr flush wlan0
except Exception, e:
  print 'Not connected'
  os.system('sudo ifconfig wlan0 down')
  os.system('sudo ifconfig wlan0 192.168.1.2')
  os.system('sudo ifconfig wlan0 up')
s.close()
