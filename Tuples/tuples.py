# Tuples in Python

#creating empth tuple
empty = ()

sisters = ( 'Jill','Cynthia')
brothers = ('Jack','Tom',)
siblings = sisters + brothers
print(siblings)
print(len(siblings))
siblings = list(siblings)
print(siblings)
parents = ['Nancy', 'John']
family_members= parents + siblings
print(tuple(family_members))
del family_members

fruits = ('mangoes','oranges','bananas','watermelon')
vegetables = ('beetroot','carrots','cucumber','onions')
animal_products = ('liver','eggs','fillet','sausages')
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)
food_stuff_list = (list(food_stuff_tp))
print(food_stuff_list)
first_three_foods = food_stuff_list[:3]
last_three_foods = food_stuff_list [-3:]
print(first_three_foods)
print(last_three_foods)
del food_stuff_tp
