#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, time, sys
import random
from random import randint
from time import sleep

CONSUMER_KEY = ''
CONSUMER_SECRET = ''

ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''

def oauth_login(consumer_key, consumer_secret,access_key,access_secret):
  """Authenticate with twitter using OAuth"""
  auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_key, access_secret)
  return tweepy.API(auth)

if __name__ == "__main__":
  api = oauth_login(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
  print "Authenticated as: %s" % api.me().screen_name

  ltweets     = []
  ldiputados  = []

  atweets     = str(sys.argv[1])
  adiputados  = str(sys.argv[2])

  ftweets     = open(atweets,'r')
  fdiputados  = open(adiputados,'r')

  stweets     = ftweets.readlines()
  sdiputados  = fdiputados.readlines()

  for line in stweets:
    ltweets.append(line.strip())

  for line in sdiputados:
    ldiputados.append(line.strip())

  for diputado in ldiputados:
    random.shuffle(ltweets)
    for tweet in ltweets:
      tweet   = tweet.decode('utf-8')
      tweet   = tweet.replace('@',diputado)
      cadena  = tweet
      print tweet
      try:
          api.update_status(status=cadena)
          espera = randint(30,300)
          time.sleep(espera)
          print 'espera: '+str(espera)+' segundos'
      except:
          print "Failed to tweet:", tweet
