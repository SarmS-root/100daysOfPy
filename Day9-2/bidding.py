import os

users = {}
loop = "yes"


while(loop == "yes"):

    name = input("What is your name?")
    bid = int(input("What is your bid?"))
    loop = input("is there someone else trying to bid?")
    
    users[name]=bid

    os.system('clear')
index = "none"
max = 0
for key in users:
    if users[key] > max:
        max = users[key]
        index = key

print(f"Winner is {index}, with a bid of {max}")
