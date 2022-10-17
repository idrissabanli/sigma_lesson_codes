
class Calc:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def sum(self):
        return self.a + self.b

    def divide(self):
        if self.b == 0:
            raise ZeroDivisionError
        return self.a / self.b


# c = Calc(4, 2)
# c.sum() # 6
# c.divide() # 2