#figuring whether win or not
def win_or_not(tic_tac_toe):
    #checking in horizondal and vertical
    for x in range(1,6,2):
        horizondal=''
        vertical=''
        for y in range(3,12,4):
            horizondal+=tic_tac_toe[x][y]
            vertical+=tic_tac_toe[y//2][x*2+1]
        if horizondal.count('X')==3 or horizondal.count('O')==3 or vertical.count('X')==3 or vertical.count('O')==3:
            return True

    #checking for diagnol
    backslash = ''.join([tic_tac_toe[back][back*2+1] for back in range(1,6,2)])
    forwordslash = ''.join(tic_tac_toe[i][j] for i,j in zip(range(1,6,2),range(11,2,-4)))
    if backslash.count('X')==3 or backslash.count('O')==3:
        return True
    if forwordslash.count('X')==3 or forwordslash.count('O')==3:
        return True
    return False
#displaying game
def display(tic_tac_toe):
    for i in tic_tac_toe:
        print(i)
#main code
print('Hello welcome to the tic tac toe game ')
print('========================================')
tic_tac_toe = ['   1   2   3','1    |   |   ','  ---+---+---','2    |   |   ','  ---+---+---','3    |   |   ']
count = 1
win = False

while(count<=9):
    char = 'X' if count % 2 != 0 else 'O'
    print((char+' Turns').center(len(tic_tac_toe[0])+3))
    display(tic_tac_toe)

    x, y = input('Enter the coordinates to x and y seprated with space :').split()
    x, y = int(x) - 1 + int(x), int(y) + (int(y) * 3) - 3 + 2

    if x > len(tic_tac_toe)-1 or y > len(tic_tac_toe[0])-1:
        print('The coordinates is must less than 3')
    else :

        if tic_tac_toe[x][y] != ' ':
            print('This coordinates already filled with ' + tic_tac_toe[x][y] + ' try different coordinates')
        else:
            tic_tac_toe[x] = tic_tac_toe[x][:y] + char + tic_tac_toe[x][y+1:]
            count+=1
            if count>5:
                if win_or_not(tic_tac_toe):
                    win = True
                    display(tic_tac_toe)
                    print('Player '+char+' Win The Match...')
                    break
if not win :
    print('Game Tied......!')
