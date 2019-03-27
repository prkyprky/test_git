# class Kocka:
#     def __init__(self, jmeno):
#         self.jmeno = jmeno
#         self.pocet_ziv = 9
#     def zamnoukej(self):
#         # print('Mnau')
#         print('Mnau {}'.format(self.jmeno))
#     def je_ziva(self):
#         if self.pocet_ziv > 0:
#             print('{} je ziva'.format(self.jmeno))
#         else:
#             print('{} je mrtva'.format(self.jmeno))
#
#     def uber_zivot(self):
#         if self.pocet_ziv == 0:
#             print('{} je mrtva'.format(self.jmeno))
#         else:
#             self.pocet_ziv = self.pocet_ziv - 1
#             print('Aktualni pocet zivotu {} je {}'.format(self.jmeno,self.pocet_ziv))
#     def snez(self, jidlo):
#         if (jidlo).lower() == 'ryba':
#             self.pocet_ziv = self.pocet_ziv +1
#             print('{} byla dobra. Pribyl mi jeden zivot. Ted mam {} zivotu'.format(jidlo,self.pocet_ziv))
#         else:
#             print('{} bylo fajn, ale porad mam {} zivotu'.format(jidlo, self.pocet_ziv))
#
#
# Alisa = Kocka('Alisa')
#
# Alisa.je_ziva()
#
#
# Alisa.snez('ryba')
# Alisa.snez('konzerva')
#
# Alisa.uber_zivot()

#######################################################################################################################

class Zviratko:
    def __init__(self, jmeno):
        self.jmeno = jmeno

    def snez(self, jidlo):
        print('{}: {} mi chutna'.format(self.jmeno, jidlo))

class Kotatko(Zviratko):
    def udelej_zvuk(self):
        print('{}: Mnau'.format(self.jmeno))

class Stenatko(Zviratko):
    def udelej_zvuk(self):
        print('{}: Haf.'.format(self.jmeno))

Mercy = Kotatko('Mercy')

Mercy.zamnoukej()
Mercy.snez('konzerva')

Baryk = Stenatko('Baryk')

Baryk.zastekej()
Baryk.snez('rybu')


zviratka = [Kotatko('Mercy'), Stenatko('Baryk')]

for zviratko in zviratka:
    zviratko.udelej_zvuk()
    zviratko.snez('beton')

print(Mercy.udelej_zvuk())