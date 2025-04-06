import numpy as np
import plotly.graph_objs as go
import plotly.offline as pyo

def generate(X, Y, phi):
    R = 1 - np.sqrt(X**2 + Y**2)
    return np.cos(2 * np.pi * X + phi) * R

def create_plot():
    xs = np.linspace(-1, 1, 50)
    ys = np.linspace(-1, 1, 50)
    X, Y = np.meshgrid(xs, ys)
    Z = generate(X, Y, 0.0)

    # Cria o gráfico 3D como wireframe
    fig = go.Figure(data=[go.Surface(
        z=Z, x=X, y=Y,
        colorscale='Viridis',
        contours=dict(
            z=dict(show=True, usecolormap=True, highlightcolor="limegreen", project_z=True)
        ),
        showscale=False,
        opacity=0.5
    )])

    # Configurações do layout
    fig.update_layout(
        title='Gráfico 3D Interativo - Wireframe',
        scene=dict(
            xaxis=dict(title='X'),
            yaxis=dict(title='Y'),
            zaxis=dict(title='Z')
        ),
        template='plotly_dark'  # Template dark
    )

    # Define o nome do arquivo como 'grafx.html'
    filename = 'grafx.html'  # Nome do arquivo fixo

    # Salva o gráfico como um arquivo HTML
    pyo.plot(fig, filename=filename, auto_open=False)

create_plot()