import string


def evaluate_password(password):
    password = password.replace(' ', '')
    al = any(char.isalpha() for char in password)
    di = any(char.isdigit() for char in password)
    sp = any(char in string.punctuation for char in password)
    lo = any(char.islower() for char in password)
    up = any(char.isupper() for char in password)

    print("Password without whitespace ", password)
    print("Password contains Alphabets ", al)
    print("Password contains digits ", di)
    print("Password contains special characters ", sp)
    print("Password with upper case ", up)
    print("Password with lower case ", lo)

evaluate_password("A123@a ")

