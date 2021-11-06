import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import control
import queue
from air_heater_simulator import AirHeaterModel

#Mulig løsning for time delay: https://stackoverflow.com/questions/42632523/solve-ode-in-python-with-a-time-delay

def step_response_ode_solve():

    th_t =22
    th_d = 2
    Kh = 3.5
    Tenv = 21.5
    Ts = 0.5
    T0 = Tenv
    u = 1
    heater = AirHeaterModel(th_t, th_d, Kh, Tenv, Ts)

    t_start = 0
    t_stop = 120
    increment = 1
    t = np.arange(t_start, t_stop, increment)


    def model(T, t, u, Kh, th_t, Tenv):

        dTdt = (1 / th_t) * (-T + (Kh * u) + Tenv)
        return dTdt

    x = odeint(model, T0, t, args=(u, Kh, th_t, Tenv))
    print(x)

    plt.plot(t, x)
    plt.title('1. order system=dTdt = (1 / th_t) * (-T + (Kh * u) + Tenv)')
    plt.xlabel('t[s]')
    plt.ylabel('T(u)[°C]')
    plt.grid()
    plt.show()

def step_response_tf():
    num = np.array([3])
    den = np.array([4, 1])

    H = control.tf(num, den)
    print('H(s) = ', H)
    t, y = control.step_response(H)

    plt.plot(t, y)
    plt.title("Step Response")
    plt.grid()
    plt.show()

if __name__ == '__main__':
    step_response_tf()
    step_response_ode_solve()
