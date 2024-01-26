import random
n= random.randrange(1,10)
guess = int(input('Enter any number:'))
while n!=guess and guess!=str:
    if guess<n:
        print('Tooo Low!!!')
        guess = int(input("Enter number agian: "))
    elif guess>n:
        print('Tooo High!')
        guess = int(input("Enter number again: "))
    else:
        break
print('You Guessed is Right!!')