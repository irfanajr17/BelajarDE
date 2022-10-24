from codecs import namereplace_errors
from os import uname_result


class Hewan:
    NewNamaLatin= "Prionailurus planiceps" #class attribut

    def __init__(self, nama, umur): #class intance
       self.nama = nama
       self.umur = umur

    def change_nama_latin(self, NewNamaLatin):
        self.NewNamaLatin=NewNamaLatin

class kucing (Hewan):
    def bangun(self, nama, umur):
        self.nama=nama
        self.umur=umur
    
    def change_nama_latin(self, NewNamaLatin):
        self.NewNamaLatin=NewNamaLatin
    
 
    def lari (self,kecepatan):
        self.kecepatan=kecepatan
        if kecepatan > 10:
            print("cepat sekali")
        else :
            print("Lambat") 
K = kucing('Lesi', 4)
K.change_nama_latin('Felis catus')   
K.lari(20)

print(K.nama)
print(K.umur)
print(K.change_nama_latin)
print(K.lari)

