import pickle
#IF ELSE
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

        

#WHILE TSIKLI
#1 Yoqtirgan kitoblaringizni so'rsh stop desa to'xtash
while True:
    kitob = input("Yoqtirgan kitobbingizni kiriting>> ")
    if kitob == "stop":
        break

        
#2 Yoshdn chipta narxini aniqlash
savol = "Yoshingizni kiriting>> "
while True:
    yosh = input(savol)
    if yosh == 'exit' or yosh == 'quit':
        break
    yoshi = int(yosh)
    if yoshi<7:
        narh = 2_000
    elif 7<=yoshi<18:
        narh = 3_000
    elif 18<=yoshi<65:
        narh = 10_000
    else: narh = 0

    if narh==0:
        print("Sizga chipta bepul")
    else:
        print(f"Chipta {narh} so'm")

        
#3 Xatoni topish
savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol)
    if qiymat=='exit':
        break
    elif float(qiymat)<0:
        continue
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")


    
#WHILE, RO'YXATLAR VA LUG'ATLAR
#1 Foydalanuvchidan maxsulotlar ro'yxtini olish
maxsulotlar = []
while True:
    kiritish = input("Mahsulot kiriting>> ")
    maxsulotlar.append(kiritish)
    if kiritish == "stop":
        break
print (maxsulotlar)


#2 Maxsulotni va narxni belgilash
maxsulotlar = {}
while True:
    maxsulot = input("Maxsulotni kiriting>> ").capitalize()
    narx = input(f"{maxsulot.title()}ni narxini kiriting>> ")
    maxsulotlar[maxsulot] = narx
    davom_etish = input("Yana mahsulot qo'shasizmi (ha/yo'q?)>> ")
    if davom_etish == "ha":
        continue
    else:
        break
for maxsulot, narxi in maxsulotlar.items():
    print(f"{maxsulot}ning narxi {narxi} so'm")




#FUNKSIYA
#1
def yil_topish(ism,yosh):
    "Foydalanuvchi ismi va yoshini so'rab, uning tug'ilgan yilini hisoblaydigan funksiya"
    print(f"\nHurmatli {ism}, siz {2024 - yosh} - yilda tug'ilgansiz\n")
yil_topish("Behruzbek" , 14)


#2
def kub_kvadrat(son):
    "Foydalanuvchidan son olib, uning kvadrati va kubini konsolga chiqaruvchi funksiya "
    kvadrat = son ** 2
    kub = son ** 3
    print(f"Son - {son}\nKvadrati - {kvadrat}\nKubi - {kub}\n")
kub_kvadrat(45)


#3
def son_turini_aniqlash(son):
    "Foydalanuvchidan son olib, son juft yoki toqligini konsolga chiqaruvchi funksiya"
    if son % 2 == 0:
        print(f"{son} juft son\n")
    else:
        print(f"{son} toq son\n")
son_turini_aniqlash(24)


#4
def son_kattasi(son1,son2):
    "Foydalanuvchidan ikkita son olib, ulardan kattasini konsolga chiqaruvchi funksiya"
    if son1 > son2:
        print("Katta son -",  son1)
    elif son1 < son2:
        print("Katta son-" , son2)
son_kattasi(23 , 45)


#5
def son_darajasi(x,y):
    "Foydalanuvchidan x va y sonlarini olib,x ni y-darajasini topuvch funksiya"
    daraja = x ** y
    print(f"{x} ni {y} darajasi - {daraja}")
son_darajasi(2 , 45)


#6
def son_darajasi(x,y = 2):
    "Foydalanuvchidan x va y sonlarini olib,x ni 2-darajasini topuvch funksiya"
    daraja = x ** y
    print(f"{x} ni {y} darajasi - {daraja}")
son_darajasi(34)


#7
def bolinish_alomatlari(son):
    "Foydalanuvchidan son qabul qilib, sonni 2 dan 10 gacha bo'lgan sonlarga qoldiqsiz bo'linishini tekshiruvchi funksiya"
    for n in range(2,11):
        if not son%n:
            print(f"{son} {n} ga qoldiqsiz bo'linadi")
bolinish_alomatlari(22)




#QIYMAT QAYTARUVCHI FUNKSIYA
#1
def malumot(ism, familya, t_yil, email = None, t_joy = None):
    """Uchta son qabul qilib, ulardan eng kattasini qaytaruvchi funksiya"""
    yosh = 2024 - t_yil
    malumotlar = {
        "ism" : ism,
        "familya" : familya,
        "t_yil" : t_yil,
        "email" : email,
        "t_joy" : t_joy,
        "yosh" : yosh
    }
    return malumotlar
foydalanuvchi =  malumot("Behruzbek","Saidov", 2010, "saidovbehruzbek2@gmail.com")
print (foydalanuvchi)


#2
mijozlar = []
while True:
    print("Mijoz haqidagi ma'lumotlarni kiriting:")
    ism = input("Ismi: ")
    yosh = input("Yoshi: ")
    manzil = input("Manzili: ")
    mijoz = {
        "ism": ism,
        "yosh": yosh,
        "manzil": manzil
    }
    mijozlar.append(mijoz)
    davom_etish = input("Yana mijoz qo'shasizmi? (ha/yo'q): ").lower()
    if davom_etish != 'ha':
        break
print("\nMijozlar ro'yxati:")
for mijoz in mijozlar:
    print(f"Ismi: {mijoz['ism']}, Yoshi: {mijoz['yosh']}, Manzili: {mijoz['manzil']}")


#3
def son(son1, son2, son3):
    """Uchta son qabul qilib, ulardan eng kattasini qaytaruvchi funksiya"""
    print(max(son1, son2, son3))
son(2,5,6)


#4
def aylana_radiusi(radius):
    """Foydalanuvchidan aylaning radiusini qabul qilib olib, uning radiusini, diametrini, perimetri va yuzini lug'at ko'rinishida qaytaruvchi funksiya"""
    radiusi = radius
    diametri = radiusi * 2
    primetri = 2 * 3.14 * radiusi
    print (f"Aylananing radiusi - {radiusi}, diametri - {diametri}, primetri - {primetri}")
aylana_radiusi(87)


#5
def tub_sonlar():
    tub_sonlar_list = []
    num = 2
    while len(tub_sonlar_list) < 200:
        is_tub = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_tub = False
                break
        if is_tub:
            tub_sonlar_list.append(num)
        num += 1
    return tub_sonlar_list
print (tub_sonlar())




#FUNKSIYA VA RO'YXAT
#1
def katta_harf(matnlar):
    """Matnlardan iborat ro'yxat qabul qilib, ro'yxatdagi har bir matnning birinchi harfini katta harfga o'zgatiruvchi funksiya"""
    for i in range(len(matnlar)):
        matnlar[i]=matnlar[i].title()
ism = ["behruzbek", "shamshod", "sherzod"]
katta_harf(ism)
print(ism)




#MOSLASHUCHAN FUNKSIYA
#1
def kopaytma(*sonlar):
    """Kiritilgan sonlarni ko'paytmasini chiqaruvchi funksiya"""
    javob = 1
    for son in sonlar:
        javob *= son
    return javob
print (kopaytma(4,6,2))


#2
def talaba_malumot(ism, familya, kurs = None, tel = None,t_yil = None):
    "Talaba xaqida malumot beruvchi funksiya"
    malumotlar = {
        "ismi" : ism,
        "familyasi" : familya,
        "kurs" : kurs,
        "tel" : tel,
        "t_yil" : t_yil
    }
    print (f"{familya} {ism}, {t_yil}- yilda tug'ilgan, {kurs} kurs talabasi, Telefon raqami - +998-{tel}")

talaba_malumot("Saidov", "Behruzbek", 3, 934688114, 2005)




#KLASSLAR
#1
class User:
    def __init__(self, ism, user,parol , email, tel):
        self.ism = ism
        self.user = user
        self.parol = parol
        self.email = email
        self.tel = tel
    
#2    
    def get_info(self):
        print (f"Ismi - {self.ism} \nUser - {self.user} \nParol - {self.parol} \nEmail - {self.email} \nTelefon raqam - {self.tel}")

    def change_password(self, eski_parol, yangi_parol):
        if self.parol == eski_parol:
            self.parol = yangi_parol
            print("Parolingiz muvaffaqiyatli o‘zgartirildi")
        else:
            print("Eski parol noto'g'ri")


#3
user1 = User("Behruzbek", "mansurvich.10", "sbm2010", "saidovbehruzbek2@gmail.com", 934688114)
user1.get_info()
user1.change_password("sbm2010", "bek1234")
user1.get_info()




# OBYKETLAR BILAN ISHLASH
# 1
class Avto:
    def __init__(self, model, rang, karobka, narx,kampaniya = "GM", yil = 2024, km = 0):
        self.model = model
        self.rang = rang
        self.karobka = karobka
        self.kampaniya = kampaniya
        self.narx = narx
        self.yil = yil
        self.km = km

#2
    def get_model(self):
        print(f"Avtomabil modeli - {self.model}")

    def get_rang(self):
        print(f"Avtomabil rangi - {self.rang}")

    def get_karobka(self):
        print(f"Avtomabil karobkasi - {self.karobka}")

    def get_narx(self):
        print(f"Avtomabil narxi - {self.narx}")

    def get_kampaniya(self):
        print(f"Avtomabil kampaniyasi - {self.kampaniya}")

    def get_yil(self):
        print(f"Avtomabil ishlab chiqarilgan yili - {self.yil}")

    def get_km(self):
        print(f"Avtomabil {self.km} km yurgan")

#3
    def update_km(self, yangi_km):
        if yangi_km > 0:
            self.km += yangi_km
            print(f"Kilometraj {yangi_km} km ga oshirildi. Jami {self.km} km yurgan")

    def get_info(self):
        print (f"Model: {self.model} \nRang: {self.rang} \nKarobka: {self.karobka}\n"
                f"Kampaniya: {self.kampaniya}\nNarx: {self.narx} so'm\nYil: {self.yil}\nHaydalgan kilometraji: {self.km}")
    

#4
class Avtosalon:
    def __init__ (self, salon_nomi, manzil, sotuvdagi_avtolar):
        self.salon_nomi = salon_nomi
        self.manzil = manzil
        self.sotuvdagi_avtolar = sotuvdagi_avtolar

#5
    def add_avto(self, model, rang, karobka, narx,kampaniya = "GM"):
        self.model = model
        self.rang = rang
        self.karobka = karobka
        self.kampaniya = kampaniya
        self.narx = narx

#6
    def avto_info(self):
        print(self.sotuvdagi_avtolar)

#7
avto1 = Avto("Matiz", "Oq", "Mexanika", 8_000)
avto1.update_km(1400)
avto1.get_info()

avtosale1 = Avtosalon("Bek motors", "Pabeda", "Matiz")
avtosale1.add_avto("Matiz", "Oq", "Mexanika", 8_000)




#VORISLIK VA POLIMORFIZM
#1, 2, 3, 4
class Talaba:
    def __init__(self, ism, familiya, kurs):
        self.ism = ism
        self.familiya = familiya
        self.kurs = kurs
        self.fanlar = []

    def fanga_yozil(self, fan_nomi):
        self.fanlar.append(fan_nomi)

    def remove_fan(self, del_fan):
        for fan in self.fanlar:
            if del_fan in self.fanlar:
                self.fanlar.remove(del_fan)
                print(f"{del_fan.sinf} - sinf {del_fan.nomi} faniga yozilganingiz bekor qilindi")
            else:
                print("Siz bu fanga yozilmagansiz")

    def get_yozilgan_fanlar(self):
        for fan in self.fanlar:
            print(f"{fan.sinf} - sinf {fan.nomi}")


class Fan:
    def __init__(self, nomi, sinf):
        self.nomi = nomi
        self.sinf = sinf

fan1 = Fan("Ona tili", 8)
fan2 = Fan("Algebra", 5)
talaba1 = Talaba("Behruzbek", "Saidov", 2)
talaba1.fanga_yozil(fan1)
talaba2 = Talaba("Aziz", "Valiev", 4)
talaba2.fanga_yozil(fan2)
talaba1.remove_fan(fan1)
talaba2.get_yozilgan_fanlar()
talaba1.get_yozilgan_fanlar()


#5
class Shaxs:
    """Shaxslar haqida ma'lumot"""
    def __init__(self,ism,familiya,passport,tyil):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
    
    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
        return info
        
    def get_age(self,yil):
        """Shaxsning yoshini qaytaruvchi metod"""
        return yil - self.tyil
    
class Prafessor(Shaxs):
    def __init__(self, ism, familiya, passport, tyil, yonalish, tajriba):
        super().__init__(ism, familiya, passport, tyil)
        self.yonalish = yonalish
        self.tajriba = tajriba

    def ish_boshlagan_yil(self, yosh):
        yili = self.tyil + (yosh - self.tajriba)
        print(yili)

    def get_info_pro(self):
        print(f"Professor {self.familiya } {self.ism} {self.tajriba} yillik tajribaga ega")

class Foydalanuvchi(Shaxs):
    def __init__(self, ism, familiya, passport, tyil, username, parol):
        super().__init__(ism, familiya, passport, tyil)
        self.username = username
        self.parol = parol

    def change_password(self, eski_parol, yangi_parol):
        if eski_parol == self.parol:
            self.parol = yangi_parol
            print ("Parol muaffaqiyatli o'zgartirildi")
        else:
            print("Eski parol noto'g'ri")

    def tizimga_kirish(self, user, parol):
        if user == self.username and parol == self.parol:
            print("Tizimga kirdingiz")
        else:
            print("Username yoki parol xato")

    def get_info_user(self):
        print(f"Foydalanuvchi {self.username} - {self.familiya} {self.ism} {self.tyil} - yilda tug'ilgan")
        
class Admin(Foydalanuvchi):
    def __init__(self, ism, familiya, passport, tyil, username, parol):
        super().__init__(ism, familiya, passport, tyil, username, parol)

    def ban_user(self, foydalanuvchi):
        print(f"{foydalanuvchi} foydalanuvchisi bloklandi")

foydalanuvchi1 = Foydalanuvchi("Behruzbek", "Saidov", "EHE7782", 2010, "mansurvich.10", "bek123")
foydalanuvchi1.change_password("bek123", "sbm001")
foydalanuvchi1.get_info()
foydalanuvchi1.get_age(2024)




#31 INKAPSULYATSIA, KLASSNING XUSUSIYAT VA METODLARI
#1
from uuid import uuid4
class Shaxs:
    __odam_soni = 0
    def __init__(self, ism, familiya, tyil):
        self.ism = ism
        self,familiya = familiya
        self.__tyil = tyil
        self.__uuid = uuid4()
        Shaxs.__odam_soni += 1

    @classmethod
    def get_odam_soni(cls):
        print(Shaxs.__odam_soni)

    def get_age(self, hozirgi_yil):
        age = hozirgi_yil - self.__tyil
        print(age)

    def get_info(self):
        print (f"{self.familiya} {self.ism}, {self.__tyil} - yilda tug'ilgan")

class Talaba(Shaxs):
    __talaba_soni = 0
    def __init__(self, ism, familiya, tyil, kurs):
        super().__init__(ism, familiya, tyil)
        self.__kurs = kurs
        Talaba.__odam_soni += 1

    @classmethod
    def get_talaba_soni(cls):
        print (Talaba.__talaba_soni)
    
    def get_info(self):
        print(f"{self.__kurs} - kurs talabasi {self.familiya} {self.ism}, {self.__tyil} - yilda tug'ilgan ")




#33 FAYLLAR BILAN ISHLASH
#2
def topish(yil):
    with open("pi_million_digits.txt") as pi:
        text = pi.read()
    if yil in text:
        print("Ha")
    else:
        print("Yo'q")
topish("0108")