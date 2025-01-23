from uuid import uuid4
import math
import random
def uuide():
    return str(uuid4().hex[:5])

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
sonlar = int(input("Son kiriting>> "))
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
if parol =="1100":
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
    print(f"{qiymat} mm-"
          f"\n{qiymat / 10} sm"
          f"\n{qiymat / 1_000} m"
          f"\n{qiymat / 1_000_000} km")
elif birlik.lower() == "sm":
    print(f"{qiymat} sm-"
          f"\n{qiymat * 10} mm"
          f"\n{qiymat / 100} m"
          f"\n{qiymat / 100_000} km")
elif birlik.lower() == "m":
    print(f"{qiymat} m-"
          f"\n{qiymat * 1_000} mm"
          f"\n{qiymat * 100} sm"
          f"\n{qiymat / 1_000} km")
elif birlik.lower() == "km":
    print(f"{qiymat} km-"
          f"\n{qiymat * 1_000_000} mm"
          f"\n{qiymat * 100_000} sm"
          f"\n{qiymat * 1_000} m")
else:
    print("Noto'g'ri birlik kiritildi. Iltimos, mm, sm, m, yoki km kiriting")

        

#Do'stlar ro'yxatini tuzish
ismlar = []
print("Yaqin do'stlaringiz ro'yxatini tuzamiz:")
n=1
while True:
    savol = f"{n}-do'stingiz ismini kiriting>>"
    ism = input(savol)
    ismlar.append(ism)
    javob = input("Yana ism qo'shasizmi? (ha/yo'q)")
    if javob.lower() =='ha':
        n+=1
        continue
    elif javob.lower() == "yoq" or javob.lower() == "yo'q":
        break
print (ismlar)



#Do'stlarni yoshlari bn lug'at tuzish
print("Do'stlaringiz yoshini saqlaymiz:")
dostlar = {}
while True:
    ism = input("Do'stingiz ismini kiriting: ")
    yosh = input(f"{ism.title()}ning yoshini kiriting: ")
    dostlar[ism] = int(yosh)
    javob = input("Yana ma'lumot qo'shasizmi? (ha/yo'q)")
    if javob.lower() == "yoq" or javob.lower() == "yo'q":
        break
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
n=1
while True:
    savol = f"{n}-do'stingiz ismini kiriting: "
    ism = input(savol)
    ismlar.append(ism)
    javob = input("Yana ism qo'shasizmi? (ha/yo'q)")
    if javob.lower() =='ha':
        n+=1
        continue
    else:
        break
print("Do'stlaringiz:")
for ism in ismlar:
    print (ism.title())



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
        if maxsulotlar.lower() == maxsulot:
            savat[maxsulotlar] = narx
    if add.lower() == "yo'q" or add.lower() == "yoq":
        yoq.append(maxsulotlar)
        for borlar,narxi in savat.items():
            print (f"{borlar}ning narxi {narxi} so'm")
        for yoqlar in yoq:
            print(f"Bizda {yoqlar} yo'q")
        break
    else:
        continue



#Login va parol tekshiruv
malumot = {
    'saidov.mee': 'saidov.b10',
    'mansurvich.10': 'mnsrvch12345',
    'bekhruz.001': 'bekhruz.001',
    'mansurvich.01': 'saidovb1111',
    'my.world.uzb': 'myworlduzb',
    'coding.zone.uz': 'coding.zone.uz2010'
}
login = str(input('Login kiriting>> ')).lower()
found = False

for user, parol in malumot.items():
    if login == user:
        print(f'Login - {user}\nParol - {parol}')
        found = True
        break

if not found:
    if login == "admin":
        admin = input("Admin parolini kiriting >>").lower()
        if admin == "adminid":
            for user, parol in malumot.items():
                print(f'Login - {user}\nParol - {parol}')
        else:
            print("Admin paroli noto'g'ri!")
    else:
        print(f"{login} - Login topilmadi!")

holat = True
savol = str(input('Yana login kiriting>> ')).lower()

for login, parol in malumot.items():
    if savol == login:
        print(f"Login- {login}")
        print(f"Parol- {parol}")
        holat = False
        break

if holat:
    print("Bunday login topilmadi")


#Son topish o'yini
tries = 0
son = "Men o'ylagan 1 dan 10 gacha sonni toping>> "
tugri_son = random.randint(1, 10)
while True:
    savol = int(input(son))
    tries += 1
    if savol == tugri_son:
        print (f"Qoyil, {tries} - urinishda topdingiz!")
        break
    else:
        print("Xato Qaytadan uruning")



#Bank xisob yaratish va o'tkazmalar qilish
class Bank:
    def __init__(self, foydalanuvchi, xisob = 0):
        self.foydalanuvchi = foydalanuvchi
        self.__xisob = xisob
        self.__uuid = uuid4()
    
    def foydalanuvchi_nomi(self):
        print(f"Foydalanuvchi nomi - {self.foydalanuvchi}")

    def balans(self):
        print(f"Xisobingizda {self.__xisob} so'm pul bor")

    def pul_qoshish(self, miqdor):
        self.__xisob += miqdor
        if miqdor >= 20_000_000:
            bonus = miqdor * 0.3 /100
            self.xisob += bonus
            print (f"Xisobingizga {miqdor} so'm qo'shildi va bonus sifatida {bonus} so'm qo'shildi")
        else:
            print (f"Xisobingizga {miqdor} so'm qo'shildi")

    def pul_yechish(self, miqdor):
        if self.__xisob >= miqdor:
            self.__xisob -= miqdor
            print(f"Xisobingizdan {miqdor} so'm yechib olindi")
        else:
            print("Xisobingizda yetarli mablag' yo'q")

    def pul_otgazish(self, miqdor, boshqa_foydalanuvchi):
        if self.__xisob >= miqdor:
            boshqa_foydalanuvchi.__xisob += miqdor
            self.__xisob -= miqdor
            print(f"{boshqa_foydalanuvchi.foydalanuvchi} xisobiga {miqdor} so'm o'tkazildi")
        else:
            print("Mablag' yetarli emas")

behruzbek = Bank("Behruzbek")
shaxruza = Bank("Shaxruza")
shaxruza.pul_qoshish(14000000)
shaxruza.pul_otgazish(4000000, behruzbek)
shaxruza.balans()
behruzbek.balans()



#Avtomobil yaratish va boshqarish
class Avtomabil:
    def __init__(self, marka, model, yil, rang):
        self.marka = marka
        self.model = model
        self.rang = rang
        self.__yil = yil
        self.__holat = False
        self.__uuid = uuid4

    def yoqish(self):
        if self.__holat == False:
            self.__holat = True
            print("Avtomabil yondi")
        else:
            print("Avtomabil allaqachon yoniq edi")

    def ochirish(self):
        if self.__holat == True:
            self.__holat = False
            print("Avtomabil o'chdi")
        else:
            print("Avtomabil allaqachon o'chiq edi")

    def get_info(self):
        if self.__holat == True:
            hozir_holat = "Yoniq"
        else:
            hozir_holat = "O'chiq"
        print(
              f"{self.marka} {self.model} avtomabili {self.rang} rangda, {self.__yil}-yilda ishlab chiqarilgan, {hozir_holat} holatda"
              )
        
avto1 = Avtomabil("Chevrolet", "Gentra", 2024, "Qora")
avto1.yoqish()
avto1.get_info()
avto1.ochirish()
avto1.ochirish()



#To'g'rito'rtburchak bilan amallar
class Togritortburchak:
    def __init__(self, eni, boyi):
        self.eni = eni
        self.boyi = boyi

    def get_eni(self):
        print(self.eni)

    def get_boyi(self):
        print(self.boyi)

    def perimetri(self):
        perimetr = 2 * (self.eni + self.boyi)
        print(f"Perimetri - {perimetr}")

    def yuzasi(self):
        yuzasi = self.eni * self.boyi
        print(f"Yuzasi - {yuzasi}")

    def get_info(self):
        print(f"Eni - {self.eni}, Bo'yi - {self.boyi}")

shakl1 = Togritortburchak(12,36)
shakl1.perimetri()
shakl1.yuzasi()
shakl1.get_info()



#TALABALARNI BAXOLASH
class Talaba:
    talaba_soni = 0
    def __init__(self, ism,  kurs):
        self.ism = ism
        self.__kurs = kurs
        self.__baholar = []
        self.uuid = uuid4
        Talaba.talaba_soni += 1

    def baho_qoyish(self, baho):
        self.__baholar.append(baho)
        print(f"Talaba {self.ism}ga {baho} baho qo'yildi")

    def ortacha_baho(self):
        if not self.__baholar:
            return 0
        ortacha_baho = sum(self.__baholar) / len(self.__baholar)
        return ortacha_baho


class Sinfxona:
    def __init__(self):
        self.talaba_royxati = []

    def talabalar_soni(self):
        soni = len(self.talaba_royxati)
        print(f"Sinfda {soni} ta talaba bor")

    def talaba_qoshish(self, talaba):
        self.talaba_royxati.append(talaba)
        print(f"{talaba.ism} sinfga qo'shildi")

    def top_talaba(self):
        if self.talaba_royxati == []:
            print("Sinfda talaba yo'q")
            return None
        
        top_talaba = self.talaba_royxati[0]
        for talaba in self.talaba_royxati:
            ortacha_baho = talaba.ortacha_baho()
            if ortacha_baho is not None and ortacha_baho > top_talaba.ortacha_baho():
                top_talaba = talaba
        print(f"Eng alochi talaba - {top_talaba.ism}, uning o'rtacha bahosi {top_talaba.ortacha_baho()}")

talaba1 = Talaba("Behruzbek", 3)
talaba1.baho_qoyish(4)
talaba1.baho_qoyish(5)
talaba1.ortacha_baho()

talaba2 = Talaba("Lola", 1)
talaba2.baho_qoyish(2)
talaba2.baho_qoyish(5)
talaba2.baho_qoyish(2)
talaba2.baho_qoyish(4)

sinf_8b = Sinfxona()
sinf_8b.talaba_qoshish(talaba1)
sinf_8b.talaba_qoshish(talaba2)
sinf_8b.top_talaba()



#1 Berilgan butun sonni teskari tartibda chiqaruvchi dastur
def teskari_son(son):
    son = str(son)
    teskari_son = son[::-1]
    print(f"{son} - {teskari_son}")

teskari_son(112)



#3 Foydalanuvchi kiritgan matnni teskari tartibda chiqaruvchi dastur
def teskari_matn(matn):
    teskari_matn = matn[::-1]
    print(f"{matn} - {teskari_matn}")

teskari_matn("Teskari matn")



#4 Foydalanuvchi kiritgan sonning toq yoki juft ekanligini aniqlash
def son_turi(son):
    if son % 2 == 0:
        print(f"{son} - juft son")
    else:
        print(f"{son} - toq son")

son_turi(58)



#5 Berilgan n soni uchun n! (faktorial) ni hisoblash
def faktarial(n):
    if n < 0:
        print("Faktarial faqat musbat sonlar uchun ishlaydi")
    elif n == 0:
        print(f"{n}! = 1")
    else:
        javob = 1
        for son in range(1, n+1):
            javob *= son
        print(f"{n}! = {javob}")

faktarial(6)



#6 Foydalanuvchi kiritgan uchta son orasidan eng kattasini aniqlash
def max(son1, son2, son3):
    sonlar = [son1, son2, son3]
    eng_kattasi = sonlar[0]
    for son in sonlar:
        if son > eng_kattasi:
            eng_kattasi = son
    print(eng_kattasi)

max(25, 35, 66)



#7 Matndagi har bir harfning nechta marta qatnashganini hisoblash
def harflarni_sanash(matn):
    soni = {}
    for harf in matn:
        if harf.isalpha():
            harf = harf.lower()
            soni[harf] = soni.get(harf, 0) + 1
    for harfi, son in soni.items():
        print(f"{harfi} - {son} ta")

harflarni_sanash("Saidov Behruzbek Mansurvich")



#8 Sonni raqamlar yig'indisini topish
def raqmlar_yigindisi(son):
    yigindi = 0
    for raqam in str(son):
        yigindi += int(raqam)
    print(yigindi)

raqmlar_yigindisi(5264)



#9 Matn palindrom ekanligini aniqlash
def palindromni_aniqlash(soz):
    tayyor = soz.lower()
    if tayyor[::-1] == tayyor:
        print("Bu so'z palindrom")
    else:
        print("Bu so'z palindrom emas")

palindromni_aniqlash("alla")



#10 Berilgan sonning tub ekanligini aniqlash
def tub_sonni_aniqlash(son):
    if son <= 1:
        print(f"{son} 1 dan katta bo'lishi kerak")
    else:
        tub = True
        for bolinma in range(2, son):
            if son % bolinma == 0:
                tub = False
                break
            else:
                tub = True
        if tub == True:
            print(f"{son} - tub son")
        else:
            print(f"{son} - murakkab son")

tub_sonni_aniqlash(17)



#15 Ikki matnning bir-biriga anagram ekanligini aniqlash
def anagramni_aniqlash(soz1, soz2):
    soz1 = soz1.lower()
    soz2 = soz2.lower()
    soz1_list = []
    soz2_list = []
    for harf in soz1:
        soz1_list.append(harf)
    for harf in soz2:
        soz2_list.append(harf)
    if sorted(soz1_list) == sorted(soz2_list):
        print("Bu so'zlar anagram")
    else:
        print("Bu so'zlar anagram emas")

anagramni_aniqlash("silent", "listen")


#16 Matnli fayldagi har bir so'zning nechta marta qatnashganini hisoblash
def sozlar_soni(matn):
    sozlar_soni = {}
    sozlar = matn.lower().split()
    for soz in sozlar:
        if soz in sozlar_soni:
            sozlar_soni[soz] += 1
        else:
            sozlar_soni[soz] = 1
    for soz, son in sozlar_soni.items():
        print(f"'{soz}' so'zi {son} marta qatnashgan.")

sozlar_soni("Salom Ali , ali seni familyang alievmi")


#17 Berilgan raqamlar ro'yxatini o'sish tartibida tartiblash
def sort_raqam(* son):
    print(sorted(son))

sort_raqam(25,12,78,65)


#Berilgan butun sonning barcha raqamlari ko'paytmasini hisoblash
def raqamlar_kopaytmasi(son):
    kopaytma = 1
    if son >= 0:
        for raqam in str(son):
            kopaytma *= int(raqam)
        print(f"{son} ni raqamlar ko'paytmasi - {kopaytma}")
    else:
        print(f"{son} musbat bo'lishi kerak")

raqamlar_kopaytmasi(652)



#Foydalanuvchi kiritgan sonlar orasidan eng kichigini aniqlash
def kichik_son(* sonlar):
    list_sonlar = []
    for son in sonlar:
        list_sonlar.append(son)
    print(list_sonlar)
    print(f"Eng kichik son - {min(list_sonlar)}")

kichik_son(2,9,4)



#Berilgan son Armstrong son ekanligini tekshirish
def check_armstrong(son):
    raqamlar = []
    new_raqamlar = []
    arm_yigindi = 0
    for raqam in str(son):
        raqamlar.append(int(raqam))

    for per_raqam in raqamlar:
        n = len(raqamlar)
        daraja = per_raqam **n
        new_raqamlar.append(daraja)

    for kopaytma_raqamlar in new_raqamlar:
        arm_yigindi += kopaytma_raqamlar

    if son == arm_yigindi:
        print(f"{son} Armstrong ekan")
    else:
        print(f"{son} Armstrong emas")

check_armstrong(407)



#Berilgan ikki ro'yxat bir xil elementlarga ega ekanligini tekshirish
def royxat_tengligi(royxat1, royxat2):
    if sorted(str(royxat1)) == sorted(str(royxat2)):
        print("Bu ro'yxatlar bir xil")
    else:
        print("Bu ro'yxatlar bir xil emas")

list1 = [22,15,78,35,5]
list2 = [22,15,5,78,35]
royxat_tengligi(list1 ,list2)



#Foydalanuvchi kiritgan matnda nechta so'z borligini hisoblash
def sozlar_soni(matn):
    sozlar = matn.split()
    print(f"Matnda {len(sozlar)} ta so'z bor")

sozlar_soni("Hi my name is Saidov Behruzbek")



#Berilgan ikki son orasidagi barcha toq sonlarni ro'yxat qilib chiqarish
def toq_sonlar(son1, son2):
    toqlar = []
    if son2 > son1 and son1 > 0:
        for son in range(son1 + 1, son2):
            if son % 2 != 0:
                toqlar.append(son)
    print(toqlar)

toq_sonlar(7,28)



#Foydalanuvchi kiritgan matndagi eng uzun so'zni topish
def uzun_soz(matn):
    sozlar = matn.split()
    uzun_soz = sozlar[0]
    for soz in sozlar:
        if len(soz) > len(uzun_soz):
            uzun_soz = soz
    print(uzun_soz)

uzun_soz("Salom so'zlar orasidagi eng uzun so'zni topish")



#Berilgan sonning barcha o'zaro bo'luvchilarini topish
def boluvchilarini_topish(son):
    boluvchisi = []
    for oldingi_son in range(1, son + 1):
        if son % oldingi_son == 0:
            boluvchisi.append(oldingi_son)
    print(f"{son} ni boluvchilari - {boluvchisi}")

boluvchilarini_topish(30)



#Berilgan ikkita matn bir xil bo'lsa, 'Ha' yoki 'Yo'q' javob qaytarish
def matn_birxil(matn1, matn2):
    if matn1.lower() == matn2.lower():
        print("Ha")
    else:
        print("Yo'q")

matn_birxil("Bu matnlar bir xil", "bu matnlar bir xil")



#Foydalanuvchi kiritgan sonlaring yig'indisini hisoblash
def yigindi(* sonlar):
    yigindi = 0
    for son in sonlar:
        yigindi += son
    print(yigindi)

yigindi(55,24,62)



#Foydalanuvchi kiritgan ro'yxatni teskari tartibda chiqarib berish
def teskari_list(list):
    print(list[::-1])

list1 = [2,77,"ali"]
teskari_list(list1)



#Matnda barcha kichik harflarni katta harflarga, katta harflarni kichik harflarga almashtirsh
def matn_ozgartir(matn):
    print(f"{matn.swapcase()}")

matn_ozgartir("Salom O'zbekiston")



#Kiritilgan matnning uzunligini aniqlash
def matn_uzunligi(matn):
    sozlar_soni = len(matn.split())
    belgilar_soni = len(matn)
    print(f"Matnda {sozlar_soni} ta so'z va {belgilar_soni} ta belgi bor")

matn_uzunligi("Salom Dunyo, O'zbekiston")



#Ro'yxatdagi toq juft sonlarni alohida chiqarish
def son_turi(list):
    toq = []
    juft = []
    try:
        for son in list:
            if son % 2 == 0:
                juft.append(son)
            elif son % 2 >= 0:
                toq.append(son)
            else:
                print("Manfiy son kiritishingiz kerak")
        print(f"Juft sonlar - {sorted(juft)}\nToq sonlar - {sorted(toq)}")
    except TypeError:
        print("Matn kiritish mumkin emas")

sonlar = [9,4,3,77,12]
son_turi(sonlar)



#Foydalanuvchi kiritgan matnni alfavit bo'yicha tartiblash
def matn_tartiblash(matn):
    harflar = sorted(matn.lower())
    matnda = "".join(harflar)
    print(matnda)

matn_tartiblash("Behruzbek")



#Foydalanuvchi kiritgan sonni ikkilik sanoq tizimiga o'tkazish
def sanoq_sistema(son):
    print(bin(son)[2:])

sanoq_sistema(5)



#Kiritilgan 2 ta sonning EKUBini topish
def ekub(son1, son2):
    son1_boluvchilari = []
    son2_boluvchilari = []
    umumiy = []

    for oldingi_son1 in range(1, son1 + 1):
        if son1 % oldingi_son1 == 0:
            son1_boluvchilari.append(oldingi_son1)
    for oldingi_son2 in range(1, son2 + 1):
        if son2 % oldingi_son2 == 0:
            son2_boluvchilari.append(oldingi_son2)

    for har_boluvchi1 in son1_boluvchilari:
        for har_boluvchi2 in son2_boluvchilari:
            if har_boluvchi1 == har_boluvchi2:
                umumiy.append(har_boluvchi1)

    ekub = max(umumiy)
    javob = f"EKUB({son1} , {son2}) = {ekub}"
    if ekub == 1:
        javob += " va bu sonlar o'zaro tub"
        print(javob)
    else:
        print(javob)

ekub(32,16)



#Kiritilgan 2 ta sonning EKUKini topish
def ekuk(son1, son2):
    son1_boluvchilari = []
    son2_boluvchilari = []
    umumiy = []

    if son1 == 0 or son2 == 0:
        print("EKUKni hisoblashda 0 kiritish mumkin emas")
        return

    for oldingi_son1 in range(1, son1 + 1):
        if son1 % oldingi_son1 == 0:
            son1_boluvchilari.append(oldingi_son1)
    for oldingi_son2 in range(1, son2 + 1):
        if son2 % oldingi_son2 == 0:
            son2_boluvchilari.append(oldingi_son2)

    for har_boluvchi1 in son1_boluvchilari:
        for har_boluvchi2 in son2_boluvchilari:
            if har_boluvchi1 == har_boluvchi2:
                umumiy.append(har_boluvchi1)

    ekub = max(umumiy)
    ekuk = (son1 * son2) // ekub
    print(f"EKUK({son1} , {son2}) = {ekuk}")

ekuk(32,16)
