from uuid import uuid4
def uuide():
    return str(uuid4().hex[:5])
class Bank:
    def __init__(self, foydalanuvchi):
        self.__foydalanuvchi = foydalanuvchi
        self.xisob = 0
        self.__uuid = uuid4()
    
    def get_nomi(self):
        return self.__foydalanuvchi

    def balans(self):
        return self.xisob

    def pul_qoshish(self, miqdor):
        if miqdor < 0:
            return "Kamida 1 so'm o'tkazish mumkin"
        self.xisob += miqdor
        if miqdor >= 20_000_000:
            bonus = miqdor * 0.3 /100
            self.xisob += bonus
            return f"Xisobingizga {miqdor:,} so'm qo'shildi va bonus sifatida {bonus:,} so'm qo'shildi"
        else:
            return f"Xisobingizga {miqdor:,} so'm qo'shildi"

    def pul_yechish(self, miqdor):
        if self.xisob >= miqdor:
            self.xisob -= miqdor
            return f"Xisobingizdan {miqdor:,} so'm yechib olindi"
        else:
            return "Xisobingizda yetarli mablag' yo'q"

    def pul_otgazish(self, miqdor, boshqa_foydalanuvchi):
        if self.__xisob >= miqdor:
            boshqa_foydalanuvchi.xisob += miqdor
            self.__xisob -= miqdor
            return f"{boshqa_foydalanuvchi.__foydalanuvchi} xisobiga {miqdor:,} so'm o'tkazildi"
        else:
            return "Mablag' yetarli emas"



class Dokon:
    def __init__(self, dokon_nomi, manzili, ish_vaqti, telefon, egasi, dkarta):
        self.__nomi = dokon_nomi
        self.__manzili = manzili
        self.__ish_vaqti = ish_vaqti
        self.__telefon = telefon
        self.__egasi = egasi
        self.__dkarta = dkarta
        self.mahsulotlar = []
        self.xaridorlar = []

    def get_dkarta(self):
        return self.__dkarta

    def get_dokon_nomi(self):
        return self.__nomi

    def get_manzil(self):
        return f"{self.__nomi.title()} do'konimiz {self.__manzili}da joylashgan"

    def get_telefon(self):
        return self.__telefon

    def get_ishvaqti(self):
        return self.__ish_vaqti

    def get_egasi(self):
        return f"Do'kon egasi {self.__egasi} va telefon raqami {self.__telefon}"

    def add_mahsulot(self, mahsulot):
        self.mahsulotlar.append(mahsulot)
        return "Yangi maxsulot qo'shildi"

    def remove_mahsulot(self, mahsulot_nomi):
        for har_mahsulot in self.mahsulotlar:
            if har_mahsulot.nomi == mahsulot_nomi:
                self.mahsulotlar.remove(har_mahsulot)
                return f"Do'kondan {har_mahsulot.nomi} olib tashlandi"
            else:
                return "Do'konda bunday mahsulot topilmadi"

    def mahsulotlar_soni(self):
        return f"Do'konda {len(self.mahsulotlar)} ta mahsulot bor"

    def hamma_mahsulotlar(self):
        if not self.mahsulotlar:
            return "Do'konda mahsulot yo'q"
        xabar = ""
        for mahsulot in self.mahsulotlar:
            harf = mahsulot.get_nomi()[-1]
            end = ""
            if harf == "a" or harf == "e" or harf == "i" or harf == "o" or harf == "u" or harf == "o'":
                end += "si"
                xabar += f"{mahsulot.get_kompaniyasi()} {mahsulot.get_nomi()}{end} {mahsulot.get_narxi()} so'mdan va Do'konda {mahsulot.get_miqdori()} ta qolgan\n"
            else:
                xabar += f"{mahsulot.get_kompaniyasi()} {mahsulot.get_nomi()}i {mahsulot.get_narxi()} so'mdan va Do'konda {mahsulot.get_miqdori()} ta qolgan\n"
        return xabar.strip()


    def qidiruv_turkumi(self, turkum):
        xabar = ""
        for mahsulot in self.mahsulotlar:
            if mahsulot.get_turkumi().lower() == turkum.lower():
                xabar += f"{mahsulot.get_kompaniyasi()} {mahsulot.get_nomi()}\n"
        if xabar == "":
            return "Bunday turkumdagi mahsulot topilmadi"
        return xabar.strip()

    def qidiruv_nomi(self, nomi):
        xabar = ""
        for mahsulot in self.mahsulotlar:
            if nomi.lower() == mahsulot.get_nomi().lower():
                xabar += f"{mahsulot.get_kompaniyasi()} {mahsulot.get_nomi()}\n"
        if xabar == "":
            return "Bunday mahsulot topilmadi"
        return xabar.strip()

    def qidiruv_komaniyasi(self, kompaniya):
        xabar = ""
        for mahsulot in self.mahsulotlar:
            if kompaniya.lower() == mahsulot.get_kompaniyasi().lower():
                xabar += f"{mahsulot.get_kompaniyasi()} {mahsulot.get_nomi()}\n"
        if xabar == "":
            return "Bunday mahsulot topilmadi"
        return xabar.strip()

    def kam_qolgan(self):
        kam = []
        for mahsulot in self.mahsulotlar:
            if mahsulot.get_miqdori() <= 3:
                kam.append(mahsulot)
        if kam == []:
            return "Do'konda kam qolgan mahsulotlar yo'q"
        else:
            xabar = ""
            for mahsulot in kam:
                if mahsulot.get_miqdori() == 0:
                    xabar += f"{mahsulot.get_kompaniyasi()} {mahsulot.get_nomi()}dan qolmagan\n"
                else:
                    xabar += f"{mahsulot.get_kompaniyasi()} {mahsulot.get_nomi()}dan {mahsulot.get_miqdori()} ta qolgan\n"
            return xabar.strip()



class Mahsulot:
    def __init__(self, nomi, turkumi, kompaniyasi, narxi, miqdori, tavsifi):
        self.id = uuide()
        self.__nomi = nomi
        self.__turkumi = turkumi
        self.__narxi = narxi
        self.__miqdori = miqdori
        self.__tavsifi = tavsifi
        self.__kompaniyasi = kompaniyasi

    def chegirma(self, foiz):
        yangi_narx = self.__narxi - (self.__narxi * foiz / 100)
        return int(yangi_narx)

    def get_id(self):
        return self.id

    def get_kompaniyasi(self):
        return self.__kompaniyasi

    def get_turkumi(self):
        return self.__turkumi

    def set_nomi(self, yangi_nomi):
        eski_nomi = self.__nomi
        self.__nomi = yangi_nomi
        return f"{eski_nomi} - {self.__nomi} Maxsulot nomi o'zgartirildi"

    def get_nomi (self):
        return self.__nomi

    def set_narxi(self, yangi_narx):
        self.__narxi = yangi_narx
        return f"Mahsulot narxi {self.__narxi} so'mga o'zgartirildi"

    def get_narxi(self):
        return self.__narxi

    def set_miqdori(self, yangi_miqdor):
        self.__miqdori = yangi_miqdor
        return f"Mahsulot miqdori {self.__miqdori} ta ga o'zgartirildi"

    def get_miqdori(self):
        return self.__miqdori

    def batafsil(self):
        return self.__tavsifi

    def get_info(self):
        return f"Do'konda {self.__nomi} {self.__turkumi}idan {self.__miqdori} ta qolgan va narxi {self.__narxi} so'm "


class Xaridor(Dokon, Bank):
    def __init__(self, dokon, ism, familiya, tel_raqam, manzil, xkarta):
        self.__dokon = dokon
        self.__ism = ism
        self.__familiya = familiya
        self.__tel_raqam = tel_raqam
        self.__manzil = manzil
        self.__xkarta = xkarta
        self.__dokon_karta = xkarta
        self.savat = {}
        self.qarz = []


    def __eq__(self, other):
        if isinstance(other, Mahsulot):
            return self.nomi == other.nomi
        return False

    def get_ism(self):
        return self.__ism

    def get_familiya(self):
        return self.__familiya

    def get_manzil(self):
        return self.__manzil

    def get_tel_raqam(self):
        return self.__tel_raqam

    def pul_otkaz(self, summa, otkaz_odam):
        if self.__xkarta.balans() >= summa:
            otkaz_odam.xisob += summa
            self.__xkarta.xisob -= summa
            return
        else:
            return "Xisobingizda yetarli mablag' yo'q."

    def sotib_olish(self, mahsulot, miqdor):
        umumiy_narx = miqdor * mahsulot.get_narxi()
        if mahsulot in self.__dokon.mahsulotlar and mahsulot.get_miqdori() >= miqdor:
            if self.__xkarta.balans() >= umumiy_narx:
                tastiqlash = input(f"Mahsulotni sotib olish uchun hisobingizdan {umumiy_narx:,} so'm pul yechib olinishiga rozimisiz? (ha/yo'q)")
                if tastiqlash.lower() == "ha":
                    self.pul_otkaz(umumiy_narx, xisob2)
                    return f"{mahsulot.get_kompaniyasi()} {mahsulot.get_nomi()} mahsulotidan {miqdor} ta sotib olindi. {umumiy_narx:,} so'm yechildi"
                else:
                    return "Sotib olish bekor qilindi"
            else:
                return "Xisobingizda yetarli mablag' yo'q"
        else:
            return "Do'konda bunday mahsulot yo'q yoki siz so'ragan miqdorda yetarli emas"

    def savatga_qoshish(self, mahsulot, miqdor):
        for per_mahsulot in self.__dokon.mahsulotlar:
            if mahsulot == per_mahsulot:
                if miqdor <= per_mahsulot.get_miqdori():
                    per_mahsulot.set_miqdori(per_mahsulot.get_miqdori() - miqdor)
                    self.savat[mahsulot] = miqdor
                    return "Mahsulot savatga qo'shildi"
                else:
                    return f"Do'konda {per_mahsulot.get_nomi()}dan faqat {per_mahsulot.get_miqdori()} qolgan"
        return f"Do'konda bunday mahsulot yo'q"

    def savatni_korish(self):
        if not self.savat:
            return "Savat bo'sh"
        xabar = "Savatdagi mahsulotlar:\n"
        umumiy_narx = 0
        for maxsulot, miqdor in self.savat.items():
            narxi = maxsulot.get_narxi() * miqdor
            xabar += f"{maxsulot.get_kompaniyasi()} {maxsulot.get_nomi()} - {miqdor} ta ({narxi:,} so'm)\n"
            umumiy_narx += narxi
        xabar += f"Savatdagi mahsulotlarning umumiy narxi - {umumiy_narx:,} so'm"
        return xabar
    
    
xisob1 = Bank("Behruzbek")
xisob2 = Bank("Mansurbek")
stroy_siti = Dokon("Stroy Siti", "Xonqa tuman, Pabeda qishlog'idagi", "8:00 - 20:00", 941104884, "Saidov Mansurbek", xisob2)
xaridor1 = Xaridor(stroy_siti, "Behruzbek", "Saidov", "Navbahor 34", 934688114, xisob1)
mahsulot1 = Mahsulot("Shurpayor", "Insturment", "Welloo", 890_000, 3, "Zo'r ishlaydigan Shurpayor")
mahsulot2 = Mahsulot("Sement", "Xaltali", "StrongCem", 35_000, 200, "Yuqori sifatli sement")
mahsulot3 = Mahsulot("Plyonka", "Bino materiallar", "PlastoWrap", 15_000, 80, "Qattiq plyonka materiallari")
mahsulot4 = Mahsulot("Gips", "Bino materiallar", "PlasterFix", 25_000, 400, "Tez quriydigan gips")

stroy_siti.add_mahsulot(mahsulot1)
stroy_siti.add_mahsulot(mahsulot2)
stroy_siti.add_mahsulot(mahsulot3)
stroy_siti.add_mahsulot(mahsulot4)

print(xisob1.pul_qoshish(60000))
print(xaridor1.sotib_olish(mahsulot2, 1))
print(xisob1.balans())