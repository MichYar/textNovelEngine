'''
   This text novel engine must run Ace Attorney-like games.
   Must be:
   Linear storylines                                                               ✓
   Linear choices (allowing multiple)                                              ✓
   Looped choices (like AA cross-examinations)                                     ✓
   Court records  (also allowing presenting evidence in cross_examination)         ✗
   Profiles in court records (allowing to be presented as evidence)                ✗
   Poli-evidence (like multiple-paged document where each page can be an evidence) ✗
'''

import os
os.system("color")
AA_MODE = None


def linear(words):
    # words must be a list of strings
    for _ in words:
        print(_)
        input()


def choice(choices,
           choose_times=1):
    # choices must be a dict of string:list of strings
    for _ in range(choose_times):
        choice = input()
        if choice in choices:
            linear(choices[choice])


def looped_choice(choices,
                  splash_string='''\033[1;31;47mHOLD IT!\033[0;0m''',
                  splash_string_decisive='''\033[1;31;47mOBJECTION!\033[0;0m'''):
    # choices must be a list of tuples(string, list of strings, bool)
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
            print(splash_string if not choices[i][2] else splash_string_decisive)
            linear(choices[i][1])
            if choices[i][2]:
                break
