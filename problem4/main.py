class Ongkir:
    def __init__(self,panjang,lebar,tinggi,berat):
        self.panjang=panjang
        self.lebar=lebar
        self.tinggi=tinggi
        self.berat=berat

    def volume(self):
        return self.panjang*self.lebar*self.tinggi
    
    def ongkos(self):
        if self.volume()< 50:
            print('Harga: Rp 5000')
        else: print(f'Harga: Rp {(int(self.berat)+1) * 5000}')

x=Ongkir(5,2,4,1)
x.ongkos()