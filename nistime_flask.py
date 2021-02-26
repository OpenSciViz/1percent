#!/usr/bin/env python3
import csv, json, os, socket, sys
from datetime import datetime
from flask import Flask
from flask import current_app

_host = socket.gethostname()

def touch(fname, mode=0o666, dir_fd=None, **kwargs):
  """
  create or touch file
  """
  flags = os.O_CREAT | os.O_APPEND
  with os.fdopen(os.open(fname, flags=flags, mode=mode, dir_fd=dir_fd)) as f:
    os.utime(f.fileno() if os.utime in os.supports_fd else fname, dir_fd=None if os.supports_fd else dir_fd, **kwargs)

def fetch_nistime(hostname='time-d.nist.gov', port=13, content=None):
  """
  nc -4 -d time-d.nist.gov 13
  echo -n '58914 20-03-06 18:18:25 53 0 0 307.9 UTC(NIST) *'|wc -c
  48
  """
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  print("netcat> try:", hostname, port)
  data = None
  try:
    s.connect((hostname, port))
    if( content ): s.sendall(content)
    data = s.recv(48) # print(repr(data))
  except Exception as e:
    print("failed to fetch nistime\n", repr(e))
    return None

  s.shutdown(socket.SHUT_WR)
  s.close()
  return repr(data)

# Flask global app
_app = Flask(__name__)

@_app.route('/', methods=['GET', 'POST', 'PUT'])
def nistime():
  global _host
  refresh = _host + 'Refresh'
  resp = '<h2>' + _host + '</h2>'
  time = fetch_nistime('time-a.nist.gov')
  resp += '<a href="http://time-a.nist.gov:13">time-a.nist.gov</a><br/><p>' + repr(time)+'</p>'
  time = fetch_nistime('time-b.nist.gov')
  resp += '<a href="http://time-b.nist.gov:13">time-b.nist.gov</a><br/><p>' + repr(time)+'</p>'
  time = fetch_nistime('time-c.nist.gov')
  resp += '<a href="http://time-c.nist.gov:13">time-c.nist.gov</a><br/><p>' + repr(time)+'</p>'
  time = fetch_nistime('time-d.nist.gov')
  resp += '<a href="http://time-d.nist.gov:13">time-d.nist.gov</a><br/><p>' + repr(time)+'</p>'
 
  resp += '<form  method="POST" name="refresh" id="refresh"><input type="submit" value=' + refresh + '></form>'
  return resp 

if __name__ == '__main__':
  time = fetch_nistime('time-a.nist.gov')
  if(time):
    print(time)

  _app.run(debug=True, host='0.0.0.0', port='80')

