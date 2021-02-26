#!/usr/bin/env python

import sys, codecs, datetime, json
print(sys.version)

import codecs, datetime, json
import yfinance as yf

# if we need to sanitize poorly encoded text for tty output:
#sys.stdout = codecs.getwriter('utf8')(sys.stdout)
#sys.stderr = codecs.getwriter('utf8')(sys.stderr)
from datetime import date

class Week:
  def __init__(self, start_end=['2020-07-06', '2020-07-11']):
    self.start = start_end[0] ; self.end = start_end[1]

def satsunday(input=datetime.date.today()):
    d = input.toordinal()
    last = d - 6
    sunday = last - (last % 7)
    sund = datetime.date.fromordinal(sunday)
    saturday = sunday + 6
    satd = datetime.date.fromordinal(saturday)
    return [str(sund), str(satd)]

def yf_weekly(tics, week):
  print(tics)
  data = yf.download(tics, week.start, week.end, group_by="ticker")
  for t in tics:
    t = t.upper()
    print(t, 'close:', data[t]['Close'])

  return data

def yf_options(tics):
  print(tics)
  optns = {}
  for t in tics:
    t = t.upper()
    q = yf.Ticker(t)
    try:
      info = q.info.items()
      for item in info: print(t,item)
    except: 
      print("failed to get ticker quote for:", t)
    try:
      opts_exp = q.options
      exp = opts_exp[0]
      opt = q.option_chain(exp)
      print(exp, opt.calls, opt.puts)
      optns[t] = { exp, str(info), str(opt.calls), str(opt.puts) }
    except: 
      print("failed to get options quote for:", t)

  return optns

if __name__ == '__main__':
  #tics = "atax diax dsl fof gut hqh hql jta jtd mfd ohi bdcs sdiv slv tpz wfc yyy"
  tics = "c wfc"
  tics = tics.upper().split(' ')
  ssday = satsunday()
  week = Week(ssday)
  #prices = yf_weekly(tics, week)
  #for t in tics:
    #print(t, prices[t])
  optns = yf_options(tics)
  for t in tics:
    print(t, optns)

