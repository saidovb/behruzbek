'''
#manfiy musbat sonlar
sonlar = [5, -3, 9, -8, 2, -6, 7, -1]
manfiy = []
musfat = []

for son in sonlar:
    if son < 0:
        manfiy.append(son)
    else:
        musfat.append(son)

print("Mufbat sonlar", manfiy)
print("Manfiy sonlar", musfat)
'''

#sonlar
sonlar = (int(input("Son kiriting")))
if sonlar<=2 :
    print ("0-2")
elif sonlar<=5 :
    print ("3-5")
elif sonlar<=10 :
    print ("6-10")
elif sonlar<=18 :
    print ("11-18")
elif sonlar<=20 :
    print ("19-20")
elif sonlar<=30 :
    print ("21-30")
elif sonlar<=40 :
    print ("31-40")
elif sonlar<=50 :
    print ("41-50")
elif sonlar<=60 :
    print ("51-60")
else :
    print("61+  ")
