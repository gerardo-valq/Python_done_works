#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import tweepy, time, sys
 
argfile = str(sys.argv[1])
 
#enter the corresponding information from your Twitter application:
CONSUMER_KEY = 'Wr9wAm7QJr0cKCj90Ux7OpudA'#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = '06YD1qy8yUQ3HWvebBTXrAKKGeNk7XNvWC7EBbaILLekXqf7VP'#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = '1125804781-R22qeNdbRQGmRzTy62MdqqCa7Yi2yl3rFVuKzeu'#keep the quotes, replace this with your access token
ACCESS_SECRET = 'AIWf0uDAddvnUtuK77xXQICrqni8tExQUHeUKFMpOlUps'#keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
 
filename=open(argfile,'r')
f=filename.readlines()
filename.close()

for line in f:
    api.update_status(line)
    time.sleep(60)#Tweet every 5 minutes
