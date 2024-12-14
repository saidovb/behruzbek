#20 ta list va dictionaryga oid masalar
sonlar = [4,62,17,97,36,18,82]
malumot = {
            'ism':'Behruzbek',
            'yosh':14,
            'tuman':'xonqa'
           }
mevalar = {
    "olma"
    "anor"
    "apilsin"
    "banan"
    "uzum"
}

#1
my_list = []
my_list.append(2)
my_list.append(5)
my_list.append(7)
my_list.append(10)
my_list.append(12)
print(my_list)

#2
print(sonlar[2])

#3
print(sum(sonlar))

#4
toq = []
for son in sonlar:
    if son % 2 ==1:
        toq.append(son)
print(toq)

#5
print(max(sonlar))

#6
kopaytma = []
for number in sonlar:
    kopaytma.append(number*2)
print(kopaytma)

#7
sonlar.remove(17)
print(sonlar)

#8
sonlar.reverse()
print(sonlar)

#9
malumot = {'ism':'Behruzbek','yosh':'14','tuman':'xonqa'}

#10
if 'yosh' in malumot:
    print(malumot['yosh'])
else:
    print("Bunday kalit topilmadi")

#11
juft = []
summa = 0
for son in sonlar:
    if son % 2 == 0:
        juft.append(son)
        summa = summa+1
print(len(juft))
print(summa)

#12
for son in sonlar:
    if son % 2 == 0 and son % 3 == 0:
        print(f"{son}- 2ga va 3ga bo'lianadi")

#13
sonlar.sort()
print(sonlar)

#14
if malumot['ism'] == "Behruzbek":
    print(int(malumot['yosh'])+1)

    
#Sonlarni joylashuvini aniqlash
sonlar = (int(input("Son kiriting>> ")))
if sonlar<=2:
    print ("0-2")
elif sonlar<0:
    print ("-")
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
    print("61+")

    
#3ga, 5 ga va ikkalasiga ham bo'linuvchi sonlar
son3 = []
son5 = []
none = []
for son in range (1,51):
    if son % 3 == 0 and son % 5 != 0:
        son3.append(son)
    elif son % 5 == 0 and son % 3 != 0:
        son5.append(son)
    elif son % 3 and son % 5:
        none.append(son)
print (f"3 ga bo'linuvchilar- {son3}")
print (f"5 ga bo'linuvchilar- {son5}")
print (f"Xech biriga bo'linmaydiganlar- {none}")


#Parol to'g'rimi noto'g'rimi tekshirish
parol = input("Kirish Parolini Kiriting>> ")
if parol =="1191":
    print ("Front-end\Stroy-city\-stroy-siti.html - KIRISHINGIZ MUMKIN!")
else:
    print("Parol noto'g'ri. Qaytadan urining")

    
#Login orqali parolni topish
malumot = {
    'saidov.mee':'saidov.b10',
    'mansurvich.10':'mnsrvch12345', 
    'bekhruz.001':'bekhruz.001',
    'mansurvich.01':'saidovb1111',
    'my.world.uzb':'myworlduzb',
    'coding.zone.uz':'coding.zone.uz2010'
}
holat = True
savol = str(input('Login kiriting>> ')).lower()

for login, parol in malumot.items():
    if savol == login:
        print(f"Login- {login}")
        print(f"Parol- {parol}")
        holat = False
if holat:
    print("Bunday login topilmadi")


#Balga qarab baxo berish
ball = float(input("Balingizni kiriting>> "))
if ball >= 90 and ball <= 100:
    print("A")
elif ball >= 80 and ball < 90:
    print ("B")
elif ball >= 70 and ball < 80:
    print ("C")
elif ball >= 60 and ball < 70:
    print ("D")
elif ball < 60 and ball > 0:
    print ("F")
else:
    print ("Bunday ball yo'q!")

    
#O'lchov birliklarini o'zgartirish
qiymat = float(input("O'lchovni qiymatini kiriting>> "))
birlik = str(input("O'lchov birligini kiriting(mm, sm, m, km)>> "))
if birlik.lower() == "mm":
    print(f"-{qiymat} mm"
          f"\n{qiymat / 10} sm"
          f"\n{qiymat / 1_000} m"
          f"\n{qiymat / 1_000_000} km")
elif birlik.lower() == "sm":
    print(f"-{qiymat} sm-"
          f"\n{qiymat * 10} mm"
          f"\n{qiymat / 100} m"
          f"\n{qiymat / 100_000} km")
elif birlik.lower() == "m":
    print(f"-{qiymat} m-"
          f"\n{qiymat * 1_000} mm"
          f"\n{qiymat * 100} sm"
          f"\n{qiymat / 1_000} km")
elif birlik.lower() == "km":
    print(f"-{qiymat} km-"
          f"\n{qiymat * 1_000_000} mm"
          f"\n{qiymat * 100_000} sm"
          f"\n{qiymat * 1_000} m")
else:
    print("Noto'g'ri birlik kiritildi. Iltimos, mm, sm, m, yoki km kiriting")

        
#Do'stlar ro'yxatini tuzish
ismlar = []
print("Yaqin do'stlaringiz ro'yxatini tuzamiz.")
n=1 # ismlarni sanash uchun o'zgaruvchi
while True:
    savol = f"{n}-do'stingiz ismini kiriting:"
    ism = input(savol)
    ismlar.append(ism)
    javob = input("Yana ism qo'shasizmi? (ha/yo'q)")
    if javob =='ha':
        n+=1
        continue
    else:
        break
print (ismlar)


#Do'stlarni yoshlari bn lug'at tuzish
print("Do'stlaringiz yoshini saqlaymiz.")
dostlar = {}
ishora = True
while ishora:
    ism = input("Do'stingiz ismini kiriting: ")
    yosh = input(f"{ism.title()}ning yoshini kiriting: ")
    dostlar[ism] = int(yosh) # ism kalit, yosh qiymat
    javob = input("Yana ma'lumot qo'shasizmi? (ha/yo'q)")
    if javob == "yo'q":
        ishora = False
for ism, yosh in dostlar.items():
    print ("Do'stlaringizning yoshlari:")
    print(f"{ism.title()} {yosh} yoshda")

    
#Ro'yxatdan bir xil elementlarni o'chirish
cars = ['lacetti','nexia','toyota','nexia','audi','malibu','nexia']
while 'nexia' in cars:
    cars.remove('nexia')
print(cars)


#Talabalarni baholash
talabalar = ['Behruzbek', 'Sherzod', 'Shamshod', 'Nurik' , "Zohid"]
baholangan_talabalar = {}
while talabalar:
    talaba = talabalar.pop()
    baho = input(f"{talaba.title()}ning bahosini kiriting: ")
    print(f"{talaba.title()} baholandi")
    baholangan_talabalar[talaba] = baho

    
#Yaqin do'stlar ro'yxati
ismlar = []
print("Yaqin do'stlaringiz ro'yxatini tuzamiz.")
n=1 # ismlarni sanash uchun o'zgaruvchi
while True:
    savol = f"{n}-do'stingiz ismini kiriting: "
    ism = input(savol)
    ismlar.append(ism)
    javob = input("Yana ism qo'shasizmi? (ha/yo'q)")
    if javob =='ha':
        n+=1
        continue
    else:
        break
for ism in ismlar:
    print (ism)

        
#Do'kondagi maxsulotlarni narxi
dokon = {
    "Olma": 25000,
    "Banan": 18000,
    "Apelsin": 30000,
    "Nok": 22000,
    "Qovun": 50000,
    "Uzum": 40000,
    "Limon": 15000,
    "O'rik": 28000,
    "Saftoli": 32000,
    "Tarvuz": 45000,
    "Non": 10000,
    "Pishloq": 45000,
    "Sut": 20000,
    "Yog'": 17000,
    "Tuxum": 35000,
    "Makaron": 20000,
    "Guruch": 15000,
    "Kartoshka": 10000,
    "Sabzi": 9000,
    "Lavash": 12000,
    "Cola": 10000,
    "Suv": 5000,
    "Pepsi": 25000,
    "Choy": 15000,
    "Kofe": 18000,
    "Aroq": 70000,
    "Fanta": 12000,
    "Sigaret": 13000,
    "Yogurt": 22000,
    "Shokolad": 28000,
    "Nos": 2000,
    "Somsa": 7000,
    "Shashlik": 7000,
    "Ruchka": 3000,
    "Televizor": 1500000,
    "Telefon": 2000000,
    "Printer": 400000,
    "Yostiq": 80000,
    "Gamburg": 20000,
    "Diapazon": 100000,
    "Poyabzal": 200000,
    "Kurtka": 250000,
    "Sharf": 50000,
    "Ko'ylak": 120000,
    "Iphone": 14450000,
    "Anor": 300000,
    "Kurtka": 450000,
    "Shlyapa": 70000,
    "Ko'ylak": 150000
}
savat = {}
yoq = []
while True:
    maxsulotlar = input("Maxsulot kiriting>> ").capitalize()
    add = input("Yana maxsulot qo'shasizmi? (ha/yo'q)")
    for maxsulot,narx in dokon.items():
        if maxsulotlar == maxsulot:
            savat[maxsulotlar] = narx
    if add == "yo'q":
        yoq.append(maxsulotlar)
        for borlar,narxi in savat.items():
            print (f"{borlar}ning narxi {narxi} so'm")
        for yoqlar in yoq:
            print(f"Bizda {yoqlar} yo'q")
        break
    else:
        continue


#Son topish o'yini
import random
son = "Men o'ylagan 1 dan 10 gacha sonni toping>> "
tugri_son = random.randint(1, 10)
while True:
    savol = int(input(son))
    if savol == tugri_son:
        print ("To'g'ri topdingiz!!!")
        break
    else:
        print("Xato Qaytadan uruning")


class Bank:
    def __init__(self, foydalanuvchi, xisob = 0):
        self.foydalanuvchi = foydalanuvchi
        self.xisob = xisob
    
    def foydalanuvchi_nomi(self):
        print(f"Foydalanuvchi nomi - {self.foydalanuvchi}")

    def balans(self):
        print(f"Xisobingizda {self.xisob} so'm pul bor")

    def pul_qoshish(self, miqdor):
        self.xisob += miqdor
        if miqdor >= 20_000_000:
            bonus = miqdor * 0.5 /100
            self.xisob += bonus
            print (f"Xisobingizga {miqdor} so'm qo'shildi va bonus sifatida {bonus} so'm qo'shildi")
        else:
            print (f"Xisobingizga {miqdor} so'm qo'shildi")

    def pul_yechish(self, miqdor):
        if self.xisob >= miqdor:
            self.xisob -= miqdor
            print(f"Xisobingizdan {miqdor} so'm yechib olindi")
        else:
            print("Xisobingizda yetarli mablag' yo'q")

    def pul_otgazish(self, miqdor, boshqa_foydalanuvchi):
        if self.xisob >= miqdor:
            boshqa_foydalanuvchi.xisob += miqdor
            self.xisob -= miqdor
            print(f"{boshqa_foydalanuvchi.foydalanuvchi} xisobiga {miqdor} so'm o'tkazildi")
        else:
            print("Mablag' yetarli emas")

behruzbek = Bank("Behruzbek")
shaxruza = Bank("Shaxruza")


