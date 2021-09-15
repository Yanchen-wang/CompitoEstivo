from matplotlib import pyplot as plt
from matplotlib.patches import Circle 
from matplotlib import use
use("Agg")

def plot_organismo(org, ax): #definisce l'apparenza di un organismo

    circle = Circle([org.x, org.y], 0.05, edgecolor="b", facecolor="lightblue", zorder=8)
    ax.add_artist(circle)

    edge = Circle([org.x, org.y], 0.05, edgecolor="blue", facecolor="None", zorder=8)
    ax.add_artist(edge)


def plot_cibo(cibo, ax): #definisce l'apparenza di un'unità di cibo

    circle = Circle([cibo.x, cibo.y], 0.03, edgecolor="darkred", facecolor="red", zorder=5)
    ax.add_artist(circle)


def plot_frame(imp, organismi, cibo, tempo, popolazione): #genera un frame della simulazione
    fig, ax = plt.subplots()
    fig.set_size_inches(9.6, 5.4)

    if imp["cornice_larga"] == True:
        plt.xlim([imp["x_min"] + imp["x_min"] * 0.45, imp["x_max"] + imp["x_max"] * 0.45])
        plt.ylim([imp["y_min"] + imp["y_min"] * 0.45, imp["y_max"] + imp["y_max"] * 0.45])
    else:
        plt.xlim([imp["x_min"] + imp["x_min"] * 0.05, imp["x_max"] + imp["x_max"] * 0.05])
        plt.ylim([imp["y_min"] + imp["y_min"] * 0.05, imp["y_max"] + imp["y_max"] * 0.05])

    for organismo in organismi:
        plot_organismo(organismo, ax)

    for cibo in cibo:
        plot_cibo(cibo, ax)

    ax.set_aspect("equal")
    frame = plt.gca()
    frame.axes.get_xaxis().set_ticks([])
    frame.axes.get_yaxis().set_ticks([])

    plt.figtext(0.025, 0.95, r"TEMPO: "+str(tempo)) # visulalizzazione delle informazioni
    if imp["+info"] == True:
        plt.figtext(0.025, 0.90, r"POPOLAZIONE: "+ str(popolazione))
        plt.figtext(0.025, 0.85, r"SEED: "+ str(imp["seed"]))
        plt.figtext(0.025, 0.80, r"ANTI_COLLISIONE: "+ str(imp["anticollisione"]))
        plt.figtext(0.025, 0.75, r"CORNICE_LARGA: "+ str(imp["cornice_larga"]))
        plt.figtext(0.025, 0.70, r"CORNICE_LETALE: "+ str(imp["cornice_letale"]))
        plt.figtext(0.025, 0.65, r"STANCHEZZA_V: "+ str(imp["stanchezza_v"]))
        plt.figtext(0.80, 0.95, r"version: "+ str(imp["versione"]))
        
    plt.savefig(str(tempo)+".png", dpi=120)


def plot_stats(imp, dati, tempo): #genera il grafico delle statistiche della popolazione
    
    nome_file = imp["nome"] + imp["data"] + ".jpg"
    
    fig, ax = plt.subplots()

    tempo = list(range(tempo+1))

    ax.plot(tempo, dati)

    ax.set_xlabel("tempo simulazione")
    ax.set_ylabel("popolazione")

    fig.savefig(nome_file, dpi=200)