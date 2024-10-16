login = ['saidov.mee', 'mansurvich.10', 'bekhruz.001','mansurvich.01', 'my.world.uzb', 'coding.zone.uz']
parol = ['saidov.b10', 'mnsrvch12345', 'bekhruz.001001001', 'saidovb1111', 'myworlduzb', 'coding.zone.uz2010']
login_nomi = input("Loginingizni kiriting:")

if login_nomi in login:
    index = login.index(login_nomi)
    print(f'Login-{login[index]}\nParol-{parol[index]}')
else:
    print("Login topilmadi!")