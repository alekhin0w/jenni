#!/usr/bin/env python
# encoding: utf-8

"""
lanata.py - Jenni Lanata Module
by alekhin0w, munshkr

More info:
 * Jenni: https://github.com/myano/jenni/
 * Phenny: http://inamidst.com/phenny/
"""

import random, re
from modules import unicode as uc

MIN_SIZE_WORD = 4
MAX_SIZE_WORD = 12
DEFAULT_FREQ = 10

reading = False
freq = None
inputs = []


def _say_lanata(jenni, target):
    target = re.sub('\W', '', target)
    if len(target) > 0:
        jenni.say("%s?" % target)
        jenni.say("*%s* es lanata" % target)

def _parse_int(s):
    try:
        return int(s)
    except ValueError:
        return DEFAULT_FREQ

def _is_valid_word(w):
    return (len(w) > MIN_SIZE_WORD and
            len(w) < MAX_SIZE_WORD and
            w not in STOPWORDS)


def lanata(jenni, input):
    """ Cualca's gag some word and tell that is lanata """

    target = input.group(2)
    if not target:
        return jenni.reply('.i <word>!')
    target.encode('utf-8')
    target = (target).strip()
    _say_lanata(jenni, target)

lanata.commands = ['l']
lanata.priority = 'medium'
lanata.example = '.l <word>'


def lanata_mode(jenni, input):
    """
    Enable lanata mode, says lanata gag based on <freq>
    and what has been said on channel

    Set <freq> to 0 to disable lanata mode

    """
    global reading, freq

    freq = _parse_int(input.group(2))
    if freq == 0:
        reading = False
        jenni.reply('.lm off')
    else:
        reading = True
        jenni.reply('.lm on (freq %d)' % freq)

lanata_mode.commands = ['lm']
lanata_mode.priority = 'medium'
lanata_mode.example = '.lm <freq> (0 to disable)'


def lanata_reader(jenni, input):
    global reading, inputs

    if reading == False:
        return

    inputs.append(input)
    #print(inputs)

    if len(inputs) >= freq:
        # Tokenize line inputs, without duplicates,
        # stopwords and words shorter than 4 chars
        words = set(w.lower() for line in inputs
                    for w in line.split()
                    if _is_valid_word(w))

        # Choose randomly a word
        if len(words) > 0:
            target = random.choice(list(words))
            _say_lanata(jenni, target)

        inputs = []

lanata_reader.priority = 'medium'
lanata_reader.rule = r'.+'
lanata_reader.thread = False


if __name__ == '__main__':
    print __doc__.strip()


STOPWORDS = set([
    "algún",
    "alguna",
    "algunas",
    "alguno",
    "algunos",
    "ambos",
    "ampleamos",
    "ante",
    "antes",
    "aquel",
    "aquellas",
    "aquellos",
    "aqui",
    "arriba",
    "atras",
    "bajo",
    "bastante",
    "bien",
    "cada",
    "cierta",
    "ciertas",
    "cierto",
    "ciertos",
    "como",
    "con",
    "conseguimos",
    "conseguir",
    "consigo",
    "consigue",
    "consiguen",
    "consigues",
    "cual",
    "cuando",
    "dentro",
    "desde",
    "donde",
    "dos",
    "el",
    "ellas",
    "ellos",
    "empleais",
    "emplean",
    "emplear",
    "empleas",
    "empleo",
    "en",
    "encima",
    "entonces",
    "entre",
    "era",
    "eramos",
    "eran",
    "eras",
    "eres",
    "es",
    "esta",
    "estaba",
    "estado",
    "estais",
    "estamos",
    "estan",
    "estoy",
    "fin",
    "fue",
    "fueron",
    "fui",
    "fuimos",
    "gueno",
    "ha",
    "hace",
    "haceis",
    "hacemos",
    "hacen",
    "hacer",
    "haces",
    "hago",
    "incluso",
    "intenta",
    "intentais",
    "intentamos",
    "intentan",
    "intentar",
    "intentas",
    "intento",
    "ir",
    "la",
    "largo",
    "las",
    "lo",
    "los",
    "mientras",
    "mio",
    "modo",
    "muchos",
    "muy",
    "nos",
    "nosotros",
    "otro",
    "para",
    "pero",
    "podeis",
    "podemos",
    "poder",
    "podria",
    "podriais",
    "podriamos",
    "podrian",
    "podrias",
    "por",
    "por qué",
    "porque",
    "primero",
    "puede",
    "pueden",
    "puedo",
    "quien",
    "sabe",
    "sabeis",
    "sabemos",
    "saben",
    "saber",
    "sabes",
    "ser",
    "si",
    "siendo",
    "sin",
    "sobre",
    "sois",
    "solamente",
    "solo",
    "somos",
    "soy",
    "su",
    "sus",
    "también",
    "teneis",
    "tenemos",
    "tener",
    "tengo",
    "tiempo",
    "tiene",
    "tienen",
    "todo",
    "trabaja",
    "trabajais",
    "trabajamos",
    "trabajan",
    "trabajar",
    "trabajas",
    "trabajo",
    "tras",
    "tuyo",
    "ultimo",
    "un",
    "una",
    "unas",
    "uno",
    "unos",
    "usa",
    "usais",
    "usamos",
    "usan",
    "usar",
    "usas",
    "uso",
    "va",
    "vais",
    "valor",
    "vamos",
    "van",
    "vaya",
    "verdad",
    "verdadera",
    "verdadero",
    "vosotras",
    "vosotros",
    "voy",
    "yo",
])
