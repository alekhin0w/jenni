#!/usr/bin/env python
"""
death.py - Jenni lasts deaths Module
by alekhin0w, ntz

More info:
 * Jenni: https://github.com/myano/jenni/
 * Phenny: http://inamidst.com/phenny/
"""
import os, random
from modules import unicode as uc
import BeautifulSoup
import urllib
def death(jenni, input):
    """ get list of last deaths """
    
    deaths = ''.join(__import__('BeautifulSoup').BeautifulSoup(__import__('urllib').urlopen('https://en.wikipedia.org/wiki/Deaths_in_2014').read()).find(id='mw-content-text').findAll('ul')[4].findAll('li',text=True)).strip()
    jenni.say(deaths)

death.commands = ['d', 'death']
death.priority = 'medium'
death.example = '.death or .d'

if __name__ == '__main__':
    print __doc__.strip()
