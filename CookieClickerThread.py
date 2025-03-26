import tkinter as tk
import time 
import threading


clickMulti=1
total = 0
cps1 = 0

upgrade1 = 10
upgrade2 = 1000
upgrade3 = 10000

upgradeCPS=1000
upgradeCPS2=100000
upgradeCPS3=1000000


#Function

#Cookie Multi Calcultor
def cookieclickerCalc():
    global total, clickMulti,cps1
    total += clickMulti
    label2["text"] = total

#Cookie per second calculator
def CPSCALC():
    global cps1, total
    while True:
        time.sleep(1)
        total += cps1
        label2["text"] = total
#Upgrade 1
def upgrad1():
    global total, clickMulti,upgrade1
    if total >= upgrade1:
        total -= upgrade1 
        clickMulti = clickMulti*5
        label2["text"] = total
        upgrade1 *= 15
        upg1["text"] = f"Upgrade cost {upgrade1}"
    else:
        return
    #Upgrade2
def upgrad2():
    global total, clickMulti, upgrade2
    if total >= upgrade2:
        total -= upgrade2 
        clickMulti = clickMulti*10
        label2["text"] = total
        upgrade2 *= 150
        upg2["text"] = f"Upgrade cost {upgrade2}"
    else:
        return
#Upgrade 3
def upgrad3():
    global total, clickMulti, upgrade3
    if total >= upgrade3:
        total -= upgrade3 
        clickMulti = clickMulti*15
        label2["text"] = total
        upgrade3 *= 200
        upg3["text"] = f"Upgrade cost {upgrade3}"
    else:
        return

#Upgrade 4 (1st CPS upgrade)
def upgradCPS1():
    global total, clickMulti, upgradeCPS, cps1
    if total >= upgradeCPS:
        total -= upgradeCPS
        cps1 = cps1 + 10
        label2["text"] = total
        upgradeCPS *= 10
        CPS1upg["text"] = f"Upgrade cost {upgradeCPS}"
    else:
        return
#Upgrade 5 (2st CPS upgrade)

def upgradCPS2():
    global total, cps1, upgradeCPS2

    if total >= upgradeCPS2:
        total -= upgradeCPS2
        cps1 = cps1*15
        label2["text"] = total
        upgradeCPS2 *= 10
        CPS2upg["text"] = f"Upgrade cost {upgradeCPS2}"

#Upgrade 6 (2st CPS upgrade)

def upgradCPS3():
    global total, upgradeCPS3, cps1
    if total >= upgradeCPS3:
        total -= upgradeCPS3
        label2["text"] = total
        upgradeCPS3 *= 4
        cps1 = cps1*20
        CPS3upg["text"] = f"Upgrade cost {upgradeCPS3}"






root = tk.Tk()
upgradee1_img = tk.PhotoImage(file="./assets/upgrade1.png").subsample(2)
upgradee2_img = tk.PhotoImage(file="./assets/upgrade2.png").subsample(2)
upgradee3_img = tk.PhotoImage(file="./assets/upgrade3.png").subsample(2)

CPS1upgrade_img = tk.PhotoImage(file="./assets/upgrade4.png").subsample(2)
CPS2upgrade_img = tk.PhotoImage(file="./assets/upgrade5.png").subsample(2)
CPS3upgrade_img = tk.PhotoImage(file="./assets/upgrade6.png").subsample(2)


label2 = tk.Label(text = 0, font = ("Helvetica,50"))
label2.grid()
img=tk.PhotoImage(file = "./assets/cookie.png")
lbl = tk.Label()
btn = tk.Button(image = img, command = cookieclickerCalc)
btn.grid()
btn2upgrade = ()
ent = tk.Entry()
root.title("")

upg1 =tk.Button(root,text= f"Upgrade cost {upgrade1}" , command = upgrad1, image=upgradee1_img, compound="right")
upg1.grid(row=0, column=1)
upg2 =tk.Button(root,text= f"Upgrade cost {upgrade2}", command=upgrad2, image=upgradee2_img, compound="right")
upg2.grid(row=1,column=1)
upg3 =tk.Button(root,text= f"Upgrade cost {upgrade3}", command=upgrad3, image=upgradee3_img, compound="right")
upg3.grid(row=2,column=1)

CPS1upg = tk.Button(root,text= f"Upgrade cost {upgradeCPS}" , command = upgradCPS1, image=CPS1upgrade_img, compound="right")
CPS1upg.grid(row=3, column=1)
CPS2upg = tk.Button(root,text= f"Upgrade cost {upgradeCPS2}" , command = upgradCPS2, image=CPS2upgrade_img, compound="right")
CPS2upg.grid(row=4, column=1)
CPS3upg = tk.Button(root,text= f"Upgrade cost {upgradeCPS3}" , command = upgradCPS3, image=CPS3upgrade_img, compound="right")
CPS3upg.grid(row=5, column=1)



threading.Thread(target = CPSCALC).start()




root.mainloop()