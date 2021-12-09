# Dictionaries in Python

dog = {'name':'mango',
        'color':'brown',
        'breed':'shiba inu',
        'legs':4,
        'age':8}

print(dog)

student ={'first_name':'Roseland',
        'last_name':'Ambuku',
        'gender':'Female',
        'age': 22,
        'marital_status':'Single',
        'Skills': ['Coding, Knitting'],
        'Country':'Kenya',
        'City':'Kisumu',
        'Address':'19202 Kisumu'}
print(student)
print(len(student))
print(student['Skills'])
student['Skills'].append('Content Writing')
print(student)
keys = student.keys()
print(keys)
values = student.values()
print(values)
tuples = [(i,j) for i,j in student.items()] 
print(tuples)
dog.pop('legs')
print(dog)
del dog
            
