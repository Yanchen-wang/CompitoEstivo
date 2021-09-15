import numpy.random as np
import plot
import funzioni_matematiche
from make_gif import make_gif
from tqdm import tqdm
from organismo import Organismo

def simulare(imp, organismi, cibi):

    tempo_totale = imp["t_sim"]
    popolazione = imp["pop_iniziale"]
    dati = []
    n = popolazione
    choices = ["sopra","sotto","destra","sinistra"]
    record_gif = imp["record_gif"]
    anticollisione = imp["anticollisione"]
    cornice_letale = imp["cornice_letale"]
    x_max = imp["x_max"]
    x_min = imp["x_min"]
    y_max = imp["y_max"]
    y_min = imp["y_min"]
    cibo_rigenerato = imp["cibo_rigenerato"]
    tempo_rigenerazione = imp["tempo_rigenerazione"]

    for tempo in tqdm(range(0, tempo_totale, 1)): #esegue tutto il codice per ciascun frame della simulazione

        np.shuffle(organismi)
        if record_gif == True: #genera immagini per ciascun frame della simulazione
            plot.plot_frame(imp, organismi, cibi, tempo, popolazione)

        if popolazione <= 0: #ferma la simulazione se avviene un'estinizione
            print("\nESTINZIONE")
            popolazione = "estinzione"
            tempo = tempo - 1
            break

        for org1 in organismi[:]:

            if cornice_letale == True: #uccisione degli organismi al di fuori del bordo della mappa
                if org1.x > (x_max * 1.45) or org1.x < (x_min * 1.45) or org1.y > (y_max * 1.45) or org1.y < (y_min * 1.45):
                    org1.energia = 0
            
            if org1.energia <= 0: #rimuove gli organismi dalla mappa se non possiedono più di 0 energia
                organismi.remove(org1)
                popolazione -= 1

            dist_min = 10000

            for cibo in cibi:

                cibo_org_dist = funzioni_matematiche.dist_da_cibo(org1, cibo)

                if cibo_org_dist < dist_min: #fornisce dati di distanza dal cibo al network neurale
                    dist_min = cibo_org_dist
                    org1.x_dist_da_cibo, org1.y_dist_da_cibo = funzioni_matematiche.xy_dist_da_cibo(org1, cibo)

                if cibo_org_dist <= 0.1: #assunzione di cibo
                    org1.energia += cibo.energia
                    cibo.energia = 0
                    org1.d_cibo = 10000

            dist_min = 10000

            for org2 in organismi:

                if org1 is org2: #controllo che non siano lo stesso organismo
                    continue

                org_org_dist = funzioni_matematiche.dist_da_vicino(org1, org2) #distanza tra i due organismi

                if org_org_dist < dist_min: #fornisce dati di distanza dal vicino al network neurale
                    dist_min = org_org_dist
                    org1.x_dist_da_vicino, org1.y_dist_da_vicino = funzioni_matematiche.xy_dist_da_vicino(org1, org2)

                if org_org_dist <= 3 and org1.energia > imp["energia_riproduzione"] and org2.energia > imp["energia_riproduzione"]: #riproduzione
                    crossover_weight = np.random()
                    wih = (crossover_weight * org1.wih) + ((1 - crossover_weight) * org2.wih)
                    who = (crossover_weight * org1.who) + ((1 - crossover_weight) * org2.who)
        
                    mutazione = np.random()
                    if mutazione <= imp["fattore_m"]: #mutazione

                        valore_casuale_1 = np.randint(0, 2)
                        if valore_casuale_1 == 0: #mutazione del wih
                            index_row = np.randint(0, imp["n_hidden"])
                            index_col = np.randint(0, imp["n_input"])
                            wih[index_row][index_col] = wih[index_row][index_col] * np.uniform(0.9, 1.1)

                        if valore_casuale_1 == 1:#mutazione del who
                            index_row = np.randint(0, imp["n_output"])
                            index_col = np.randint(0, imp["n_hidden"])
                            who[index_row][index_col] = who[index_row][index_col] * np.uniform(0.9, 1.1)

                    popolazione += 1
                    n += 1

                    organismi.append(Organismo(imp, wih=wih, who=who, nome="org["+str(n)+"]")) #aggiunta del nuovo organismo

                    org1.energia -= imp["costo_riproduzione"]
                    org2.energia -= imp["costo_riproduzione"]

                if org_org_dist <= 0.1 and anticollisione == True: #funzione anticollisione
                    
                    if np.choice(choices) == "sopra":
                        org1.y_v -= 1
                        org2.y_v += 1
                    elif np.choice(choices) == "sotto":
                        org1.y_v += 1
                        org2.y_v -= -1
                    elif np.choice(choices) == "destra":
                        org1.x_v += 1
                        org2.x_v -= 1
                    elif np.choice(choices) == "sinistra":
                        org1.x_v -= 1
                        org2.x_v += 1

        dati.append(popolazione)

        for cibo in cibi:
            if cibo.energia <= 0:
                valore_casuale_2 = np.random()
                if tempo % tempo_rigenerazione == 0: #rigenerazione cibo
                    if valore_casuale_2 <= cibo_rigenerato:
                        cibo.rigenerare(imp)

        for org in organismi: #gli organismi penseranno a come muoversi
            org.pensare()

    if record_gif == True: # crea il gif
        plot.plot_frame(imp, organismi, cibi, tempo+1, popolazione)
        make_gif(imp)

    return organismi, dati, tempo
