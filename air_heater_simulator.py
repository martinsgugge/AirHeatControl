import queue

class AirHeaterModel:

    def __init__(self,  th_t,  th_d,  Kh,  Tenv,  Ts):
        self.th_t = th_t
        self.th_d = th_d
        self.Kh = Kh
        self.Tenv = Tenv
        self.Ts = Ts
        self.T = Tenv

        self.initialize_time_array()

    def run(self, u, t):

        self.TimeShift(u)
        self.T = t + (1 / self.th_t) * (-self.T + (self.Kh * self.u) + self.Tenv)*self.Ts
        return self.T


    def time_shift(self, u):

        self.u = self.U.get()
        self.U.add(u)


    def initialize_time_array(self):

        self.length = self.th_d / self.Ts
        U = queue.Queue(self.length)
        for i in range(len(self.length)):
            U.add(0)

        self.U = U


if __name__ == '__main__':
    print('h')