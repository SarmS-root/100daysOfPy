def encrypt(text, shift):
    sol = ""
    for char in text:
        if char == " ":
            sol = sol+(" ")
        else:
            i = 0
            while i <= 25:
                if alpha[i] == char:
                    position = i
                i += 1 
            new = (position + shift)%26
            sol = sol+(alpha[new])
    print(f"encrypted text in rot{shift} is: {sol}")

def decrypt(text, shift):
    sol = ""
    for char in text:
        if char == " ":
            sol = sol+(" ")
        else:
            i = 0
            while i <= 25:
                if alpha[i] == char:
                    position = i
                i += 1 
            new = (position - shift)%26
            sol = sol+(alpha[new])
    print(f"decrypted text in rot{shift} is: {sol}")
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if (direction == "encode"):
    encrypt(text,shift)
elif(direction == "decode"):
    decrypt(text,shift)