#Loops in Python

'''Iterate 0 to 10 using for loop, do the same using while loop.'''
i = 0
while i <11:
    print(i)
    i = i + 1

j = (0,1,2,3,4,5,6,7,8,9,10)
for t in j:
    print(t)

'''Iterate 10 to 0 using for loop, do the same using while loop.'''
x = 10
while x < 0:
    print(x)
    x=x-1
    if x ==0:
        break

    