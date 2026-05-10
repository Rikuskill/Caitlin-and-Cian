import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox
import random
import enemies
import player

##CREATE WINDOWS AND FRAMES BELOW vvvvvvv

root = tk.Tk()

root.title("Deep Space")
root.geometry("1920x1080")
root.attributes("-fullscreen", True)

root.configure(bg="black")
cf = tkFont.Font(family="Courier", size=25)

storytext=tk.StringVar()
enemy_desc=tk.StringVar()
enemy_name=tk.StringVar()
enemy_maxhp= 0
enemy_hp= 0
enemy_dfs= 0

mc_name=tk.StringVar()
mc_hp= 0
mc_atk= 0
mc_dfs= 0
mc_sci=tk.IntVar()
mc_dex=tk.IntVar()
mc_lck=tk.IntVar()

attack= 0

Cframe = tk.Frame(root, bg="black")
Cframe.place(relwidth=.6, relheight=1, relx=.2)

Lframe = tk.Frame(root, bg="darkgray", bd=3, relief=tk.RIDGE)
Lframe.place(relwidth=.2, relheight=1)

Rframe = tk.Frame(root, bg="darkgray", bd=3, relief=tk.RIDGE)
Rframe.place(relwidth=.2, relheight=1, relx=.8)

def update_frame():
    Cframe.destroy()
    Lframe.destroy()
    Rframe.destroy()
    create_frame()

def create_frame():
    global Cframe
    global Lframe
    global Rframe

    Cframe = tk.Frame(root, bg="black")
    Cframe.place(relwidth=.6, relheight=1, relx=.2)

    Lframe = tk.Frame(root, bg="darkgray", bd=3, relief=tk.RIDGE)
    Lframe.place(relwidth=.2, relheight=1)
    
    Rframe = tk.Frame(root, bg="darkgray", bd=3, relief=tk.RIDGE)
    Rframe.place(relwidth=.2, relheight=1, relx=.8)

    Lframe.label = tk.Label(Lframe, textvariable=mc_name, wraplength=380, fg="black", bg="darkgray", font=cf)
    Lframe.label.pack()

    button_exit = tk.Button(Lframe, text="Exit", command=root.destroy)
    button_exit.pack(side="bottom", pady=10)

##PLAYER VARIABLE CREATION BELOW vvvvvvvv

mc_hp = int(player.mc.hp)
mc_atk = int(player.mc.atk)

##NAME INPUT BELOW vvvvvvv

def name():
    update_frame()
    storytext.set("What is your name?")
    story = tk.Label(Cframe, textvariable=storytext, wraplength=950, fg="white", bg="black", font=cf)
    story.pack(pady=10)
    name_entry = tk.Entry(Cframe, textvariable=mc_name)
    name_entry.pack()
    button_greet = tk.Button(Cframe, text="Next", command=on_submit)
    button_greet.pack(pady=50)

def validate_name (name):
	if str(name).isalpha() and len(name) <= 10:
	    return True
	return False

def on_submit():
    name = mc_name.get()
    if not validate_name(name):
        messagebox.showwarning("Invalid Name", "Name must be 10 or less letters. Special characters not accepted.") 
    else:
        greet() 

##STORY STUFF BELOW vvvvvvv

def start():
    update_frame()
    storytext.set("Welcome.")
    story = tk.Label(Cframe, textvariable=storytext, wraplength=950, fg="white", bg="black", font=cf)
    story.pack(pady=10)
    button_name = tk.Button(Cframe, text="Next", command=name)
    button_name.pack(pady=50)

def greet():
    update_frame()
    tk.Label(Cframe, text="Welcome, " + mc_name.get() + ".", wraplength=950, fg="white", bg="black", font=cf).pack(pady=10)
    button_battle = tk.Button(Cframe, text="Next", command=encounter)
    button_battle.pack(pady=50)

##BATTLE STUFF BELOW vvvvvvv

def encounter():
    
    if random.random() < .25:
        enemy_desc.set(enemies.slime.desc)
        enemy_maxhp = int(enemies.slime.hp)
        global enemy_hp 
        enemy_hp = int(enemies.slime.hp)
        enemy_name.set(enemies.slime.name)
        enemy_dfs = int(enemies.slime.dfs)
        battle()

    else:
        if random.random() < .25:
            enemy_desc.set(enemies.jerboa.desc)
            enemy_hp = (enemies.jerboa.hp)
            enemy_name.set(enemies.jerboa.name)
            enemy_dfs = (enemies.jerboa.dfs)
            battle()

        else:
            escape()
            

def battle():
    update_frame()
    tk.Label(Cframe, text= enemy_desc.get(), wraplength=950, fg="white", bg="black", font=cf).pack(pady=10)
    tk.Label(Rframe, text= enemy_name.get(), wraplength=950, fg="black", bg="darkgray", font=cf).pack(pady=10)
    tk.Label(Rframe, text= str(enemy_hp) + " HP", wraplength=950, fg="black", bg="darkgray", font=cf).pack(pady=10)
    tk.Label(Lframe, text= str(mc_hp) + " HP", wraplength=950, fg="black", bg="darkgray", font=cf).pack(pady=10)


    button_atk = tk.Button(Cframe, text="Attack", command=atk)
    button_atk.place(relx=.1, rely=.5)
    button_item = tk.Button(Cframe, text="Items", command=greet)
    button_item.place(relx=.5, rely=.5)
    button_flee = tk.Button(Cframe, text="Flee", command=greet)
    button_flee.place(relx=.9, rely=.5)

def atk():
    attack = mc_atk - enemy_dfs
    enemy_hp = enemy_maxhp - attack
    tk.Label(Cframe, text= "You deal " + str(attack) + " damage to the " + enemy_name.get() + ".", wraplength=950, fg="white", bg="black", font=cf).pack(pady=10)


def escape():
    update_frame()
    tk.Label(Cframe, text= "You avoid the monsters.", wraplength=950, fg="white", bg="black", font=cf).pack(pady=10)
    button_reroll = tk.Button(Cframe, text="Reroll", command=encounter)
    button_reroll.pack(pady=50)

##Start Below vvvvv

start()

root.mainloop()