
#!/usr/bin/env python

import urllib.parse, sys, urllib.request
import feedparser

def error(msg):
    sys.exit(msg)

def main():
    api = 'https://www.instapaper.com/api/add'

def post_is_in_db(link):
    with open(db, 'r') as database:
        for line in database:
            if link in line:
                return True
    return False

db = "test.db" #locate a file for storing basic url feeds that have been saved
log = "log.dg" #log to note changes


RSS_feeds = ['https://www.exmaple.com',
            'https://www.example2.com',
            'https://www.example3.com'
            ]
feeds = []
for url in RSS_feeds:
    feeds.append(feedparser.parse(url))


#print (d['feed']['title'])
#print (d['feed']['link'])
#print (d.entries[0]['link'])
#print (len(d['entries']))

for feed in feeds:
    items = (len(feed['entries']))
    title = (feed['feed']['title'])
    #print (len(feed['entries']))
    #print (feed['feed']['title'])
    f = open (log, 'a')
    f.write(title + str(items) + "\n")
    for post in feed.entries:
        link = post.link
        if post_is_in_db(link):
            f.write (post.title + 'already saved' + "\n")
            f.close
            #print('already saved')
        else:
            f = open(db, 'a')
            #for link in post_is_in_db:
            f.write(link + "\n")
            f.close
            params = urllib.parse.urlencode({
                'username'  : 'username', #instapaper username
                'password'  : 'password', #instapaper password 
                'url'       : post.link,
                'title'     : post.title,
                'selection' : 'codetest' 
                }).encode("utf-8")
            r = urllib.request.urlopen('https://www.instapaper.com/api/add', params)