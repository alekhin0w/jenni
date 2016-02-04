#!/usr/bin/env python
"""
ctf.py - Jenni CTF tool
by alekhin0w

More info:
 * Jenni: https://github.com/myano/jenni/
 * Phenny: http://inamidst.com/phenny/
"""
import os, random
from modules import unicode as uc

class CTF():

    players = []
    challenges = [] # 'name' : 'solved? (true/false)'

    players_challenges = {} # 'player' : 'challenge_name'

    challenge_status = {} # 'challenge' : 'status (Solved, Unsolved)'

CTF = CTF()

def ctf(jenni, input):
    """ report the state of every ctf player """
    player = input.group(2)
    if player == None:
        jenni.say('[CTF] Showing all statuses')
        jenni.say('--------B E G I N --------')
        for player in CTF.players_challenges.keys():
            jenni.say('[CTF] Player (%s) is working on challenge (%s)' % (player, CTF.players_challenges[player]))    
        jenni.say('-----------E N D----------')            
        return
    elif player in CTF.players:
        try:
            jenni.say('[CTF] Player (%s) is working on challenge (%s)' % (player, CTF.players_challenges[player]))    
        except:
            jenni.say('[CTF] No challenges for player: %s' % player)    
    else:
        jenni.say('[CTF] No such player: %s' % player)    
    

ctf.commands = ['ctf']
ctf.priority = 'low'
ctf.example = '.ctf [player] show user status'
    
def add_player(jenni, input):
    """ adds a player to the CTF """
    target = input.group(2)
    if target == None:
        jenni.say('[CTF] Add Player: - must add a username')
    else:
        CTF.players.append(input.group(2))
        jenni.say('[CTF] Add Player: %s added!' % target ) 

add_player.commands=['ctf_add_player']
add_player.priority='low'
add_player.example='.ctf_add_player [player_name]'

def add_challenge(jenni, input):
    """ add a challenge """
    target = input.group(2)
    if target == None:
        jenni.say('[CTF] Add Challenge: - must add a challenge name')
    else:
        CTF.challenges.append(target)
        CTF.challenge_status[target] = False
        jenni.say('[CTF] Add Challenge: %s added!' % target ) 

add_challenge.commands=['ctf_add_challenge']
add_challenge.priority='low'
add_challenge.example='.ctf_add_challenge [challenge_name]'

def add_player_challenge(jenni, input):
    """ adds a player and a challenge that is working on """
    player = input.group(2).split(' ')[0]
    challenge = input.group(2).split(' ')[1]

    if player in CTF.players:
        if challenge in CTF.challenges.keys():
            CTF.players_challenges[player] = CTF.challenges[challenge]
        else:
            jenni.say('[CTF] No challenge named %s' % (challenge) )
    else:
        jenni.say('[CTF] %s not playing this instance of ctf' % (player) )

add_player_challenge.commands=['ctf_add_player_challenge']
add_player_challenge.priority='low'
add_player_challenge.example='.ctf_add_player_challenge [player_name] [challenge_name]'

def ctf_save(jenni, user):
    pass

# def insult(jenni, input):
#     """ insults <target> with configured language insult """
#     try:
#         insultFilename = os.path.expanduser('~/.jenni/insult.'+ jenni.config.insult_lang +'.txt')
#     except:
#         jenni.say("You need to configure the default language!")
#         return

#     target = input.group(2)
#     if not target:
#         return jenni.reply('.i <target>!')
#     target.encode('utf-8')
#     target = (target).strip()
#     try:
#         fn = open(insultFilename, "r")
#     except IOError as e:
#         generateDatabase(jenni, insultFilename)
#         fn = open(insultFilename, "r")
#     lines = fn.readlines()
#     fn.close()
#     random.seed()
#     jenni.say(target + ': ' + uc.decode(random.choice(lines)))

# insult.commands = ['i']
# insult.priority = 'medium'
# insult.example = '.i <target>'

# def addinsult(jenni, input):
#     """.iadd <insult> -- adds a harsh adjetive to the insult database"""
#     try:
#         insultFilename = os.path.expanduser('~/.jenni/insult.'+ jenni.config.insult_lang +'.txt')
#     except:
#         jenni.say("You need to configure the default language!")
#         return

#     text = input.group(2)
#     text = uc.encode(text)
#     fn = open(insultFilename, "a")
#     fn.write(text)
#     fn.write("\n")
#     fn.close()
#     jenni.reply("Insult added.")
# addinsult.commands = ['iadd']
# addinsult.priority = 'medium'
# addinsult.example = '.iadd Bad Person'
# addinsult.rate = 30

# def generateDatabase(jenni, insultFilename):
#     if jenni.config.insult_lang == "english":
#         insultList = ['fuck you', 'stupid', 'asshole', 'you suck']
#     elif jenni.config.insult_lang == "spanish":
#         insultList = ['puto', 'trolo', 'forro', 'insurrecto', 'trolita', 'aguafiestas', 'actualizame esta gil', 'apestoso usuario de windows']
#     else:
#         return # silent fail due lack of configuration
#     fn = open(insultFilename, "a")

#     for insult in insultList:
#         fn.write(insult)
#         fn.write("\n")
#     fn.close()

#     jenni.say(jenni.config.insult_lang + " insult database created.")

if __name__ == '__main__':
    print __doc__.strip()
