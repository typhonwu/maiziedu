# -*- coding: utf-8 -*-
import urllib2

def nowplaying_movies(url):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)\
                   AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73\
                   Safari/537.36'}
        req = urllib2.Request(url, headers=headers)

if __name__ == '__main__':
    url = 'https://movie.douban.com/nowplaying/xiamen/'
    movies = nowplaying_movies(url)

    import json
    print('%s' % json.dumps(
        movies, sort_keys=True, indent=4, separators=(',', ': ')))
