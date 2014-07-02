#!/usr/bin/env python
"""
lanata.py - Jenni Lanata Module
by alekhin0w

More info:
 * Jenni: https://github.com/myano/jenni/
 * Phenny: http://inamidst.com/phenny/
"""
import os, random
from modules import unicode as uc

def lanata(jenni, input):
    """ Cualca's gag some word and tell that is lanata """

    target = input.group(2)
    if not target:
        return jenni.reply('.i <word>!')
    target.encode('utf-8')
    target = (target).strip()
    jenni.say(target + "?")
    jenni.say("*" + target + "* es lanata")
    #jenni.say(target + ': ' + uc.decode(random.choice(lines)))
    

lanata.commands = ['l']
lanata.priority = 'medium'
lanata.example = '.l <word>'

if __name__ == '__main__':
    print __doc__.strip()
