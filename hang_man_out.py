import random
hang_man = ['','','','']
length = 9
def hang_man_position(hang_man,attempts):
    if attempts == 1:
        hang_man[0] = '-'*length
        print(str(10-attempts) +' attempts left')
    elif attempts == 2:
        hang_man[1] = '0'.center(length)
        print(str(10-attempts) + ' attempts left')
    elif attempts == 3:
        hang_man[2] = '|'.center(length)
        print(str(10-attempts) + ' attempts left')
    elif attempts == 4:
        hang_man[3] = '/  '.center(length)
        print(str(10-attempts) + ' attempts left')
    elif attempts == 5:
        hang_man[3] = '/ \\'.center(length)
        print(str(10-attempts) + ' attempts left')
    elif attempts == 6:
        hang_man[1] = '\\ 0  '.center(length)
        print(str(10-attempts) + ' attempts left')
    elif attempts == 7:
        hang_man[1] = '\\ 0 /'.center(length)
        print(str(10-attempts) + ' attempts left')
    elif attempts == 8:
        hang_man[1] = '\\ 0 /|'.center(length)
        print(str(10-attempts ) + ' attempts left')
    elif attempts == 9:
        hang_man[1] = '\\ 0_|/'.center(length)
        print(str(10-attempts) + ' attempts left')
        print('Last breaths counting. Take care!')

    elif attempts == 10:
        hang_man[1] = ' 0_|'.center(length)
        hang_man[2] = '/|\\'.center(length)
        print('You loose......')
        print('You let a man die.........:(')
    else:
        pass
# Main implementation
fruits = ["apple", "banana", "orange", "grape", "strawberry", "watermelon", "pineapple", "mango", "pear", "kiwi", "cherry", "blueberry", "raspberry", "peach", "plum", "lemon", "lime", "fig", "pomegranate", "apricot", "coconut", "grapefruit", "cranberry", "blackberry", "melon", "dragonfruit", "guava", "papaya", "passion fruit", "lychee"]
random_no = random.randint(1,len(fruits)-1)
the_fruit = fruits[random_no]
attempts = 0
word = '_'*len(the_fruit)
user_name = input('Enter your name :')
print('Hi! '+user_name+' Welcome to the game :)')
print('===================')
print('Try to find the fruit name less than 10 attempts')
print(the_fruit)
while(attempts!=10):
    print('Guess the fruit word : '+word)
    user_char = input()
    if user_char in the_fruit:
        word = word[:the_fruit.index(user_char)]+user_char+word[the_fruit.index(user_char)+1:]
        the_fruit = the_fruit[:the_fruit.index(user_char)]+' '+the_fruit[the_fruit.index(user_char)+1:]
    else:
        attempts+=1
    if attempts!=0:
        hang_man_position(hang_man,attempts)
        for i in hang_man:
            print(i)
    if word == fruits[random_no]:
        print('You won...')
        print('You save a man')
        break
