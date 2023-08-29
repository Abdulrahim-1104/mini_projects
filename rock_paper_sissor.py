import  random
import  time
def intro():
    print(' welcome to rock papaper and sissor game '.center(80,'-').title(),end='\n\n')
    print(' game description '.upper().center(80,'-'),end='\n\n')
    print('get 5 points to win the match'.title().center(80,' '))
    print('you are going to play with computer'.title().center(80,' '))
    print('game start now'.title().center(80,' '))
    print('-'*80)

def win(user_point,computer_point):
    if user_point == 5:
        print('Hey ' + user + ' congrats you win the match ...')
        print(user + '-> poor computer....... Haha ')
        return 1
    if computer_point == 5:
        print('Oops computer wins the match')
        print('Computer -> poor ' + user+' Haha')
        return 1
    return 0

if __name__ == '__main__':

    intro()
    user = input('Enter your name : ').title()
    user_point = 0
    computer_point = 0
    dict = {'stone':'sissor','paper':'stone','sissor':'paper'}
    objects = [i for i in dict.keys()]
    while True:
        try:
            if win(user_point,computer_point):
                break

            print(user+' turn \n')
            print('--- Options ---')
            [print(str(i) + ' -> ' + objects[i - 1]) for i in range(1, len(objects) + 1)]
            your_option = objects[int(input('\nEnter your option : '))-1]
            print('Your choosed '+your_option)
            print('\nComputer turn \n')
            computer_option = objects[random.randint(1,3)-1]
            print('Computer choosed ' +computer_option)

            if dict[your_option] == computer_option:
                user_point += 1
                print(your_option+' vs '+computer_option+' --> '+your_option+' wins ')
                print(user+' got ',user_point,' points',end='\n\n')
            elif dict[computer_option] == your_option:
                print(your_option+' vs '+computer_option+' --> '+computer_option+' wins')
                computer_point += 1
                print('Computer got ',computer_point,end='\n\n')
            else:
                print('Tied',end='\n\n')
        except Exception:
            print('Enter the valid input ')