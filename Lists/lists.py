# Lists in Python

import statistics
from statistics import mean


companies = ['Facebook','Google','Apple','IBM','Oracle','Amazon']
print(companies)
print(len(companies))
first_company,*rest,sixth_company =companies
print(first_company)
print(rest)
print(sixth_company)
companies [0] = 'Meta'
print(companies) 
does_exist = 'Oracle' in companies
print(does_exist)
companies.sort()
print(companies)
companies.reverse()
print(companies)
companies.append('Netflix')
print(companies)
three_companies = companies[0:3]
print(three_companies)
companies.clear()
print(companies)

front_end= ['HTML','CSS','JS','React','Redux']
back_end = ['Node','Express','MongoDB']
front_end.extend(back_end)
print('Fullstack:',front_end)

ages = [19,22,19,24,20,25,26,24,25,24]
ages.sort()
print(ages)

#Formula for getting the median of ages
print("Median of ages: %s" %(statistics.median(ages)))

#Formula for getting the average of ages
def Average(ages):
    return sum(ages)/len(ages)
average=Average(ages)
print('The average of the ages is:', round(average,2))

#Formula for getting the range of ages
maximum = max(ages)
minimum = min(ages)
Range = maximum - minimum
print('The range of the ages is: {}' .format(Range))
