import pokemon
from instancias import *
import tkinter as tk
from tkinter import messagebox


# miss = 100 - ataque.accuracy

jogador_current = 1
def controle_jogador(pokemon):
    global jogador_current
    if jogador_current == 1:
        messagebox.showinfo("Escolha", f"Jogador 1 escolheu {pokemon.nome}")
        jogador_current = 2
    else:
        messagebox.showinfo("Escolha", f"Jogador 2 escolheu {pokemon.nome}")
        jogador_current = 1


root = tk.Tk()
root.title("PokeBattle.py")
root.geometry("800x600")

btn_sceptile = tk.Button(root, text="Sceptile", command=lambda: controle_jogador(sceptile))
btn_sceptile.pack(pady=10)

btn_infernape = tk.Button(root, text="Infernape", command=lambda: controle_jogador(infernape))
btn_infernape.pack(pady=10)

btn_blastoise = tk.Button(root, text="Blastoise", command=lambda: controle_jogador(blastoise))
btn_blastoise.pack(pady=10)

root.mainloop()