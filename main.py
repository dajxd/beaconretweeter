# -*- coding: utf-8 -*-
import twitter
import os


api = twitter.Api(consumer_key=os.environ['C_KEY'],
                  consumer_secret=os.environ['C_SEC'],
                  access_token_key=os.environ['AT_KEY'],
                  access_token_secret=os.environ['AT_SEC'])

for item in api.GetStreamFilter(track=['#beaconny']):
    print item
    if item.has_key('text'):
        try:
            statis = api.PostRetweet(item['id'])
        except twitter.TwitterError:
            print "dupe"