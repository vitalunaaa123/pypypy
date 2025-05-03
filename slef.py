import math
class Calculator:
    def __init__(self,dodavana,vidnimana ):
        self.dodavana = dodavana
        self.vidnamana = vidnimana
    def dodavana(self):
        suma=self.dodavana + self.vidnimana
        print(suma)
    def vidnimana(self):
        minus = self.dodavana - self.vidnimana
        print(minus)
    def mnoz(self):
        mn = self.dodavana * self.vidnimana
        print(mn)
    def dil(self):
        dilena = self.dodavana / self.vidnimana
        print(dilena)
    def Dis(self, a, b, c):
        D = b*b - 4*a*c
        if D>0:
            x1=((b*-1)+math.sqrt(D)) / 2*a
            x2=((b*-1)-math.sqrt(D)) /2*a
            print(x1)
            print(x2)
        if D == 0:
            x=(b/2*a)
            print(x)
        if D !=0:
            print("Коренів немає")









