#ex using list comp:

numbers = [1,2,3]
new_list= []
for n in numbers:
    new_n = n+1
    new_list.append(new_n)


# using list comp...

#formula:
#new_list = [new_item for item in list]

new_list = [(n+1) for n in numbers] # this is the same as the above snippet