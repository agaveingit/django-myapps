import time

class Loading:
    def __init__(self):
        self.loadings: list[str] = ["Mengambil data dari input ....",
                                "Memproses data ....",
                                "Mengkalkulasikan data",
                                "Memperhitungkan posisi kuantum",
                                "Menampilkan hasil"]
    def load(self) -> str:
        for line in self.loadings:
            print(line)
            time.sleep(0.8)