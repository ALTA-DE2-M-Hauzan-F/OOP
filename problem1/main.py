# tulis solusi code disini
class Persegi:
    def __init__(self,width):
        self.width=width

    def keliling(self):
        print(f'Keliling Persegi: {self.width*4}')
    
    def luas(self):
        print(f'Luas Persegi: {self.width*self.width}')
    

class PersegiPanjang:
    def __init__(self,width,height):
        self.width=width
        self.height=height

    def kll(self):
        print(f'Keliling Persegi Panjang: {2*(self.width+self.height)}')
    
    def ls(self):
        print(f'Luas Persegi Panjang: {self.width*self.height}')

class Segitiga:
    def __init__(self,width,height):
        self.width=width
        self.height=height

    def k(self):
        print(f'Keliling Segitiga: {2*(((self.width/2)**2+self.height**2)**0.5) + self.width}')
    
    def l(self):
        print(f'Luas Segitiga: {self.width*self.height/2}')


# Instantiation
d= Persegi(4)
p= PersegiPanjang(7,8)
s=Segitiga(3,4)

# print Luas
d.luas()
p.ls()
s.l()

# print keliling
print('Keliling')
d.keliling()
p.kll()
s.k()

