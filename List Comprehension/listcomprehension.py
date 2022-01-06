#List comprehension in Python
'''Filter only negative and zero in the list using list comprehension'''
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_numbers = [i for i in range(10) if i > -1]
print(negative_numbers)

'''Flatten the following list of lists of lists to a one dimensional list '''
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattened_list = [numbers for row in list_of_lists for numbers in row]
print(flattened_list)
'''Flatten the following list to a new list'''

