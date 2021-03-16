class A:
    def __init__(self):
        self.a = 1
        self.b = 2
        self.c = 3
    def seta(self):
        def afunction():
            self.a = 4
        afunction()
    def geta(self):
        return self.a

if __name__ == '__main__':
    cA = A()
    print(cA.a)
    cA.seta()
    print(cA.a)
    print(cA.geta())