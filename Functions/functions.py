#Functions in Python

'''Declare a function add_two_numbers. It takes two parameters and it returns a sum'''
def add_two_numbers(num_one, num_two):
    sum = num_one + num_two
    return sum
print('Sum of two numbers:',add_two_numbers(2,4))

'''Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle'''
def area_of_circle(radius):
    pie = 3.14
    area = pie *radius**2
    return area
print('Area of a circle:', area_of_circle(7))

'''Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer'''
def check_season(month):
    seasons= ['Autumn','Spring','Summer','Winter']
    if month in ('December','January','February',):
        print('Winter')
    elif month in ('March','April','May'):
        print('Spring')
    elif month in ('June','July','August'):
        print('Summer')
    else :
        print('Autumn')
    return seasons
print('The season is',check_season('April'))