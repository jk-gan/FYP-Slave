import urllib

try:
  stri = "http://192.168.1.2:3306"
  data = urllib.urlopen(stri)
  print "Connected"
except urllib.URLError as e:
  print "not connected",e
