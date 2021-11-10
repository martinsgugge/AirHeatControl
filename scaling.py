
class Scaler:
    def __init__(self, lowIn, highIn, lowOut, highOut):
        self.LowIn = lowIn
        self.HighIn = highIn
        self.LowOut = lowOut
        self.HighOut = highOut


    def convert(self, signalIn):
        self.y = (signalIn - self.LowIn) * ((self.HighOut - self.LowOut) / (self.HighIn - self.LowIn)) + self.LowOut
        return self.y

if __name__ == '__main__':
    s = Scaler(1, 5, 0, 50)
    print(s.convert(1))
    print(s.convert(3))
    print(s.convert(5))