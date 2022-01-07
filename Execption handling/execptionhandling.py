'''Unpack the first five countries and store them in a variable nordic_countries, store Estonia and Russia in es, and ru respectively'''
# countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
# fin, sw, nor, *rest = countries
# print(fin, sw, nor, rest)   # Finland Sweden Norway ['Denmark', 'Iceland']
names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']
fin,sw,nor,den,ice, *others = names
nordic_countries = fin,sw,nor,den,ice
print(nordic_countries)
# print(fin,sw,nor,den,ice, others)