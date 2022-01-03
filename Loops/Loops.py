#Loops in Python

'''Iterate 0 to 10 using for loop, do the same using while loop.'''
# while loop
i = 0
while i <11:
    print(i)
    i = i + 1
# for loop
j = (0,1,2,3,4,5,6,7,8,9,10)
for t in j:
    print(t)

'''Iterate 10 to 0 using for loop, do the same using while loop.'''
#while loop
x = 10
while x < 0:
    print(x)
    x=x-1
    if x ==0:
        break
#for loop
me = (10,9,8,7,6,5,4,3,2,1,0)
for u in me:
    print(u)

'''Write a loop that makes seven calls to print(), so we get on the output the following triangle '''
rows =7
for y in range(1,rows +1):
    for z in range(1,y + 1):
        print("#",end=" ")
    print('')
    

for b in range(1,8):
    for c in range(1,8):
        print('#', end='')
    print()