import cmath
#Operators in python

#age as an integer
age = 22

#length as a float
length = 155.6

#creating a complex number
i= 7
j= 9
k= complex(i,j)

#area of a triangle with use input
print('Enter the length of the triangle :')
base = float(input())
print('Enter the length of the height :')
height = float(input())

area =0.5 *base * height
print('\nThe area is :',area)

#perimeter of a rectangle
print('Enter the length of the rectangle :')
length =float(input())
print('Enter the width of the rectangle :')
width =float(input())
perimeter = 2 * (length+width)
print('\nThe perimeter is :',perimeter)