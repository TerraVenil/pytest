#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#python-twitter
import twitter

def sendTwitter(text,img,consumer_key, consumer_secret, access_token_key, access_token_secret):
    api = twitter.Api(consumer_key=consumer_key, consumer_secret=consumer_secret,
                      access_token_key=access_token_key, access_token_secret=access_token_secret)
    api.PostMedia(text, img)

if __name__ == '__main__' :
    text = 'Free #Youtube Views #vagex http://vagex.com/?ref=390884'
    img = '/backup/ad.png'
    consumer_key = 'DiS3phJ4EWuJhdwwh2DPzjjMo'
    consumer_secret = 'yVqVnayeLXH6bDFmV3vrjIFzur6TNG4OsCwwcSFAhXfNp6PwY1'
    access_token_key = '743645094595661824-tIj8DiiFcXE0i3t22l5RlbdIxLnJynK'
    access_token_secret = 'MtHIcgRyoeeVCCL3R8Po8T51jos8RgFUwuz7ruxbFvCT7'
    sendTwitter(text, img, consumer_key, consumer_secret, access_token_key, access_token_secret)

