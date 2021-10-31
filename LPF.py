


class LPF:
    tf = None
    ts = None
    y = None
    a = None
    def __init__(self, tf, ts, y):
        self.tf = float(tf)
        self.ts = float(ts)
        self.y = float(y)
        self.calc_a()


    def calc_a(self):
        self.a = float(self.ts/(self.tf+self.ts))


    def filter(self, y):
        self.y = (1.0 - self.a) * float(y) + self.a * self.y
        return self.y

