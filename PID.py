class PID:

    def __init__(self, Kp, Ti, Td, Ts, SetPoint, outputLow = 0, outputHigh = 5):

        self.Kp = Kp
        self.Ti = Ti
        self.Td = Td
        self.Ts = Ts
        self.SetPoint = SetPoint
        self.outputLow = outputLow
        self.outputHigh = outputHigh
        self.e = None
        self.u = None
        self.automatic = True

    def Run(self, T, U):

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


