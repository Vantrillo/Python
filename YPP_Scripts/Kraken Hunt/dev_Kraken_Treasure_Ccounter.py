"""
Vandalize's Greedy Bash Counter
Version: 1.8
Date: June 27, 2020
Purpose: Displays the number of lockers cleared per pirate
To Be Continued: Ability to acquire score X number of dips ago, not just latest.
"""

from datetime import date
from collections import defaultdict
from operator import itemgetter

# Executing Script will automatically call this statement
if __name__ == '__main__':
    menu('/home/malcyan/Documents/Logs/Vandalize_emerald_1',
        '/home/malcyan/Documents/Logs/kraken_treasure.csv')

def read_log(filename):
    with open(filename, 'r') as file:
        log = file.readlines()
    return log

def filter_dip(data, dip = 1):
    score = defaultdict(dict)
    dip_count = 1
    end = len(data)-1
    keywords = {'Egg':'loaded 1 kraken\'s egg safely aboard',
        'Ink':'loaded 1 unit of kraken\'s ink safely aboard',
        'Pod':'loaded 1 cephalo pod safely aboard',
        'Locker':'loaded 1 tentacle locker safely aboard',
        'Box':'loaded 1 cuttle box safely aboard'}
    # Separate data by dips
    for count, line in enumerate(reversed(data)):
        if 'A displeased kraken dips into the dark depths and disappears' in line:
            if dip_count == dip:
                start = count
                data = data[start:end]
            else:
                dip_count += 1
                end = count
            break

    for line in data:
        if len(line) < 3:
            continue
        for key, value in keywords.items():
            if value in line:
                treasure_counter(score, line, key)
    return score

def treasure_counter(score, line, keyword):
    line = line.split()
    score[keyword][line[1]] = score.get(keyword, {}).get(line[1], 0) + 1
    return score

def total_treasure(score, current = defaultdict(dict)):
    for key, value in score.items():
        for key2, value2, in value.items():
            current[key][key2] = current.get(key,{}).get(key2, 0) + score[key][key2]
    return current
    #return sum(score.values())

def print_score(dip, score, total = False):
    if total:
        dip -= 1
    print(f'\nDip: {dip}', end = '')
    for key, value in score.items():
        print(f'\n{key}: ', end = '')
        for count, (key2, value2) in enumerate(dict(sorted(value.items(), key=itemgetter(1),reverse=True))):
            if count < len(value)-1:
                print(f'{key2} = {value2}', end = ", ")
            else:
                print(f'{key2} = {value2}', end = "")
    #print(f'Total: {sum(score.values())}')

def write_to_file(filename, total):
    header = ['Pirate Name', 'Total Locker']
    with open(filename, 'a+') as file:
        file.write(str(date.today()) + '\n')
        file.write(', '.join(header) + '\n')
        for key, val in total.items():
            file.write(', '.join([key, str(val)]) + '\n')

def single_score(data, dip, overall):
    score = filter_dip(data)
    # Prints Score
    print_score(dip, score)
    # Asks to Progress include score to running total
    save = input("\nDo you want to save score? (yes/no): ")
    if save.lower() == 'yes':
        overall = total_treasure(score, overall)
        dip += 1
        print("Score was saved!")
    else:
        print("Score was not saved!")
    return (dip,overall)

def menu(filename, output, u_input = 1, dip = 1):
    overall = defaultdict(dict)
    print("| Kraken Hunt Treasure Counter |")
    while u_input != 0:
        try:
            u_input = int(input("\n\t"
                "1 - Acquire Treasure Count for 1 dip\n\t"
                "2 - Acquire Treasure Count for Entire KH\n\t"
                "0 - Quit\n"
                "Please select an option: "))
            if u_input == 1:
                data = read_log(filename)
                dip, overall = single_score(data, dip, overall)
                #dip, overall = single_score(data, dip, overall)
            elif u_input == 2:
                print_score(dip, overall, True)
                #write_to_file(output, overall)
            elif u_input == 0:
                continue
            else:
                print("Invalid input, please enter an integer provided in the menu!")
        except ValueError:
            print("Invalid input, please enter an integer!")
