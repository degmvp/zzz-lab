import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D

def generate(X, Y, phi):
    R = 1 - np.sqrt(X**2 + Y**2)
    return np.cos(2 * np.pi * X + phi) * R

def update(phi, ax, X, Y):
    ax.cla()  # Limpa o frame anterior
    Z = generate(X, Y, phi)
    ax.plot_wireframe(X, Y, Z, 
                      rstride=2, 
                      cstride=2,
                      color='cyan',      # Cor do wireframe
                      linewidth=0.8)     # Espessura das linhas
    ax.set_facecolor('black')  # Cor de fundo dos eixos 3D
    ax.grid(False)             # Remove grid
    ax.axis('off')             # Remove eixos

def gcubo():
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

    # Cria a animação
    anim = FuncAnimation(fig, update, frames=np.linspace(0, 360 / 2 / np.pi, 100),
                         fargs=(ax, X, Y), interval=50)

    # Salva a animação como um arquivo GIF
    anim.save('grafx.gif', writer='imagemagick', fps=20)
    print("Animação salva como 'grafx.gif'.")

gcubo()