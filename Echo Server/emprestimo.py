import math
class Emprestimo:
    def __init__(self,VP,n):
        self.VP = VP
        self.n = n
        self.i = 0.05

    def valor_final(self):
        self.VF = self.VP * math.pow(1+self.i,self.n)
        return self.VF

    def valor_parc(self):
        self.parc = self.VF/self.n
        return self.parc

    def juros_efetivo(self):
        self.JE = (self.VF/self.VP-1)*100
        return self.JE

