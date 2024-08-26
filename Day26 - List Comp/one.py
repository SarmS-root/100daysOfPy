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

num = range(1,5)

range_list = [n*2 for n in num]
print(range_list)

#conditional 
#new_list = [(n+1) for n in numbers if test] # this is the same as the above snippet

#example

names = ["Eleanor", "Joel", "Isabella" , "Tim" , "George"]
short_name = [name for name in names if len(name) <= 4]
print(short_name)


upper_case = [name.upper() for name in names]
print(upper_case)
