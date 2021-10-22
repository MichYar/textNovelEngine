import os
def linear(words):
    for _ in words:
         print(_)
         os.system("pause")
def choice(choices, choose_times=1):
    for _ in range(choose_times):
        choice = input()
        if choice in choices:
            linear(choices[choice])
            
