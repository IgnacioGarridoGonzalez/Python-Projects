text = input('Input the information you wish to encrypt: ')
passw = input('\nEnter your password: ')

access = input('\nTo access the information, type the password. \n(You have 3 attempts): ')

i = 0
if passw == access:
    print('The encrypted text is: ', text)
else:
    while i <= 1 and passw != access:
        i = i + 1
        print('\nThe password is incorrect!\n(Attempt', i+1, 'out of 3)') 
        access = input('Try again: ')
    if access == passw:
        print('\nThe encrypted text is: ', text)
    else:
        print('\nYou ran out of attempts. The information is locked.\n')