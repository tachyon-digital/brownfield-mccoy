__author__ = 'George Spiceland'
#Brownfield-McCoy is a game of skill based on trying to think through often complicated and multi-layered problems
#in an attempt to access secured networks. It is also a training field for Python for the Tachyon-Digital team.

#This Py is a beginning and introductory Py to cover basic functions and terms for use with Python 3.3.2.
import hashlib
import getpass


#A basic function for determining if users are new users or returning users.
def login_menu():
    #Just an interesting introduction here that explains the options.
    print('Welcome to Brownfield-McCoy\n' 'This is a game of skill\n')
    print("Tell me if you are a [new] player, or a [returning] one.\n")
    while True:
        #While loop allows for us to force players to answer correctly.
        next_act = input('Have you played before? >')
        #If statement here checks if players are returning...
        if next_act in ('n', 'ne', 'new', 'N', 'NE', 'NEW', 'Ne', 'New'):
            return 'new'
        elif next_act in ('r', 're', 'ret', 'retu', 'retur', 'return', 'returni', 'returnin', 'returning', 'R',
                          'RETURNING'):
            return 'old'
        else:
            print("Sorry, I don't understand.")


#A basic function for requesting the user's information.
def ask_info(prompt, min_length, max_length, complaint, password):
    #While loop waits for the user to input the requested information.
    while True:
        if password == 'y':
            usr_info = getpass.getpass(prompt)
        else:
            usr_info = input(prompt)
        if min_length <= len(usr_info) <= max_length:
            #If statement tests whether or the the info is usable length.
            print('Thank you.')
            return usr_info
        else:
            #Else statement asks user to re-enter info to where it's correct length.
            print(complaint)


#Function writes information to a file. Currently can only write info to target file.
def write2file(info_written, target_file, newline):
    #With statement opens file as [f] for use inside function. Automatically closes file.
    with open(target_file, 'a') as f:
        #Write statement adds file to end of file due to 'a' modifier in open.
        f.write(info_written)
        if newline == 'n':
            #Write statement adds a newline character to end of file.
            f.write('\n')
        else:
            f.write(' ')


#Function reads information from a file. Currently can only read info from target file.
def read0file(target_file):
    #With statement opens file as [f] for use inside function. Automatically closes file.
    with open(target_file, 'r') as f:
        #Read statement reads file.
        temp_nfo = f.read()
    return temp_nfo


#Function uses ask_info function to get new user's name and password.
def new_player_get():
    #Prints the account creation intro.
    print("Now we'll set you up with an account.")
    #Calls the usr_info function.
    usr_n = ask_info("What's your name, new user? >", 6, 20, "Must be between 6 and 20 characters!", 'n')
    usr_p = ask_info("What's your password, new user? >", 6, 20, "Must be between 6 and 20 characters!", 'y')
    #Creates a hash using sha256 encoding.
    h = hashlib.sha256()
    #Updates the hash using the user's password and then user's name.
    h.update(usr_p.encode(encoding='utf-8', errors='strict') + usr_n.encode(encoding='utf-8', errors='strict'))
    usr_h = h.hexdigest()
    #Writes the hash to the credentials file, including the newline.
    write2file(usr_h, 'files/credentials.txt', 'n')
    return usr_n


#Function uses ask_info function to get returning user's name and password.
def old_player_get():
    #Prints the returning user intro.
    print("Welcome back, Enter your credentials to log in.")
    #Calls the usr_info function.
    while True:
        usr_n = ask_info("Provide your login name. >", 6, 20, "Must be between 6 and 20 characters!", 'n')
        usr_p = ask_info("Provide your login password. >", 6, 20, "Must be between 6 and 20 characters!", 'y')
        #Creates a hash using sha256 encoding.
        h = hashlib.sha256()
        #Updates the hash using the user's password and then user's name.
        h.update(usr_p.encode(encoding='utf-8', errors='strict') + usr_n.encode(encoding='utf-8', errors='strict'))
        usr_h = h.hexdigest()
        #Checks the info against the credentials file.
        temp_info = read0file("files/credentials.txt")
        if usr_h in temp_info:
            print('Welcome back ', usr_n)
            return usr_n
        else:
            print("Sorry, I can't find your records, try again.")


user_type = login_menu()
if user_type == 'new':
    active_player = new_player_get()
else:
    active_player = old_player_get()
print("Successfully logged you in, ", active_player, ".")
