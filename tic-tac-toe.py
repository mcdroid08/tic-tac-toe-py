from tkinter import *
from tkinter import ttk
from tkinter import messagebox

activeplayer=1 #first turn of player 1
p1=[]
p2=[]
p3=[]
winner=-1

root=Tk()
root.title('Tic Tac Toy : Player 1')

#defing styles
stylemain=ttk.Style()
stylemain.theme_use('classic')
stylemain.configure('TButton',font=('Arial',24,'bold'),foreground='Grey',background='White')
stylemain.map('TButton',foreground=[('pressed','Red'),('disabled','Black')],background=[('pressed','green'),('disabled','Grey')])

style2=ttk.Style()
style2.configure('style2.TButton',background='Green',foreground='Red',font=('Arial',24,'bold'))
style2.map('style2.TButton',foreground=[('pressed','Grey'),('disabled','Black')],background=[('pressed','White'),('disabled','Grey')])

#defining all 10 buttuouns and their calling fnction
bu1=ttk.Button(root,text='-')
bu1.grid(row=0,column=0,sticky='snew',ipady=20,ipadx=30)
bu1.config(command=lambda:Buclick(1))

bu2=ttk.Button(root,text='-')
bu2.grid(row=0,column=1,sticky='snew',ipady=20,ipadx=60)
bu2.config(command=lambda:Buclick(2))

bu3=ttk.Button(root,text='-')
bu3.grid(row=0,column=2,sticky='snew',ipady=20,ipadx=60)
bu3.config(command=lambda:Buclick(3))

bu4=ttk.Button(root,text='-')
bu4.grid(row=1,column=0,sticky='snew',ipady=20,ipadx=30)
bu4.config(command=lambda:Buclick(4))

bu5=ttk.Button(root,text='-')
bu5.grid(row=1,column=1,sticky='snew',ipady=20,ipadx=60)
bu5.config(command=lambda:Buclick(5))

bu6=ttk.Button(root,text='-')
bu6.grid(row=1,column=2,sticky='snew',ipady=20,ipadx=60)
bu6.config(command=lambda:Buclick(6))

bu7=ttk.Button(root,text='-')
bu7.grid(row=2,column=0,sticky='snew',ipady=20,ipadx=30)
bu7.config(command=lambda:Buclick(7))

bu8=ttk.Button(root,text='-')
bu8.grid(row=2,column=1,sticky='snew',ipady=20,ipadx=60)
bu8.config(command=lambda:Buclick(8))

bu9=ttk.Button(root,text='-')
bu9.grid(row=2,column=2,sticky='snew',ipady=20,ipadx=60)
bu9.config(command=lambda:Buclick(9))

resetbu=ttk.Button(root,text='Reset')
resetbu.grid(row=3,column=0,sticky='snew',ipady=20,ipadx=30)
resetbu.config(command=lambda : reset())
resetbu.configure(style='style2.TButton')

#window properties
root.rowconfigure(0,weight=1) #for changing size label with window increase
root.rowconfigure(1,weight=1) # weight 2 for twice the size of others
root.rowconfigure(2,weight=1)
root.columnconfigure(0,weigh=1)
root.columnconfigure(1,weigh=1)
root.columnconfigure(2,weigh=1)


def reset():
    '''This will reset all th buttouns and winner and player entered data in last game'''
    global p1
    global p2
    global p3
    global winner
    global activeplayer

    Buttons=[bu1,bu2,bu3,bu4,bu5,bu6,bu7,bu8,bu9]
    for bu in Buttons:
        bu.config(text='-')
        bu.state(['!disabled'])
    p1=[]
    p2=[]
    p3=[]
    winner=-1
    activeplayer=1

def Buclick(idButton):
    '''This function will define will will happpen when any buttoun got clicked
    param : idbuttoun ; Butrtoun nubmber that got clicked 
    '''
    global  activeplayer

    if activeplayer==1:
        root.title('Tic Tac Toy : Player 2')
        p1.append(idButton)
        if idButton not in p3:
            p3.append(idButton)
        print("Player 1 : {}".format(p1))
        setButton(idButton, 'X')
        checkwinner(activeplayer)
        activeplayer=2

    else:
        root.title('Tic Tac Toy : Player 1')
        p2.append(idButton)
        if idButton not in p3:
            p3.append(idButton)
        print("Player 2 : {}".format(p2))
        setButton(idButton, 'O')
        checkwinner(activeplayer)
        activeplayer=1

def setButton(idButton,Playersymbol):
    '''This function will change all the styles after got clicked'''
    
    if idButton==1:
        bu1.config(text=Playersymbol)
        bu1.state(['disabled'])

    elif idButton==2:
        bu2.config(text=Playersymbol)
        bu2.state(['disabled'])
    
    elif idButton==3:
        bu3.config(text=Playersymbol)
        bu3.state(['disabled'])
    
    elif idButton==4:
        bu4.config(text=Playersymbol)
        bu4.state(['disabled'])

    elif idButton==5:
        bu5.config(text=Playersymbol)
        bu5.state(['disabled'])

    elif idButton==6:
        bu6.config(text=Playersymbol)
        bu6.state(['disabled'])

    elif idButton==7:
        bu7.config(text=Playersymbol)
        bu7.state(['disabled'])

    elif idButton==8:
        bu8.config(text=Playersymbol)
        bu8.state(['disabled'])

    elif idButton==9:
        bu9.config(text=Playersymbol)
        bu9.state(['disabled'])

def checkwinner(activeP):
    '''This function will check who is winner
    param : activeP ; active player that last clicked on buttoun
    '''
    global winner
    global p1
    global p2

    nowinlist=[1,2,3,4,5,6,7,8,9] #for comparing that no winner
    p3.sort()
    print(p3)

    if activeP == 1:

        if (1 in p1) and (2 in p1) and (3 in p1):
            winner=1
        elif (4 in p1) and (5 in p1) and (6 in p1):
            winner=1
        elif (7 in p1) and (8 in p1) and (9 in p1):
            winner=1
        elif (1 in p1) and (4 in p1) and (7 in p1):
            winner=1
        elif (2 in p1) and (5 in p1) and (8 in p1):
            winner=1
        elif (3 in p1) and (6 in p1) and (9 in p1):
            winner=1
        elif (1 in p1) and (5 in p1) and (9 in p1):
            winner=1
        elif (3 in p1) and (5 in p1) and (7 in p1):
            winner=1

    elif activeP==2:

        if (1 in p2) and (2 in p2) and (3 in p2):
            winner=2
        elif (4 in p2) and (5 in p2) and (6 in p2):
            winner=2
        elif (7 in p2) and (8 in p2) and (9 in p2):
            winner=2
        elif (1 in p2) and (4 in p2) and (7 in p2):
            winner=2
        elif (2 in p2) and (5 in p2) and (8 in p2):
            winner=2
        elif (3 in p2) and (6 in p2) and (9 in p2):
            winner=2
        elif (1 in p2) and (5 in p2) and (9 in p2):
            winner=2
        elif (3 in p2) and (5 in p2) and (7 in p2):
            winner=2
    #generating message if win or no win
    if winner == 1 or winner == 2: 
        if winner==1:
            messagebox.showinfo(title='Congratulation',message='Player 1 is winner')
        else:
            messagebox.showinfo(title='Congratulation',message='Player 2 is winner')

        reset()

    elif (p3)==nowinlist:
        messagebox.showerror(title='OPPS..',message='No winner !! Try Again >>>')
        reset()

root.mainloop()


