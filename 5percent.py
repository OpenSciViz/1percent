#!/usr/bin/env python3

import csv, json, os, sys 
import logging as log 
from pprint import pprint
from datetime import date
from datetime import datetime as dt

def pp(*argv):
  try:
    # print('Hello', 'World', 2+3, file=open('file.txt', 'w'))
    # sys.write(argv[0]+': ') 
    # for arg in argv[1:]:
    for arg in argv[0:]:
      pprint(arg)
  except: pass

def hon2020(args=[]):
  """
  Manual text entry transposed from yfinance during market day, not da close
  TPD: replace snapshot vals with { close: val, open: val, low: val, high: val } 
  """
  today = 'Mon Feb 22, 2021'
  honhedge = {}

# no dividends, but potentially bid capital gains:
  honhedge['UVXY'] = -27.85
  honhedge['PSTX'] = 19.70
  pp(honhedge) ; idx = len(honhedge)

# dividends 5% and higher at datetime  of acq:
  honhedge['AINV'] = 55.64
  pp(list(honhedge.items())[-idx:]) ; idx = len(honhedge)

  honhedge['AM'] = 48.91
  honhedge['STWD'] = 47.33
  honhedge['ABR'] = 46.67
  honhedge['OHI'] = 43.46
  pp(list(honhedge.items())[-idx:]) ; idx = len(honhedge)

  honhedge['WBA'] = 37.63
  honhedge['KBWD'] = 32.16
  honhedge['GLAD'] = 32.03
  honhedge['BIZD'] = 31.37
  honhedge['CIM'] = 30.17
  pp(list(honhedge.items())[-idx:]) ; idx = len(honhedge)

  honhedge['GAIN'] = 28.96
  honhedge['MFD'] = 25.13
  honhedge['DPG'] = 24.02
  honhedge['SDIV'] = 23.84
  honhedge['BDCS'] = 23.38
  honhedge['JTA'] = 22.55
  honhedge['JRS'] = 22.13
  honhedge['LUMN'] = 21.84
  honhedge['ARR'] = 21.73
  honhedge['EXG'] = 21.5
  honhedge['NVG'] = 21.32
  pp(list(honhedge.items())[-idx:]) ; idx = len(honhedge)

  honhedge['DIAX'] = 18.65
  honhedge['MHD'] = 18.04
  honhedge['JDD'] = 17.42
  honhedge['FOF'] = 17.39
  honhedge['DSL'] = 17.2
  honhedge['MYD'] = 16.39
  honhedge['MUX'] = 16.2
  honhedge['ATAX'] = 15.52
  honhedge['NMZ'] = 10.01
  honhedge['JQC'] = 10.0
 
  pp(list(honhedge.items())[-idx:]) ; idx = len(honhedge)

  honhedge['GORO'] = 8.9
  honhedge['QYLD'] = 7.59
  honhedge['UTG'] = 1.25
  pp(list(honhedge.items())[-idx:]) ; idx = len(honhedge)

  return honhedge

def main(args):
  today = 'Mon Feb 22, 2021'
  pp('args: ', args)
  hh = hon2020()
  pp(today) 

############################

if __name__ == "__main__":
  args = sys.argv[1:]
  status = main(args)
  sys.exit(status)

