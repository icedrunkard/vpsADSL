import os
import time
def connect():
  name="宽带连接"
  username='75713643@hinet.net'
  password="1qazqq"
  cmd_str="rasdial %s %s %s" %(name,username,password)
  res=os.system(cmd_str)
  ipconfig=os.popen('ipconfig')
  k=0
  for i in ipconfig.readlines():
    
    print(k,i)
    k+=1
  if res==0:
    print "connect successful"
  else:
    print res
  time.sleep(5)
def disconnect():
  name="宽带连接"
  cmdstr="rasdial %s /disconnect" %name
  os.system(cmdstr)
  time.sleep(5)


while(True):
  connect()
  disconnect()
  
