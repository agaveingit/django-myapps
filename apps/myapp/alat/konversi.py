class Konverter:
    def __init__(self):
        self.satuan: list[str] = ['', 'satu', 'dua', 'tiga', 'empat', 'lima', 'enam', 'tujuh', 'delapan', 'sembilan']
        self.belasan: list[str] = ["sepuluh", "sebelas", "dua belas", "tiga belas", "empat belas", "lima belas", "enam belas", "tujuh belas", "delapan belas", "sembilan belas"]

    def puluhan(self, i: int) -> str:
        puluh: int = int(i / 10)
        sisa: int = i % 10
        if i < 10:
            return f"{self.satuan[i]}"
        elif i < 20:
                return f"{self.belasan[i - 10]}"
        elif i < 100:
            if (sisa) == 0:
                return f"{self.satuan[puluh]} puluh" 
            else:
                return f"{self.satuan[puluh]} puluh {self.satuan[sisa]}"
        else:
            pass

    def ratusan(self, i: int) -> str:
        ratus: int = int(i / 100)
        sisa: int = i % 100
        if i < 200:
            if (sisa) == 0:
                return "seratus"
            else:
                return f"seratus {self.puluhan(sisa)}"
        elif i < 1000:
            if (sisa) == 0:
                return f"{self.satuan[ratus]} ratus"  
            else:
                return f"{self.satuan[ratus]} ratus {self.puluhan(sisa)}"
        else:
            pass

    def konversi(self, angka: int) -> str:
        if angka < 100:
            return self.puluhan(angka)
        elif angka < 1000:
            return self.ratusan(angka)
        else:
            return "Error!: Maksimal input adalah 999"
        

# if __name__ == "__main__":
#     konversi_angka = Konverter()
#     try:
#         nomor: int = int(input("Masukan angka: "))
#         hasil: str = konversi_angka.konversi(nomor) # Konverter.konversi(nomor)
#         print(hasil)
#     except (ValueError, TypeError):
#         print("Error!: Harus masukan angka 0 - 999")