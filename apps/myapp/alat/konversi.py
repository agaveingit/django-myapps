class Konverter:
    """
    Kode ini berfungsi untuk mengubah angka menjadi teks 
    sesuai dengan input yang diberikan.

    Kalkulasi dilakukan dengan cara mencari bilangan dan posisinya.
    """
    def __init__(self):
        self.satuan: list[str] = ['', 'satu', 'dua', 'tiga', 'empat', 'lima', 'enam', 'tujuh', 'delapan', 'sembilan']
        self.belasan: list[str] = ["sepuluh", "sebelas", "dua belas", "tiga belas", "empat belas", "lima belas", 
                                    "enam belas", "tujuh belas", "delapan belas", "sembilan belas"]
        self.angka_level_tinggi: list[tuple[int, str]] = [
            (1_000_000_000_000, "triliun"),
            (1_000_000_000, "miliar"),
            (1_000_000, "juta"),
            (1_000, "ribu"),
        ]

    def puluhan(self, i: int) -> str:
        puluh: int = int(i / 10)
        sisa: int = i % 10
        if i < 10:
            return f"{self.satuan[i]}"
        elif i < 20:
                return f"{self.belasan[i - 10]}"
        else:
            if (sisa) == 0:
                return f"{self.satuan[puluh]} puluh" 
            else:
                return f"{self.satuan[puluh]} puluh {self.satuan[sisa]}"

    def ratusan(self, i: int) -> str:
        ratus: int = int(i / 100)
        sisa: int = i % 100
        if i < 100:
            return self.puluhan(i)
        elif i < 200:
            return f"seratus {self.puluhan(sisa)}"
        else:
            return f"{self.satuan[ratus]} ratus {self.puluhan(sisa)}"

    def konversi(self, angka: int) -> str:
        if angka < 0:
            return f"minus {self.konversi(-angka)}"
        
        if angka == 0:
            return "nol"
        
        if angka < 1000:
            return self.ratusan(angka)

        # Kode dilakukan dengan mencari nilai yang setara dengan
        # input yang diberikan. Dimulai dari level tertinggi
        # menuju level yang lebih rendah.
        for nilai, nama in self.angka_level_tinggi:
            if angka >= nilai:
                depan = angka // nilai
                sisa = angka % nilai

                if nilai == 1_000 and depan == 1:
                    head = "seribu"
                else:
                    head = f"{self.konversi(depan)} {nama}"

                return head if sisa == 0 else f"{head} {self.konversi(sisa)}"

        # fallback 
        return ""