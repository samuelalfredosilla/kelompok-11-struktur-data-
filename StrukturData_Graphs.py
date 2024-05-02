class Peta:
    def __init__(self):
        self.ListKota = {}
    
    def printPeta(self):
        for kota in self.ListKota:
            print(kota, ":",self.ListKota[kota])
        
    def tambahkanKota(self,kota):
        if kota not in self.ListKota:
            self.ListKota[kota] = []
            return True
        return False
    
    def hapusKota(self,kotaDihapus):
        #cek apakah kota yang ingin dihapus ada di list
        if kotaDihapus in self.ListKota:
        #iterasi setiap kotalain untuk hapus kotadihapus
            for kotalain in self.ListKota:
                #cek apakah kota yang ingin dihapus ada jalannya ke kotalain
                if kotaDihapus in self.ListKota[kotalain]:
                    self.ListKota[kotalain].remove(kotaDihapus)
            del self.ListKota[kotaDihapus]
            return True
        return False
    
    def tambahkanJalan(self,kota1,kota2):
        if kota1 in self.ListKota and kota2 in self.ListKota:
            #masukkan kota 1 di list kota2
            self.ListKota[kota2].append(kota1)
            #masukkan kota 2 di list kota1
            self.ListKota[kota1].append(kota2)
            return True
        return False
    
    def hapusJalan(self,kota1,kota2):
        if kota1 in self.ListKota and kota2 in self.ListKota:
            #hapus kota 1 di list kota2
            self.ListKota[kota2].remove(kota1)
            #hapus kota 2 di list kota1
            self.ListKota[kota1].remove(kota2)
            return True
        return False
        

petaJateng = Peta()
petaJateng.tambahkanKota("Surakarta")
petaJateng.tambahkanKota("Klaten")
petaJateng.tambahkanKota("Semarang")
petaJateng.tambahkanKota("Boyolali")
petaJateng.tambahkanKota("Magelang")
petaJateng.tambahkanKota("Temanggung")
petaJateng.tambahkanKota("Wonosobo")
petaJateng.tambahkanKota("Sukoharjo")
petaJateng.tambahkanKota("Karanganyar")
petaJateng.tambahkanKota("Purwodadi")
petaJateng.tambahkanKota("Wonogiri")
petaJateng.tambahkanKota("Sukoredjo")
petaJateng.tambahkanKota("Kebumen")
petaJateng.tambahkanKota("Purworejo")
petaJateng.tambahkanKota("Salatiga")
petaJateng.tambahkanJalan("Surakarta","Klaten")
petaJateng.tambahkanJalan("Klaten","Semarang")
petaJateng.tambahkanJalan("Semarang","Boyolali")
petaJateng.tambahkanJalan("Boyolali","Magelang")
petaJateng.tambahkanJalan("Magelang","Temanggung")
petaJateng.tambahkanJalan("Temanggung","Wonosobo")
petaJateng.tambahkanJalan("Wonosobo","Sukoharjo")
petaJateng.tambahkanJalan("Sukoharjo","Karanganyar")
petaJateng.tambahkanJalan("Karanganyar","Purwodadi")
petaJateng.tambahkanJalan("Purwodadi","Wonogiri")
petaJateng.tambahkanJalan("Wonogiri","Sukoredjo")
petaJateng.tambahkanJalan("Sukoredjo","Kebumen")
petaJateng.tambahkanJalan("Kebumen","Purworejo")
petaJateng.tambahkanJalan("Purworejo","Salatiga")
petaJateng.tambahkanJalan("Salatiga","Surakarta")
petaJateng.tambahkanJalan("Klaten","Boyolali")
petaJateng.tambahkanJalan("Semarang","Magelang")
petaJateng.tambahkanJalan("Boyolali","Temanggung")
petaJateng.tambahkanJalan("Magelang","Wonosobo")
petaJateng.tambahkanJalan("Temanggung","Sukoharjo")
petaJateng.tambahkanJalan("Wonosobo","Karanganyar")
petaJateng.tambahkanJalan("Sukoharjo","Purwodadi")
petaJateng.tambahkanJalan("Karanganyar","Wonogiri")
petaJateng.tambahkanJalan("Purwodadi","Sukoredjo")
petaJateng.tambahkanJalan("Wonogiri","Kebumen")
petaJateng.tambahkanJalan("Sukoredjo","Purworejo")
petaJateng.tambahkanJalan("Kebumen","Salatiga")
petaJateng.tambahkanJalan("Purworejo","Surakarta")
petaJateng.tambahkanJalan("Salatiga","Boyolali")
petaJateng.tambahkanJalan("Klaten","Magelang")
petaJateng.tambahkanJalan("Boyolali","Surakarta")


petaJateng.printPeta()
print('------------------------------')
petaJateng.printPeta()
