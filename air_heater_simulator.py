import queue

class AirHeaterModel:

    def __init__(self,  th_t,  th_d,  Kh,  Tenv,  Ts):
        self.th_t = th_t
        self.th_d = th_d
        self.Kh = Kh
        self.Tenv = Tenv
        self.Ts = Ts
        self.T = Tenv
        self.length = None
        self.U = None
        self.u = None
        self.dTdt = 0

        self.initialize_time_array()

    def run(self, u, t):

        self.time_shift(u)
        self.T = t + (1 / self.th_t) * (-self.T + (self.Kh * self.u) + self.Tenv)*self.Ts
        return self.T

    def model(self, u):
        self.time_shift(u)
        self.dTdt = (1 / self.th_t) * (-self.T + (self.Kh * self.u) + self.Tenv)
        return self.dTdt

    def time_shift(self, u):

        self.u = self.U.get()
        self.U.put(u)


    def initialize_time_array(self):

        self.length = int(self.th_d / self.Ts)
        U = queue.Queue(self.length)
        for i in range(self.length):
            U.put(0)

        self.U = U


if __name__ == '__main__':

    heater = AirHeaterModel(22, 2, 3.5, 21.5, 0.5)
    for i in range((20)):

        print(heater.run(heater.U.get(), heater.T))
        (heater.U.put(5))
