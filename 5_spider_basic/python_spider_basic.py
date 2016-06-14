# -*- coding: utf-8 -*-
import urllib

def demo():
    s = urllib.urlopen('http://blog.kamidox.com')
    print s.read(100)


if __name__=='__main__':
    demo()
