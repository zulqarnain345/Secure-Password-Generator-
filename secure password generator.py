import secrets
import string

def genrate_password(length):
    if length <8:
        print(f"PASSWORD IS WEAK..")


    upper=secrets.choice(string.ascii_uppercase)
    lower=secrets.choice(string.ascii_lowercase)
    digit=secrets.choice(string.digits)
    symbol=secrets.choice(string.punctuation)

    total=length-4
    all_chr=string.ascii_letters+string.digits+string.punctuation
    remaning=" ".join(secrets.choice(all_chr) for i in range(total))

    password_list=list(upper+lower+symbol+digit+remaning)
    secrets.SystemRandom().shuffle(password_list)
    return "".join(password_list)

# print(f"THE PASSWORD IS {password}")

password_num=int(input("ENTER HOW MANY PASSWORDS YOU WANT TO GENRATE:: ")
                 )
length=int(input("ENTER THE LENGHT OF THE PASSWORD::  "))

print("GENRATE THE PASSOWRDS")
for i in range(password_num):
    print(f"{i+1} PASSWORD {genrate_password(length)}")








