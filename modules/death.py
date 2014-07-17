#!/usr/bin/env python
"""
death.py - Jenni lasts deaths Module
by alekhin0w, ntz

More info:
 * Jenni: https://github.com/myano/jenni/
 * Phenny: http://inamidst.com/phenny/
"""
import os, random
#from modules import unicode as uc
from BeautifulSoup import BeautifulSoup
from urllib import urlopen
from datetime import datetime, date
def death(jenni, input):
    """ get list of last deaths by date or get the last ones """
    url = 'https://en.wikipedia.org/wiki/Deaths_in_%s'
    d = date.today()
 
    if not input.group(2):
        year = datetime.now().year
        html = BeautifulSoup(urlopen(url % year).read())
        items = html.find(id='mw-content-text').findAll('ul')[3].findAll('li')
    else:
        if '/' in input.group(2):
            # proximamente nombre
            day,month,year = input.group(2).split('/')
            d = date(int(year), int(month), int(day))
            if d > date.today():
                return jenni.say('*%s*, unknown, hemorroids and bleeding prolapse' % input.nick )
            html = BeautifulSoup(urlopen(url % d.strftime("%B_%Y")).read())
            try:
		items = html.find(id=d.day).findParent('h3').findNext('ul').findAll('li')
	    except AttributeError:
		return jenni.say('No encontre muertes para la fecha %s' % d.__str__())
        else:
            return jenni.say('.d[eaths] %d/%m/%y')
    for e in items:
        jenni.say("[%s] %s" % (d.__str__(), e.text))
    return

death.commands = ['d', 'death']
death.priority = 'medium'
death.example = '.death|.d [dd/mm/yyyy]'

if __name__ == '__main__':
    print __doc__.strip()
