# Strings in Python

# Concatenating strings
first_word = 'Thirty'
second_word = 'Days'
third_word = 'Of'
fourth_word = 'Python'
space = ' '
single_string = first_word + space + second_word + space + third_word + space + fourth_word
print(single_string)

#String manipulation
company = 'Coding for all'
print(len(company))
print(company.upper())
print(company.lower())
print(company.swapcase())
print(company.title())
cut = company[7:14]
print(cut)
print(company.find('Coding'))
print(company.replace('Coding','Python'))
sub_string = 'C'
print(company.index(sub_string))
print(company.rindex(sub_string))
sentence_one = 'I am enjoying this challenge \nI just wonder what is next.'
print(sentence_one)
radius = 10
area = 3.14 * radius ** 2
formated_string = 'The area of the circle with a radius {} is {:2f}.'.format(radius,area)
print(formated_string)