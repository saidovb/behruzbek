#IF ELSE
"""
#1 Ro'yxatni katta harf bilan boshlash
cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
    if car=='gm':
        print (car.upper())
    else:
        print (car.title())

#2 Yuqoridagini != bilan yechish
for car in cars:
    if car != 'gm':
        print (car.title())
    else:
        print (car.upper())

#3 Login kiritish
login = input("Login kiriting>>")
if login.lower() == "admin":
    print ("Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?")
else:
    print (f"Xush kelibsiz, {login.upper()}, Xozir siz bilan sonlarga doir biroz mashqlar qilamiz")

#4 Sonlar tengmi yoki yoq topish
son1 = input("2 ta son kiriting 👇 \n1-son >>")
son2 = input("2-son >>")
if son1 == son2:
    print ("Bu sonlar teng!")
else:
    print ("Raxmat!")

#5 Son manfiy yoki musbat aniqlash
son = int(input("Son kiriting >>"))
if son > 0:
    print (f"{son} -Musbat son")
elif son == 0:
    print (f"{son} - Musbat xam manfiy xam emas")
else:
    print (f"{son} - Manfiy son")

#6 Ildiz ostini xisoblash
son = int(input("Son kiriting >>"))
if son > 0:
    print (son, "ning ildiz ostisi-", son ** 0.5)
else:
    print ("Musbat son kiriting!")



#BIR NECHTA SHARTLARNI TEKSHIRISH

#1 Juft yoki toq aniqlash
son = int(input("Juft son kiriting >>"))
qoldiq = (son % 2)
if qoldiq == 0:
    print ("Raxmat!")
else:
    print (f"{son} - Juft son emas!")

#2 Yosh kiritib narxini bilish
yosh = int(input("Yoshingiz necha?>>"))
if yosh < 4 or yosh > 60:
    print ("Muzeyga kirish sizga bepul!")
elif yosh < 18 and yosh > 4:
    print ("Kirish 10 000 so'm")
else:
    print ("Kirish 20 000 so'm")

#3 2 ta son katta kichik yoki teng aniqlash
son1 = float(input("2 ta son kiriting👇 \n1- son>>"))
son2 = float(input("2- son>>"))
if son1 > son2:
    print (son1, ">", son2)
elif son1 < son2:
    print (son1, "<", son2)
else:
    print (son1, "=", son2)

#4 Kiritilgan maxsulot ro'yxatda bormi yo'qmi topish
mevalar = ["olma" , "anor" , "nok" , "shaftoli" , "tarvuz" , "qovun" , "uzum" , "anjir" , "banan" , "olcha"]
savat = []
for n in range(5):
    savat.append(input(f"Savatga {n+1}-mevani kiriting>> "))
for meva in savat:
    if meva in mevalar:
        print (f"{meva} do'konimizda bor")
    else:
        print (f"{meva} do'konimizda yo'q")
"""

for son in range (1,51):
    if son % 3 == 0:
        print (son , "-Fizz")
    elif son % 5 == 0:
        print (son , "-Buzz")
    elif son % 3 and son % 5:
        print (son , "-FizzBuzz")