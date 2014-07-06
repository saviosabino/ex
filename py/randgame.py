from random import randrange

def game():    
    random_number = randrange(1, 10)
    count = 0
    print "Welcome to the Guess Game"
    print "Type numbers between 1 to 9"
    while count < 3:
        guess = int(raw_input("enter a guess:"))
        if guess == 0: # hacker mode activated
            hk=raw_input('hacked, n=%s, type y to win:' % random_number)
            if hk == 'y': guess = random_number
        if guess == random_number:
            print "You Win!"
            break
        count += 1
        print 'wrong!'
    else:
        print 'You lose!'

