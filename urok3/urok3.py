from random import randint
s = [1, 2, 5 ,4 , 88]
spisok = list()
for i in range(10):
    spisok.append(randint(-100,100))
print(spisok)
spisok[5]
for i in spisok:
    if i%2==1:
        print(i)

#spisok_1 = [1, 2, 3, ["Hello", "1234"], 'piano']
#spisok_1.insert(5,['qwerty'])
#print(spisok_1)
"""
for i in range(10):
    spisok.append(i+1)
print(spisok)
"""
#spisok = [i+1 for i in range(10)]
#print(spisok)