from cryptography.fernet import Fernet


def write_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)


def load_key():
    with open('key.key', 'rb') as key_file:
        key = key_file.read()
    return key


master_pwd = input('What is the master password? ')
key = load_key() + master_pwd.encode()
fer = Fernet(key)


def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passe = data.split('|')
            print('user:', user, '| Password:', str(fer.decrypt(passe.encode())))


def add():
    name = input('Account Name: ')
    pwd = input('Password: ')

    with open('password.txt', 'a') as f:
        f.write(name + '|' + str(fer.encrypt(pwd.encode())) + '\n')


while True:
    mode = input(
        'Would you like to add an a new password or view existing passwords? (view, add, q to quit program)').lower()
    if mode == 'q':
        break

    if mode == 'view':
        view()

    elif mode == 'add':
        add()

    else:
        print('Invalid mode!')
