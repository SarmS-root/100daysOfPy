text1 = []
text2 = []

with open('file1.txt') as f:
    lines = f.readlines()
    stripped = [line.strip() for line in lines]
    text1 = stripped
print(text1)
with open('file2.txt') as f:
    lines = f.readlines()
    stripped = [line.strip() for line in lines]
    text2 = stripped
print(text2)
final=[]

for n in text1:
    for i in text2:
        if n == i:
            final.append(n)
            break
print(final)

result = [int(num) for num in final]

print(result)