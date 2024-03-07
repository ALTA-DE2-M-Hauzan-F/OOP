# tulis solusi code disini
class Kubus:
    def __init__(self,width):
        self.width=width

    def volume(self):
        print(f'Kubus: {self.width**3}')

class Balok:
    def __init__(self,width,height,depth):
        self.width=width
        self.height=height
        self.depth=depth

    def volume(self):
        print(f'Balok: {self.width*self.height*self.depth}')

class Tabung:
    def __init__(self,radius,height):
        self.radius=radius
        self.height=height

    def volume(self):
        import math
        print(f'Tabung: {math.pi*(self.radius**2)*self.height}')

# Instantiation
k= Kubus(10)
b= Balok(3,6,10)
t=Tabung(7,10)

print('Volume')
k.volume()
b.volume()
t.volume()