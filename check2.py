import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(0.5)

try:
  s.connect(('192.168.1.2', 3306))
  print 'Connected'
except Exception, e:
  print 'Not connected'

s.close()
