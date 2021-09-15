import numpy as np

class Organismo():
    def __init__(self, imp, wih=None, who=None, nome=None):

        self.x_v = 0  #velocità nella direzione x
        self.y_v = 0  #velocità nella direzione y

        self.fattore_d = imp["fattore_d"]
        self.fattore_af = imp["fattore_af"]

        self.stanchezza_v = imp["stanchezza_v"]
        self.fattore_stanchezza = imp["fattore_stanchezza"]
        self.stanchezza = self.fattore_stanchezza

        self.x = np.random.uniform(imp["x_min"], imp["x_max"])
        self.y = np.random.uniform(imp["y_min"], imp["y_max"])
        
        self.x_dist_da_cibo = 0
        self.y_dist_da_cibo = 0

        self.x_dist_da_vicino = 0
        self.y_dist_da_vicino = 0

        self.fitness = 0
        self.energia = imp["e_iniziale"]

        self.wih = wih      #pesi (weight) dallo strato input allo strato nascosto
        self.who = who      #pesi (weight) dallo strato nascosto allo strato output

        self.nome = nome

    #network neurale
    def pensare(self):

        def attivazione_funzione(x):
            return np.tanh(x)

        inputs = [
            self.x_v,
            self.y_v,
            self.x_dist_da_cibo,
            self.y_dist_da_cibo,
            self.x_dist_da_vicino,
            self.y_dist_da_vicino
        ]

        h1 = attivazione_funzione(np.dot(self.wih, inputs))                   #strato nascosto
        out = attivazione_funzione(np.dot(self.who, h1)) * self.fattore_af    #strato output
        
        #aggiornamento velocità
        self.x_v = float(out[0]) + self.x_v * self.fattore_d 
        self.y_v = float(out[1]) + self.y_v * self.fattore_d

        #aggiornamento posizione
        self.x += self.x_v 
        self.y += self.y_v

        #aggiornamento stanchezza
        if self.stanchezza_v == True:
            self.stanchezza = self.fattore_stanchezza * np.hypot(self.x_v, self.y_v) * 4

        #aggiornamento energia
        self.energia -= self.stanchezza
        
