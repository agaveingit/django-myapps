import time

class Loading:
    def __init__(self):
        self.loadings: list[str] = ["Mengambil data dari input ....",
                                "Memproses data ....",
                                "Mengkalkulasikan data",
                                "Memperhitungkan posisi kuantum",
                                "Menampilkan hasil"]
    def load(self, massage: str) -> str:
        self.loadings.append(massage)
        lines: list[str] = self.loadings
        return lines
        # for line in lines:
        #     print(line)
        #     time.sleep(0.8)

# y = Loading()
# x = y.load("w")