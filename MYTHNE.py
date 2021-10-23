'''
   This text novel engine must run Ace Attorney-like games.
   Must be:
   Linear storylines                                                               ✓
   Linear choices (allowing multiple)                                              ✓
   Looped choices (like AA cross-examinations)                                     ✓
   Court records  (also allowing presenting evidence in cross_examination)         ✗
   Profiles in court records (allowing to be presented as evidence)                ✗
   Poli-evidence (like multiple-paged document where each page can be an evidence) ✗
   Health system                                                                   ✗
'''

# REMEMBER: quit is for quittin in-game menus, exit for quitting the game

import os
os.system("color")

AA_MODE = None
courtRecords = {}


def checkAndPresentEvidence(choosingMode=False):
    loopingList = [(_, courtRecords[_]) for _ in courtRecords]
    # loopingList is a copy of courtRecords, used for looping
    _ = 0
    while 1:
        print(f'''\033[1;32;m{loopingList[_][0]}\033[0;0m''')
        print(loopingList[_][1])
        q = input().lower()
        if q == 'дальше' or q == 'next':
            if _ == len(loopingList)-1:
                _ = -1
            _ += 1
        elif q == 'раньше' or q == 'prev':
            if _ == 0:
                _ = len(loopingList)
            _ -= 1
        elif q == 'показать' or q == 'present':
            if choosingMode:
                return courtRecords[loopingList[_][0]]
            else:
                print(f'''\033[1;32;mНевозможно показать.\033[0;0m''')
        elif q == 'выйти' or q == 'quit':
            break


def linear(words):
    # words must be a list of tuples (strings, evidence)
    # evidence must be a tuple of (string,string)
    for _ in words:
        print(_)
        q = input().lower()
        if q == 'материалы' or q == 'records':
            checkAndPresentEvidence()
        if AA_MODE and _[2]:
            ans = 'добавлен в материалы дела'
            if _[2][0] not in courtRecords:
                ans = 'обновлён в материалах дела'
            courtRecords[_[2][0]] = _[2][1]
            print(f'''\033[1;32;m{_[2]} {ans}\033[0;0m''')   
            q = input().lower()
            if q == 'материалы' or q == 'records':
                checkAndPresentEvidence()


def choice(choices,
           chooseTimes=1):
    # choices must be a dict of string:list of strings
    for _ in choices:
        print(_, choices[_])
    for _ in range(chooseTimes):
        choice = input()
        if choice in choices:
            linear(choices[choice])


def loopedChoice(choices,
                  splashString='''\033[1;31;47mHOLD IT!\033[0;0m''',
                  splashStringDecisive='''\033[1;31;47mOBJECTION!\033[0;0m'''):
    # choices must be a list of tuples(string, list of strings, bool, evidence - if boolean argument is True)
    i = 0
    while 1:
        print(choices[i][0])
        q = input()
        if q == 'дальше' or q == 'next':
            if i == len(choices) - 1:
                i = -1
            i += 1
        elif q == 'раньше' or q == 'prev':
            if i == 0:
                i = len(choices)
            i -= 1
        elif q == 'здесь' or q == 'here':
            print(splashString if not choices[i][2] else splashStringDecisive)
            linear(choices[i][1])
            if choices[i][2]: # TODO: it must trigger a short conversation then choosing an evidence
                break
        elif q == 'материалы' or q == 'records':
            checkAndPresentEvidence()
