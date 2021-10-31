class PID:

    def __init__(self, Kp, Ti, Td, Ts, SetPoint, outputLow = 0, outputHigh = 5):

        self.Kp = Kp
        self.Ti = Ti
        self.Td = Td
        self.Ts = Ts
        self.SetPoint = SetPoint
        self.outputLow = outputLow
        self.outputHigh = outputHigh
        self.e = 0
        self.u = 0
        self.automatic = True

    def run(self, T, U):

        if self.automatic:
            e_tmp = self.SetPoint - T
            u = self.u + self.Kp * (e_tmp - self.e) + self.Kp / self.Ti * self.Ts * e_tmp
            self.e = e_tmp
            if u < self.outputLow:

                u = self.outputLow

            elif u > self.outputHigh:

                u = self.outputHigh

            self.u = u
            return self.u
        else:
            return U


if __name__ == '__main__':
    from air_heater_simulator import AirHeaterModel

    heater = AirHeaterModel(22, 2, 3.5, 21.5, 0.5)
    pi = PID(2, 30, 0, 0.5, 25)
    for i in range((60)):
        pi.run(heater.T, heater.u)
        print(heater.run(pi.u, heater.T))
