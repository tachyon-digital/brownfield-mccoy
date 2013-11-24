__author__ = 'George Spiceland'

#This Py is a beginning and introductory Py to cover basic functions and terms for use with Python 3.3.2.


#A basic function for determing if users are new users or returning users.
def login_menu():
    #Just an interesting introduction here that explains the options.
    print('Welcome to Brownfield-McCoy\n' 'This is a game of skill\n')
    print('If you have played before, choose 1.) Existing User\n'
          'If you have never played before, choose 2.) New User\n')
    while True:
        #While loop allows for us to force players to answer correctly.
        next = input('Have you played before? >')
        if next == '1':
            #If statement here checks if players are returning...
            print('A returning player! Excellent.')
            return 'old'
        elif next == '2':
            #Else-if statement here checks if players are new.
            print ('A new player, how wonderful.')
            return 'new'
        else:
            #Else statement here re-runs the loop and gives an error code.
            print("I'm sorry, but that isn't an option.")


#A basic function for requesting the user's name.
def ask_name(prompt, min_length, max_length, complaint):
    #While loop waits for user to input a name with proper length.
    while True:
        usr_name = input(prompt)
        if min_length <= len(usr_name) <= max_length:
            #If statement tests whether or not name is usable length.
            print('Thank you, {}'.format(usr_name))
            return usr_name
        else:
            #Else statement asks user to re-enter username to where it's correct length.
            print(complaint)


#A basic function for requesting the user's password.
def ask_pass(prompt, min_length, max_length, complaint):
    #While loop waits for user to input a password with proper length.
    while True:
        usr_pass = input(prompt)
        if min_length <= len(usr_pass) <= max_length:
            #If statement tests whether or not password is usable length.
            print('You will use {} as your password.'.format(usr_pass))
            return usr_pass
        else:
            #Else statement asks user to re-enter password to where it's correct length.
            print(complaint)


#Function writes information to a file. Currently can only write info to target file
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
    print('File Written Successfully!')


def new_player_get():
    print("Now we'll set you up with an account.")
    usr_name = ask_name("What's your name, new user? >", 6, 20, "Must be between 6 and 20 characters!")
    usr_pass = ask_pass("What's your password, new user? >", 6, 20, "Must be between 6 and 20 characters!")
    write2file(usr_name,'files/credentials.txt','0')
    write2file(usr_pass,'files/credentials.txt','n')
    return usr_name

def old_player_get():
    pass


user_type = login_menu()
if user_type == 'new':
    active_player = new_player_get()
else:
    active_player = 'old'
print(active_player)

#print(usr_name)
#print(usr_pass)