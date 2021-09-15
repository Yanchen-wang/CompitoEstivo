import datetime
import numpy as np
from numpy.random.mtrand import seed
from cibo import Cibo
from organismo import Organismo
import plot
from simulazione import simulare

#impostazioni
imp = {}
imp["nome"] = "simulazione evoluzione"        
imp["pop_iniziale"] = 50
imp["pop_cap"] = None
imp["c_iniziale"] = 25         #numero di cibo
imp["e_iniziale"] = 200        #energia iniziale degli organismi
imp["energia_cibo"] = 100
imp["energia_riproduzione"] = 250
imp["costo_riproduzione"] = 100
imp["t_sim"] = 1000            #tempo simulazione
imp["fattore_m"] = 0.5         #mutazioni
imp["fattore_af"] = 0.5        #modifica il cambiamento dei pesi
imp["fattore_stanchezza"] = 3  #fattore che influenza la velocità a cui un organismo perde energia
imp["fattore_d"] = 0.12        #decellerazione
imp["cibo_rigenerato"] = 0.4   #la percentuale del cibo che viene rigenerato a ogni rigenerazione
imp["tempo_rigenerazione"] = 5 #frequenza di rigenerazione di cibo
imp["seed"] = 420               #per riprodurre simulazioni
imp["x_max"] = 3.0
imp["x_min"] = -3.0
imp["y_max"] = 3.0
imp["y_min"] = -3.0
imp["n_input"] = 6
imp["n_hidden"] = 5
imp["n_output"] = 2
imp["gif_fps"] = 12
imp["data"] = datetime.datetime.now().strftime("_%Y-%m-%d_%H-%M-%S")
imp["record_gif"] = True
imp["anticollisione"] = True
imp["cornice_letale"] = True
imp["cornice_larga"] = True   
imp["stanchezza_v"] = True     #se la stanchezza dipende dalla velocità dell'organismo
imp["+info"] = True            #se visualizzare più informazioni nel GIF (richiede record_gif = True)
imp["versione"] = "1.2.8"

def run(imp):

    np.random.seed(imp["seed"]) #seed 

    #Aggiungere cibo alla mappa
    foods = []
    for i in range(0, imp["c_iniziale"]):
        foods.append(Cibo(imp))

    #Aggiungere organismi alla mappa
    organismi = []
    for i in range(0, imp["pop_iniziale"]):
        wih_iniziale = np.random.uniform(-1, 1, (imp["n_hidden"], imp["n_input"]))      #pesi (input -> nascosto)
        who_iniziale = np.random.uniform(-1, 1, (imp["n_output"], imp["n_hidden"]))     #pesi (nascosto -> output)

        organismi.append(Organismo(imp, wih_iniziale, who_iniziale, nome="gen[x]-org["+str(i)+"]"))


    organismi, dati, tempo = simulare(imp, organismi, foods) #fa partire la simulazione

    plot.plot_stats(imp, dati, tempo) #crea una immagine di un grafico che visualizza il numero di popolazione per ciascun istante

run(imp)