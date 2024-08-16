file = open("text.txt")
content = file.read()
print(content)
file.close()


#or we can do this to auto close file
with open("text.txt") as file:
    content = file.read()
    print(content)

with open("text.txt", mode="a") as file:
    content = file.write("\nNEW TEXT ADDED...")
