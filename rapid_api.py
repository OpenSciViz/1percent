#!/usr/bin/env python
import os, sys
import argparse, copy, datetime
import requests
# import flask

def dotcom(url):
  domain_name = url[2+url.index('//'):4+url.index('.com')] ; print(domain_name)
  return domain_name

def querydict(domains, ticker):
  query_hist = {"symbol":ticker,"interval":"1day","outputsize":"30","format":"json"}
  query_now = {'term': ticker} # either delayed or not, depending on source domain?
  querydict = {}
  for dom in domains: 
    querydict[dom] = {'term': ticker}

def rapid_api(ticker='UVXY', domain='seeking-alpha.p.rapidapi.com', url='https://seeking-alpha.p.rapidapi.com/auto-complete'):
  """
  from:
  https://rapidapi.com/apidojo/api/seeking-alpha
  https://rapidapi.com/zirra/api/zirra
  """
  domain_name = dotcom(url)
  headers = {
    'x-rapidapi-key': "ec866c3dafmsh8ee53350a526aeep1a5cbdjsn2fdaf680b7d7",
    'x-rapidapi-host': domain_name
  }

  response = requests.request("GET", url, headers=headers, params=querystring)
  txt = response.text
  return txt

def all_urls(ticker='UVXY'):
  """
  dictionay or url key vals with placeholder val
  """
  urls = {}
  urls['https://zirra.p.rapidapi.com/v1/companies'] = ticker
  urls['https://twelve-data1.p.rapidapi.com/time_series'] = ticker
  urls['https://seeking-alpha.p.rapidapi.com/auto-complete'] = ticker
# key_val = {'https://seeking-alpha.p.rapidapi.com/auto-complete': ticker}
# urls = {**urls ,**key_val}

  print(urls)
  return urls

def main(argv=None):
  urldict = all_urls() ; print(urldict)
  domains = urldict.keys() ; urls = urldict.vals()

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
      if(args.count <= len(domains)): cnt = args.count
      print(ticker, cnt)
      while cnt > 0:
        cnt -= 1;
        txt = rapid_api(ticker, doamins[cnt],  urls[cnt]) ; print(txt)
    except Exception as esa:
      print(esa, ticker) # seeking_alpha api
      return -cnt
  except Exception as eap: 
    print(eap, ticker) # arg parsing
    return -cnt

  # if all webt well cnt == 0
  return cnt

if __name__ == "__main__":
  status = main()
  sys.exit(status)

