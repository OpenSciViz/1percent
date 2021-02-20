#!/usr/bin/env python
import os, sys
import argparse, copy, datetime
import requests
# import flask

def rapid_api(ticker='UVXY', url='https://seeking-alpha.p.rapidapi.com/auto-complete'):
  """
  from:
  https://rapidapi.com/apidojo/api/seeking-alpha
  https://rapidapi.com/zirra/api/zirra
  """
  querystring = {'term': ticker}
  domain_name = url[2+url.index('//'):4+url.index('.com')] ; print(domain_name)
  headers = {
    'x-rapidapi-key': "ec866c3dafmsh8ee53350a526aeep1a5cbdjsn2fdaf680b7d7",
    'x-rapidapi-host': domain_name
  }

  response = requests.request("GET", url, headers=headers, params=querystring)
  txt = response.text
  return txt

def all_urls():
  urls = []
  urls.append('https://zirra.p.rapidapi.com/v1/companies')
  urls.append('https://seeking-alpha.p.rapidapi.com/auto-complete')
  return urls

def main(argv=None):
  urls = all_urls() ; print(urls)
  ticker = 'UVXY' ; cnt = len(urls) ; txt = None
  try:
    if argv is None: argv = sys.argv
    ap = argparse.ArgumentParser()
    ap.add_argument('--ticker', nargs='?', const=1, type=str, default='uvxy')
    ap.add_argument('-t', nargs='?', const=1, type=str, default='uvxy')
    ap.add_argument('--count', nargs='?', const=1, type=int, default=len(urls))
    ap.add_argument('-c', nargs='?', const=1, type=int, default=len(urls))
    #opts, args = ap.parse_known_args(['uvxy', '-t', 'uvxy', '--ticker', 'aticker'])
    args = ap.parse_args()
    try:
      ticker = args.ticker
      if(args.count <= len(urls)): cnt = args.count
      print(ticker, cnt)
      while cnt > 0:
        cnt -= 1;
        txt = rapid_api(ticker, urls[cnt-1]) ; print(txt)
    except Exception as esa:
      print(esa, ticker) # seeking_alpha api
      return -2
  except Exception as eap: 
    print(eap, ticker) # arg parsing
    return -1

  return 0

if __name__ == "__main__":
  sys.exit(main())

