"""
Vandalize's Greedy Bash Counter
Version: 1.9
Date: June 27, 2020
Purpose: Displays the number of lockers cleared per pirate
To Be Continued: Ability to acquire score X number of battles ago, not just latest.
"""

from datetime import date
from collections import defaultdict
from os import path

def read_log(filename):
    with open(filename, 'r') as file:
        log = file.readlines()
    return log

def filter_battle(data, battle = 1):
    score = defaultdict(list)
    first = None
    last = None
    keywords = ['performs', 'delivers', 'executes', 'swings']
    for count, line in enumerate(reversed(data)):
        if 'has grappled' in line:
            data = data[len(data)-count+1:]
            break
    for line in data:
        line = line.split()
        if len(line) > 3 and line[2] in keywords:
            if first == None:
                first = line[1]
            score[line[1]] = score.get(line[1], 0) + 1
            last = line[1]
    return (first, last), score

def total_locker(score, current = {}):
    for key, value in score.items():
        current[key] = current.get(key,0) + value
    return current
        #return sum(score.values())

def print_score(battle, score, total = False, loss = 0):
    if total:
        battle -= 1
        print(f'\nTotal Battles: {battle}')
    else:
        print(f'\nBattle No. {battle}:')
    for key, value in sorted(score.items(), key=lambda score: score[1], reverse=True):
        print(f'{key}: {value}')
    print(f'Total Lockers: {sum(score.values())}')

def write_to_file(filename, total):
    header = ['Pirate Name', 'Total Locker']
    with open(filename, 'w+') as file:
        file.write(str(date.today()) + '\n')
        file.write(', '.join(header) + '\n')
        for key, val in total.items():
            file.write(', '.join([key, str(val)]) + '\n')

def single_score(data, battle, overall, loss = 0, RE = False):
    _,score = filter_battle(data)
    # Prints Score
    print_score(battle, score)
    # Asks to Progress include score to running total
    save = input("Result of battle? (win/loss): ")
    if save.lower() == 'win':
        overall = total_locker(score, overall)
        battle += 1
        print("Score was saved!")
    elif save.lower() == 'loss':
        loss = -round(sum(overall.values()) * 0.2 + sum(score.values()))
        overall = total_locker(score, overall)
        overall = total_locker({'Losses':loss}, overall)
        battle += 1
        print("Score was saved!")
    else:
        print("Score was not saved!")
    return (battle,overall,loss)

def score_transform(score):
    freq = defaultdict(dict)
    for key, value in score.items():
        freq[value].append(key)
    print(freq)
    return freq

def snipe_score(data, battle = 1):
    print(f'\nBattle No. {battle} Bragging Rights!')
    keywords = ['performs', 'delivers', 'executes', 'swings']
    special, score = filter_battle(data)
    print(f'First Clear: {special[0]} | Last Clear: {special[1]}\nTop 5:')
    score = dict(sorted(score.items(), key=lambda score: score[1], reverse=True))
    for x in list(score)[0:5]:
        print(f'{x}: {score[x]}')
        #print (f"{x}, {score[x]} ")
    print(f'Total Lockers: {sum(score.values())}')

def menu(filename, output, u_input = 1, battle = 1, total_loss = 0):
    overall = defaultdict(dict)
    print("| Greedy Locker Counter |")
    while u_input != 0:
        try:
            u_input = int(input("\n"
                "1 - Acquire a Single Score\n"
                "2 - Acquire total score\n"
                "3 - Acquire Bragging Rights\n"
                "4 - Update Battles\n"
                "5 - Newly Looted Lockers\n"
                "0 - Quit\n"
                "Please select an option: "))
            if u_input == 1:
                data = read_log(filename)
                battle, overall, loss = single_score(data, battle, overall)
                total_loss += loss
            elif u_input == 2:
                print_score(battle, overall, True, total_loss)
            elif u_input == 3:
                data = read_log(filename)
                snipe_score(data, battle)
                battle += 1
            elif u_input == 4:
                battle = int(input("How many battles has it been?: ")) + 1
            elif u_input == 5:
                looted = int(input("How many lockers looted this battle?: "))
                overall['Looted'] = overall.get('Looted',0) + looted
            elif u_input == 0:
                continue
            else:
                print("Invalid input, please enter an integer provided in the menu!")
        except ValueError:
            print("Invalid input, please enter an integer!")

# Executing Script will automatically call this statement
if __name__ == '__main__':
    pirate_name = input("Enter Bashing Pirate name: ")
    pirate_name = pirate_name.capitalize()
    try:
        log ='/home/malcyan/Documents/Puzzle Pirates Chat Logs/' +pirate_name+ '_emerald_.log'
        path.exists(log)
        menu(log,'/home/malcyan/Documents/Logs/greedy_clear.csv')
    except FileNotFoundError:
        print('File Does Not Exists!')
