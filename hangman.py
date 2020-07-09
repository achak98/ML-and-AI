""" NAME: ABHIRUP CHAKRAVARTY
    REGISTRATION NO: 17BCE7055
    CODE: HANGMAN"""

import random as rn
from collections import Counter

#cities dictionary
cities = '''paris london newyork newdelhi tunis washington kolkata
mumbai chennai nagasaki tokyo beijing shanghai hongkong
austin ahmedabad hyderabad islamabad berlin bangalore jaipur kochi vizag
vijayawada'''

cities = cities.split(' ')

answer = rn.choice(cities)

#main function
if __name__ == '__main__':

    print("Guess the city")

    for i in answer:
        print('-', end=' ')
    print()

    alreadyDone = ''
    tries = len(answer) + 2
    correct = 0
    flag = 0
    try:
       #input
        while(tries != 0) and flag == 0:
            print()

            try:
                ip = str(input('Provide input: '))
                tries -= 1
            except:
                print('Enter only letters, please.')
                continue

            #checker
            if not ip.isalpha():
                print('Enter only letters, please.')
                continue
            elif len(ip) > 1:
                print('Enter only a single letter, please.')
                continue
            elif ip in alreadyDone:
                print('Already done.')
                continue

            #if correct
            if ip in answer:
                ltrFr = answer.count(ip)
                for _ in range(ltrFr):
                    alreadyDone += ip
            #print word
            for ch in answer:
                if (ch in alreadyDone) and (Counter(alreadyDone) != Counter(answer)):
                    print(ch, end=' ')
                    correct += 1
                #if all guessed correctly
                elif(Counter(alreadyDone) == Counter(answer)):
                    print(answer.capitalize())
                    flag = 1
                    print('Bless you.')
                    break
                    break
                else:
                    print('_', end=' ')

        #all chances exhausted
        if tries <= 0 and (Counter(alreadyDone) != Counter(answer)):
            print()
            print('You lost. Try again.')
            print('The word was {}'.format(answer))

    except KeyboardInterrupt:
        print()
        print('Try again.')
        exit()
