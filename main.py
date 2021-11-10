from air_heater_simulator import AirHeaterModel
from PID import PID
from LPF import LPF
from XML import XML

import numpy as np
import matplotlib.pyplot as plt
from time import sleep


def static_plot_test_air_heat_control_sim():
    # Simulation Parameters
    Ts = 0.1  # Sampling Time
    Tstop = 120  # End of Simulation Time
    N = int(Tstop / Ts)  # Simulation length

    # Init heater
    th_t = 22
    th_d = 2
    Kh = 3.5
    Tenv = 21.5

    heater = AirHeaterModel(th_t, th_d, Kh, Tenv, Ts)

    # Init PI
    Kp = 0.58
    Ti = 18
    Td = 0
    SP = 25
    pi = PID(Kp, Ti, Td, Ts, SP)

    # Init LPF
    tf = 0.5
    ts = 1
    lpf = LPF(tf, ts, Tenv)

    Tout = np.zeros(N + 2)  # Initialization the Tout vector
    Tout[0] = Tenv  # Initial Vaue
    e = np.zeros(N + 2)  # Initialization
    u = np.zeros(N + 2)  # Initialization
    t = np.arange(0, Tstop + 2 * Ts, Ts)

    for i in range(N + 1):
        pi.run(lpf.y, heater.u)
        (heater.run(pi.u, heater.T))
        lpf.filter(heater.T)
        Tout[i] = lpf.y
        e[i] = SP - lpf.y
        u[i] = pi.u

    # Plot Process Value
    plt.figure(1)
    plt.plot(t, Tout)
    # Formatting the appearance of the Plot
    plt.title('Simulation of Air Heater')
    plt.xlabel('t [s]')
    plt.ylabel('Tout [°C]')
    plt.grid()
    xmin = 0
    xmax = Tstop
    ymin = 20
    ymax = 32
    plt.axis([xmin, xmax, ymin, ymax])

    # Plot Control Signal
    plt.figure(2)
    plt.plot(t, u)
    # Formatting the appearance of the Plot
    plt.title('Control Signal')
    plt.xlabel('t [s]')
    plt.ylabel('u [V]')
    plt.grid()
    plt.show()


def dynamic_plot_test_air_heat_control_sim():
    # Simulation Parameters
    Ts = 0.1  # Sampling Time
    Tstop = 120  # End of Simulation Time
    N = int(Tstop / Ts)  # Simulation length

    # Init heater
    th_t = 22
    th_d = 2
    Kh = 3.5
    Tenv = 21.5

    heater = AirHeaterModel(th_t, th_d, Kh, Tenv, Ts)

    # Init PI
    Kp = 0.58
    Ti = 18
    Td = 0
    SP = 30
    pi = PID(Kp, Ti, Td, Ts, SP)

    # Init LPF
    tf = 0.5
    ts = 1
    lpf = LPF(tf, ts, Tenv)

    Tout = np.zeros(N + 2)  # Initialization the Tout vector
    Tout[0] = Tenv  # Initial Vaue
    e = np.zeros(N + 2)  # Initialization
    u = np.zeros(N + 2)  # Initialization
    t = np.arange(0, Tstop + 2 * Ts, Ts)

    # Formatting the appearance of the Plot
    plt.figure(1)
    plt.title('Simulation of Air Heater')
    plt.xlabel('t [s]')
    plt.ylabel('T [°C]')

    plt.figure(2)
    plt.title('Control Signal')
    plt.xlabel('t [s]')
    plt.ylabel('u [V]')

    for i in range(1, N):
        pi.run(lpf.y, heater.u)
        (heater.run(pi.u, heater.T))
        lpf.filter(heater.T)

        e[i] = SP - lpf.y
        u[i] = pi.u
        Tout[i] = lpf.y

        print("Time [s] = %2.1f, u [V] = %3.2f, T [°C] = %2.1f" % (t[i], u[i], lpf.y))
        if i % 10 == 0:  # Update Plot only every second
            # Plot Temperature
            plt.figure(1)
            plt.plot(t[i], Tout[i], '-o', markersize=2, color='blue')
            plt.ylim(20, 32)
            if i*Ts > 20:
                plt.xlim((i*Ts-20), (i*Ts))
            print(i*Ts)
            plt.show(block=False)
            plt.pause(Ts)

            # Plot Control Signal
            plt.figure(2)
            plt.plot(t[i], u[i], '-o', markersize=2, color='red')
            plt.ylim(0, 5)
            if i * Ts > 20:
                plt.xlim((i*Ts-20), (i*Ts))
            plt.show(block=False)
            plt.pause(Ts)
        sleep(Ts/10)
    plt.figure(1)
    plt.plot(t, Tout, '-o', markersize=2, color='blue')
    plt.ylim(20, 32)
    plt.show()
    #plt.xlim(0, (i*Ts))
    plt.figure(2)
    plt.plot(t, u, '-o', markersize=2, color='red')
    plt.ylim(0, 5)
    #plt.xlim(0, (i * Ts))
    plt.show()







if __name__ == '__main__':
    #static_plot_test_air_heat_control_sim()
    dynamic_plot_test_air_heat_control_sim()