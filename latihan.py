class Segitiga:
    def __init__(self):
        self.t = ""
        self.a = ""
        self.s = ""

    def luas(self):
        hasil = (int(self.a) * int(self.t)) / 2
        print(hasil)

    def keliling(self):
        hasil = int(self.a) + int(self.s) + int(self.t)
        print(hasil)


sg = Segitiga()

sg.a = input("alas: ")
sg.t = input("tinggi: ")
sg.s = input("sisi: ")

sg.luas()
sg.keliling()