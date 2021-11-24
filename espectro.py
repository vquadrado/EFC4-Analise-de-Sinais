import math
import numpy as np
import matplotlib.pyplot as plt

""" Rotina que exibe o espectro de magnitude (X(ejw)) de um sinal discreto """
def espectro(y,name="default"):

    #modulo da transf. de Fourier
    Y = np.abs(np.fft.fft(y))
    #frequencias avaliadas
    w = np.linspace(0,2*math.pi,Y.size)

    #exibe o grafico do espectro
    plt.figure() 
    plt.plot(w,Y/np.max(Y))
    plt.xlabel('$\Omega$ [rad]', fontsize=15)
    plt.ylabel('|$Y(e^{j\Omega})$|', fontsize=15)
    plt.grid(True)
    plt.xlim((0,2*math.pi))

    if name != "default":
        plt.savefig(f'{name}.png')
    
    return Y    