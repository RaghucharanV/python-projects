"""Password Authentication is the process of checking the identity of a user. 
Almost every online platform today makes sure that they only give access to the real user which can be only
possible by asking for a password while a user wants to log in to the account"""

username = input("Enter User Name: ")
Database = {"Kittu":'kittu@123', "likith":'liki@434', 'sam':'sam@am','oppi':'op*@'}

count=1
while True:
    if username in Database.keys():
        password = input('Enter password: ')
        if password not in Database[username]:
            count+=1
            if count==3:
                password = input('Enter Password: ')
                break
        else:
            print('Verified')
            break
    else:
        username = input('Enter username')
