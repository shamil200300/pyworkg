import random
spisok = ['волк', 'тигр', 'олень', 'крыса']
random_slovo = random.randrange(len(spisok))
j0 = "волк"
j1 = "тигр"
j2 = "олень"
j3 = "крыса"
h = "УЗНАТЬ"
c0 = spisok[0]
c1 = spisok[1]
c2 = spisok[2]
c3 = spisok[3]
a = (spisok[random_slovo])

print("Угадай слово")

if j0 in a :
    print("живет в лесу , серая шерсть") 
elif j1 in a :
    print("полосатый , оранжево черный , похож на льва") 
elif j2 in a :
    print("длиные и красивый рога") 
elif j3 in a :
    print("похожа на мышь") 

b = input()
if a in b :
    print("ты угадал",'Твое слово было :',a)
else :
    print("ты не угадал",'Твое слово было :',a)


