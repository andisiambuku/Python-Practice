# Operators in Python
it_companies = {'Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon'}
print(len(it_companies))
it_companies.add('Twitter')
print(it_companies)
it_companies.update(['Discord','Clubhouse','Twitch'])
print(it_companies)
it_companies.remove('Twitch')
print(it_companies)


A = {19,22,24,20,25,26}
B = {19,22,20,25,26,24,28,27}
C = A.union(B)
print(C)
A.intersection('B')
A.issubset('B')
A.isdisjoint('B')
# B.join('A')
# A.join('B')
A.symmetric_difference('B')
del C


age = [22,19,24,25,26,24,25,24]
print(len(age))
age = set(age)
print(age)
print(len(age))

# words = 'I am a teacher and I love to inspire and teach people'
# words_string = words.split('')
# unique_words =[] 
# for word in words_string:
#     if word not in unique_words:
#         unique_words.append(words)
# unique_words.sort()
# print(unique_words)
