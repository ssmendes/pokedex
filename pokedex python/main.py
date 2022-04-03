from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

from dados import *

########## cores ##########
co0 = "#444466" #preto
co1 = "#feffff" #branco
co2 = "#6f9fbd" #azul
co3 = "#38576b" #valor
co4 = "#403d3d" #letra
co5 = "#ef5350" #vermelho

#criando janela
janela = Tk()
janela.title('')
janela.geometry('550x510')
janela.configure(bg=co1)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=272)

style = ttk.Style(janela)
style.theme_use("clam")

#criando frame
frame_pokemon = Frame(janela, width=550, height=290, relief='flat')
frame_pokemon.grid(row=1, column=0)

def trocar_pokemon(i):
    global imagem_pokemon, pok_imagem
    
    frame_pokemon['bg'] = pokemon[i]['tipo'][3]
    
    pok_nome['text'] = i
    pok_nome['bg'] = pokemon[i]['tipo'][3]

    pok_tipo['text'] = pokemon[i]['tipo'][1]
    pok_tipo['bg'] = pokemon[i]['tipo'][3]
    
    pok_id['text'] = pokemon[i]['tipo'][0]
    pok_id['bg'] = pokemon[i]['tipo'][3]
    
    imagem_pokemon = pokemon[i]['tipo'][2]
    
    # imagem do pokemon
    imagem_pokemon = Image.open(imagem_pokemon)
    imagem_pokemon = imagem_pokemon.resize((238, 238))
    imagem_pokemon = ImageTk.PhotoImage(imagem_pokemon)
    pok_imagem = Label(frame_pokemon, image=imagem_pokemon, relief='flat', bg=pokemon[i]['tipo'][3], fg=co1)
    pok_imagem.place(x=60, y=50)
    pok_tipo.lift()
    
    pok_hp['text'] = pokemon[i]['status'][0]
    pok_ataque['text'] = pokemon[i]['status'][1]
    pok_defesa['text'] = pokemon[i]['status'][2]
    pok_velocidade['text'] = pokemon[i]['status'][3]
    pok_total['text'] = pokemon[i]['status'][4]
    
    pok_hb_1['text'] = pokemon[i]['habilidades'][0]
    pok_hb_2['text'] = pokemon[i]['habilidades'][1]
    

#nome
pok_nome = Label(frame_pokemon, text='', relief='flat', anchor=CENTER, font=('Fixedsys 20'), fg=co1)
pok_nome.place(x=12, y=15)

# categoria
pok_tipo = Label(frame_pokemon, text='', relief='flat', anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co1)
pok_tipo.place(x=12, y=50)

#id
pok_id = Label(frame_pokemon, text='', relief='flat', anchor=CENTER, font=('Fixedsys 10'), bg=co1, fg=co1)
pok_id.place(x=12, y=75)


# status
pok_status = Label(janela, text='Status', relief='flat', anchor=CENTER, font=('Verdana 20'), bg=co1, fg=co0)
pok_status.place(x=15, y=310)

pok_hp = Label(janela, text='HP: 300', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pok_hp.place(x=15, y=360)

pok_ataque = Label(janela, text='Ataque: 600', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pok_ataque.place(x=15, y=385)

pok_defesa = Label(janela, text='Defesa: 500', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pok_defesa.place(x=15, y=410)

pok_velocidade = Label(janela, text='Velocidade: 300', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pok_velocidade.place(x=15, y=435)

pok_total = Label(janela, text='Total: 1700', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pok_total.place(x=15, y=460)

# habilidades
pok_habilidades = Label(janela, text='Habilidades', relief='flat', anchor=CENTER, font=('Verdana 20'), bg=co1, fg=co4)
pok_habilidades.place(x=180, y=310)

pok_hb_1 = Label(janela, text='Jato de água', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pok_hb_1.place(x=195, y=360)

pok_hb_2 = Label(janela, text='Soco elétrico', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pok_hb_2.place(x=195, y=385)

#criando botões
# imagem do pokemon
imagem_pokemon_1 = Image.open('imagens/cabeca-pikachu.png')
imagem_pokemon_1 = imagem_pokemon_1.resize((40, 40))
imagem_pokemon_1 = ImageTk.PhotoImage(imagem_pokemon_1)
b_pok_1 = Button(janela, command=lambda:trocar_pokemon('Pikachu'), image=imagem_pokemon_1, text='Pikachu', width=150, relief='raise', overrelief=RIDGE, compound=LEFT, padx=5, anchor=NW, font=('Verdana 12'), bg=co1, fg=co0)
b_pok_1.place(x=375, y=10)

# imagem do bulbasaur
imagem_pokemon_2 = Image.open('imagens/cabeca-bulbasaur.png')
imagem_pokemon_2 = imagem_pokemon_2.resize((40, 40))
imagem_pokemon_2 = ImageTk.PhotoImage(imagem_pokemon_2)
b_pok_2 = Button(janela, command=lambda:trocar_pokemon('Bulbasaur'), image=imagem_pokemon_2, text='Bulbasaur', width=150, relief='raise', overrelief=RIDGE, compound=LEFT, padx=5, anchor=NW, font=('Verdana 12'), bg=co1, fg=co0)
b_pok_2.place(x=375, y=65)

# imagem do charmander
imagem_pokemon_3 = Image.open('imagens/cabeca-charmander.png')
imagem_pokemon_3 = imagem_pokemon_3.resize((40, 40))
imagem_pokemon_3 = ImageTk.PhotoImage(imagem_pokemon_3)
b_pok_3 = Button(janela, command=lambda:trocar_pokemon('Charmander'), image=imagem_pokemon_3, text='Charmander', width=150, relief='raise', overrelief=RIDGE, compound=LEFT, padx=5, anchor=NW, font=('Verdana 12'), bg=co1, fg=co0)
b_pok_3.place(x=375, y=120)

# imagem do gyarados
imagem_pokemon_4 = Image.open('imagens/cabeca-gyarados.png')
imagem_pokemon_4 = imagem_pokemon_4.resize((40, 40))
imagem_pokemon_4 = ImageTk.PhotoImage(imagem_pokemon_4)
b_pok_4 = Button(janela, command=lambda:trocar_pokemon('Gyarados'), image=imagem_pokemon_4, text='Gyarados', width=150, relief='raise', overrelief=RIDGE, compound=LEFT, padx=5, anchor=NW, font=('Verdana 12'), bg=co1, fg=co0)
b_pok_4.place(x=375, y=175)

# imagem do gengar
imagem_pokemon_5 = Image.open('imagens/cabeca-gengar.png')
imagem_pokemon_5 = imagem_pokemon_5.resize((40, 40))
imagem_pokemon_5 = ImageTk.PhotoImage(imagem_pokemon_5)
b_pok_5 = Button(janela, command=lambda:trocar_pokemon('Gengar'), image=imagem_pokemon_5, text='Gengar', width=150, relief='raise', overrelief=RIDGE, compound=LEFT, padx=5, anchor=NW, font=('Verdana 12'), bg=co1, fg=co0)
b_pok_5.place(x=375, y=230)

# imagem do dragonite
imagem_pokemon_6 = Image.open('imagens/cabeca-dragonite.png')
imagem_pokemon_6 = imagem_pokemon_6.resize((40, 40))
imagem_pokemon_6 = ImageTk.PhotoImage(imagem_pokemon_6)
b_pok_6 = Button(janela, command=lambda:trocar_pokemon('Dragonite'), image=imagem_pokemon_6, text='Dragonite', width=150, relief='raise', overrelief=RIDGE, compound=LEFT, padx=5, anchor=NW, font=('Verdana 12'), bg=co1, fg=co0)
b_pok_6.place(x=375, y=285)

import random
lista_pokemon = ['Pkachu', 'Bulbasaur', 'Charmander', 'Gyarados', 'Gengar', 'Dragonite']
pokemon_escolhido = random.sample(lista_pokemon, 1)
trocar_pokemon(pokemon_escolhido[0])

janela.mainloop()