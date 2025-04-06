import random
import math
import sys

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D
import time


def generate(X, Y, phi):
    R = 1 - np.sqrt(X**2 + Y**2)
    return np.cos(2 * np.pi * X + phi) * R

def gcubo():
    plt.ion()
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # Configurações visuais
    fig.patch.set_facecolor('black')  # Cor de fundo da figura
    ax.set_facecolor('black')         # Cor de fundo dos eixos 3D
    ax.grid(False)                    # Remove grid
    ax.axis('off')                    # Remove eixos

    xs = np.linspace(-1, 1, 50)
    ys = np.linspace(-1, 1, 50)
    X, Y = np.meshgrid(xs, ys)
    Z = generate(X, Y, 0.0)

    wframe = None
    tstart = time.time()
    
    for phi in np.linspace(0, 360 / 2 / np.pi, 100):
        oldcol = wframe

        Z = generate(X, Y, phi)
        wframe = ax.plot_wireframe(X, Y, Z, 
                                  rstride=2, 
                                  cstride=2,
                                  color='cyan',      # Cor do wireframe
                                  linewidth=0.8)     # Espessura das linhas

        if oldcol is not None:
            ax.collections.remove(oldcol)

        plt.draw()
        plt.pause(0.01)  # Pequena pausa para atualização suave

    plt.ioff()
    plt.show()
   
gcubo()
sys.exit()
print("Aplicação encerrada pelo usuário.")

