from flags import Flags
import sys
from ports import APP, static_APP,Core, localStorage,Response,HTTPWorker, Socket
from ports import tools
import ssl
import socket
x = Flags(sys.argv)
def server(p):

  l = "no response"
  def lx(data):  
    x = input("> ")
    if x == "exit":
      print("exiting...")
      app.kill()
    return x
  from ports import Socket
  from taskel import Tasks
  import time
  tm = Tasks()
  app = APP()
  
  app.config["static_dir"] = "www"
  s = Socket(app)
  def refresh():
    print("hello world")
  
  
  
  time.sleep(2)
  @s.on("*")
  async def all(data,path):
  
      print("received data!")
      return lx(data)
  def socketrun():
    s.run(port=p)
  t = tm.create(target=socketrun,daemon=True)
  t.start()
  print("Mesh network, socket server booted.")
  print("waiting for connections..")
  while True:
    time.sleep(1)

    
def con(h,p,c):
  app = APP()
  s = Socket(app)
  app.config["host"] = h
  app.config["port"] = int(p)
  s.connect(sock="*",conn=c)


if x.flag in ["-s","--server"]:
  server(x.arg)
if x.flag in ["-c","--connect"]:
  h = x.arg
  p = x.args[0]
  x.args.remove(x.args[0])
  if "-ka" in x.args:
    x.args.remove("-ka")
    while True:
      l = input("!> ")
      con(h,p,l)
  else:
    con(h,p," ".join(x.args))
    

  
  
    
