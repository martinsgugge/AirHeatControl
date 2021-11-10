import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt
import control

def fr_heater():
    Kh = 3.5
    th_t = 22
    s = control.TransferFunction.s
    H = (Kh)/(th_t*s+1)

    num = np.array([Kh])
    den = np.array([th_t , 1])
    H = signal.TransferFunction(num, den)

    print ('H(s) =', H)
    # Frequencies
    w_start = 0.01
    w_stop = 10
    step = 0.01
    N = int ((w_stop-w_start )/step) + 1
    w = np.linspace (w_start , w_stop , N)
    # Bode Plot
    w, mag, phase = signal.bode(H, w)
    plt.figure()
    plt.subplot (2, 1, 1)
    plt.semilogx(w, mag) # Bode Magnitude Plot
    plt.title("Bode Plot")
    plt.grid(b=None, which='major', axis='both')
    plt.grid(b=None, which='minor', axis='both')
    plt.ylabel("Magnitude (dB)")
    plt.subplot (2, 1, 2)
    plt.semilogx(w, phase) # Bode Phase plot
    plt.grid(b=None, which='major', axis='both')
    plt.grid(b=None, which='minor', axis='both')
    plt.ylabel("Phase (deg)")
    plt.xlabel("Frequency (rad/sec)")
    plt.show()

def fr_lpf():
    wb = 10 #rad/s
    Tf = 1/wb
    num = np.array([1])
    den = np.array([Tf, 1])
    H = signal.TransferFunction(num, den)
    w_start = 0.01
    w_stop = 100
    step = 0.01
    N = int((w_stop - w_start) / step) + 1
    w = np.linspace(w_start, w_stop, N)
    # Bode Plot
    w, mag, phase = signal.bode(H, w)
    plt.figure()
    plt.subplot(2, 1, 1)
    plt.semilogx(w, mag)  # Bode Magnitude Plot
    plt.title("Bode Plot")
    plt.grid(b=None, which='major', axis='both')
    plt.grid(b=None, which='minor', axis='both')
    plt.ylabel("Magnitude (dB)")
    plt.subplot(2, 1, 2)
    plt.semilogx(w, phase)  # Bode Phase plot
    plt.grid(b=None, which='major', axis='both')
    plt.grid(b=None, which='minor', axis='both')
    plt.ylabel("Phase (deg)")
    plt.xlabel("Frequency (rad/sec)")
    plt.show()

def create_sys_tf():

    s = control.TransferFunction.s

    Kh = 3.5
    th_t = 22
    th_d = 2
    N = 5

    [num_pade, den_pade] = control.pade(th_d, N)
    Hpade = control.tf(num_pade, den_pade)
    H_h = Kh / (th_t * s + 1)

    H_h = control.series(H_h, Hpade)

    Kp = 0.52
    Ti = 18
    H_PI = Kp*(Ti*s+1)/Ti*s

    Tf = 0.5
    H_lpf = 1/(Tf*s+1)
    L = control.series(H_h, H_PI, H_lpf)
    print(L)
    return L

def analyze_tf():
    s = control.TransferFunction.s

    Kh = 3.5
    th_t = 22
    th_d = 2
    N = 5

    [num_pade, den_pade] = control.pade(th_d, N)
    Hpade = control.tf(num_pade, den_pade)
    H_h = Kh / (th_t * s + 1)
    print('H_h(s) =', H_h)
    H_h = control.series(H_h, Hpade)
    print('H_h(s) =', H_h)
    Kp = 0.52
    Ti = 18
    H_PI = Kp * (Ti * s + 1) / (Ti * s)
    print('H_PI = ', H_PI)

    Tf = 0.5
    H_lpf = 1 / (Tf * s + 1)
    print('H_lpf = ', H_lpf)
    L = control.series(H_h, H_PI, H_lpf)
    print('L = ', L)

    #Tracking transfer function
    T = control.feedback(L)
    #Sensitivity tf
    S = 1-T

    #Step response of system
    t,y = control.step_response(T)
    plt.figure(1)
    plt.plot(t, y)
    plt.title("Step Response Feedback System T(s)")
    plt.grid()

    # Bode Diagram with Stability Margins
    plt.figure(2)
    control.bode(L, dB=True, deg=True, margins=True)
    # Poles and Zeros
    plt.figure(3)
    control.pzmap(T)
    p = control.pole(T)
    z = control.zero(T)
    print("poles = ", p)
    print("zeros = ", z)
    #plt.plot(p, z)

    # Calculating stability margins and crossover frequencies
    gm, pm, w180, wc = control.margin(L)
    # Convert gm to Decibel
    gmdb = 20 * np.log10(gm)
    print("wc =", f'{wc:.2f}', "rad/s")
    print("w180 =", f'{w180:.2f}', "rad/s")
    print("GM =", f'{gm:.2f}')
    print("GM =", f'{gmdb:.2f}', "dB")
    print("PM =", f'{pm:.2f}', "deg")
    # Find when Sysem is Marginally Stable (Kritical Gain - Kc)
    Kc = Kp * gm
    print("Kc=", f'{Kc:.2f}')
    plt.show()

if __name__ == '__main__':
    #Loop transfer function
    analyze_tf()
