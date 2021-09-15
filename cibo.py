from numpy.random import uniform

class Cibo():
    def __init__(self, imp):
        self.x = uniform(imp["x_min"], imp["x_max"])
        self.y = uniform(imp["y_min"], imp["y_max"])
        self.energia = imp["energia_cibo"] #quantità di energia che ricarica un'unità di cibo

    def rigenerare(self, imp):  #rigenera il cibo nella mappa
        if self.energia == 0:
            self.x = uniform(imp["x_min"], imp["x_max"])
            self.y = uniform(imp["y_min"], imp["y_max"])
            self.energia = imp["energia_cibo"]