# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key,value) in dict.items()}




#THIS IS TO ITERATE OVER DICT:
# d = {'x': 1, 'y': 2, 'z': 3}

# for key in d:
#     print(key, 'corresponds to', d[key])

import random

names = ["Dave", "Alex", "Ellie", "Joel"]

students_grades = { student:random.randint(1,100) for student in names}
# makes dict for students with random grades 

print(students_grades)

passed_students = {student:grade for (student,grade) in students_grades.items() if grade >=50}   # check each student, if grade is more than 50 add them into new list
print(passed_students)

##########################3
# /////////
weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

weather_f = {days:((temp * 9/5) + 32) for (days,temp) in weather_c.items()}

print(weather_f)




# //side note looping through dict:

for (key, value) in dict.items():
	print(key + value)

dict = {}
import pandas
df = pandas.DataFrame(dict)
# //pandas df iteraion:   (ROW: Key Value)
for (index, row) in df.iterrows():
	print(row.key + row.value)