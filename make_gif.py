import glob
import moviepy.editor as mpy
import os

def make_gif(imp): #crea un gif partendo da tutti i frame generati in precedenza 

    nome_gif = imp["nome"] + imp["data"] 
    fps = imp["gif_fps"]
    lista_file = glob.glob("*.png")

    list.sort(lista_file, key=lambda x: int(x.split(".png")[0]))
    clip = mpy.ImageSequenceClip(lista_file[0:imp["t_sim"]], fps=fps)
    clip.write_gif("{}.gif".format(nome_gif), fps=fps)

    del clip
    a = [os.remove(f) for f in lista_file]
