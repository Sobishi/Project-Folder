from cryptography.fernet import Fernet #allows to encrypt text files
#NB always define a function before you use it.

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key","wb")as key_file:
        key_file.write(key)'''


def load_key():
    file = open("key.key","rb")
    key = file.read()
    file.close()
    return key

key = load_key()
fer = Fernet(key)



def view(): #whatever is indented happens when you call view() function
    with open("passwords.txt", "r") as f: #"a" "w" "r"mode "with" keyword automatically closes the file.
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("Username:", user, "| Password:", fer.decrypt(passw.encode()).decode()) #splits data into username and password using the "|" as seperator

def add(): #create a new file if the password does not exist and add new password
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open("passwords.txt", "a") as f: #"a" "w" "r"mode "with" keyword automatically closes the file.
        f.write(name, "|", fer.encrypt(pwd.encode().decode))

while True:

    mode = input("would you like to add a password or view old ones (view, add)? or Q to quit ").lower()

    if mode == "q":
        break

    if mode == "view":
        view()

    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue
