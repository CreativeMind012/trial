#done
#Set the background and foreground colours of the labels by using the bg and fg attribute of the label.
from tkinter import *
from PIL import ImageTk, Image
import random

root=Tk()
root.title("Pokemon")
root.geometry("800x600")

root.configure(background="orange")

button = ImageTk.PhotoImage(Image.open("button.jpg"))

squirtle = ImageTk.PhotoImage(Image.open("squirtle.jpg"))
ratata = ImageTk.PhotoImage(Image.open("ratata.jpg"))
pikachu = ImageTk.PhotoImage(Image.open("pikachu.jpg"))
persion = ImageTk.PhotoImage(Image.open("persion.jpg"))
paras = ImageTk.PhotoImage(Image.open("paras.jpg"))
nidoking = ImageTk.PhotoImage(Image.open("nidoking.jpg"))
meowth = ImageTk.PhotoImage(Image.open("meowth.jpg"))
kadabra = ImageTk.PhotoImage(Image.open("kadabra.jpg"))
jigglypuff = ImageTk.PhotoImage(Image.open("jigglypuff.jpg"))
charmender = ImageTk.PhotoImage(Image.open("charmender.jpg"))
abra = ImageTk.PhotoImage(Image.open("abra.jpg"))
bulbasour = ImageTk.PhotoImage(Image.open("bulbasour.jpg"))
Iyvasour = ImageTk.PhotoImage(Image.open("Iyvasour.jpg"))

poke_list = [squirtle,ratata,pikachu,persion,paras,nidoking,meowth,kadabra,jigglypuff,charmender,abra,bulbasour,Iyvasour]
power_list= [50,40,200,70,40,70,60,70,70,50,30,60,100]

lab_pl1 = Label(root,text="Player 1",bg="red",fg="white")
lab_pl1.place(relx=0.1,rely=0.2)
p1Sc = Label(root,bg="royal blue",fg="black")
p1Sc.place(relx=1,rely=0.3)

lab_pl2 = Label(root,text="Player 2",bg="red",fg="white")
lab_pl2.place(relx=0.8,rely=0.2)
p2Sc = Label(root,bg="royal blue",fg="black")
p2Sc.place(relx=8,rely=0.3)

lab_img = Label(root)
lab_img.place(relx=0.3,rely=0.2)

pl1_score = 0
def player1():
    global pl1_score
    a = random.randint(0,12)
    rand_poke = poke_list[a]
    lab_img["image"] = rand_poke
    
    rand_power = power_list[a]
    pl1_score = pl1_score + int(rand_power)
    p1Sc["text"] = " "+str(pl1_score)
    
pl2_score = 0
def player2():
    global pl2_score
    b = random.randint(0,12)
    rand_poke2 = poke_list[b]
    lab_img["image"] = rand_poke2
    
    rand_power2 = power_list[b]
    pl2_score = pl2_score + int(rand_power2)
    p2Sc["text"] = " "+str(pl2_score)
    
btn1 = Button(root,image=button,command=player1)
btn1.place(relx=0.05,rely=0.4)

btn2 = Button(root,image=button,command=player2)
btn2.place(relx=0.75,rely=0.4)

root.mainloop() 
