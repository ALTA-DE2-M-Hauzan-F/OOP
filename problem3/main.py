class Kalkulator:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def tambah(self):
        print(f'Penjumlahan: {self.a+self.b}')

    def kurang(self):
        print(f'Pengurangan: {self.a-self.b}')

    def kali(self):
        print(f'Perkalian: {self.a*self.b}')

    def bagi(self):
        if self.b ==0: print(f'Pembagian: None')
        else: print(f'Pembagian: {self.a/self.b}')

cal=Kalkulator(12,3)
cal.tambah()
cal.kurang()
cal.kali()
cal.bagi()
