class Car:
    def __init__(self, marka, model, konsulu,vupysk):
        self.marka = marka
        self.model = model
        self.konsulu = konsulu
        self.vupysk = vupysk
    def speak_about(self):
        print(f"Привіт, я {self.marka}. Я модель {self.model}, у мене {self.konsulu} конячих сил і я {self.vupysk} року випуску")

Mersedes = Car("Mercedes",'S', "600","2006")
Mersedes.speak_about()