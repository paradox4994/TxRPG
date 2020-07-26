import tkinter
from Player import *
from Attack import *
mainwin = tkinter.Tk()
from tkinter import ttk

class mainGUI:
    def start(self):
        self.oup = tkinter.Frame(mainwin)
        self.oup.grid(row=0,column=0,padx=8,pady=8,rowspan=3)

        self.inp = tkinter.Frame(mainwin)
        self.inp.grid(row=3,column=0,padx=8,pady=8)

        self.stats = tkinter.Frame(mainwin)
        self.stats.grid(row=0,column=1,padx=8,pady=8)

        self.misc = tkinter.Frame(mainwin)
        self.misc.grid(row=1,column=1,padx=8,pady=8)


        self.oupText = tkinter.Text(self.oup, height = 30, width = 60)
        self.oupText.pack()

        self.pinp=''
        self.ip = tkinter.Entry(self.inp,textvariable=self.pinp,width=80)
        self.ip.pack()

        self.ph = 0
        self.hpL = tkinter.Label(self.stats, text='HP',font = "Verdana 10 bold")
        self.hpL.grid(row=0,column=0)
        self.hpO = tkinter.Label(self.stats,text=self.ph)
        self.hpO.grid(row=0,column=1)
        self.mpL = tkinter.Label(self.stats,text='MP',font = "Verdana 10 bold")
        self.mpL.grid(row=0,column=2)
        self.mpO = tkinter.Label(self.stats,text=self.ph)
        self.mpO.grid(row=0,column=3)

        self.strL = tkinter.Label(self.stats, text='STR',font = "Verdana 10 bold")
        self.strL.grid(row=1,column=0)
        self.strO = tkinter.Label(self.stats,text=self.ph)
        self.strO.grid(row=1,column=1)
        self.intL = tkinter.Label(self.stats,text='INT',font = "Verdana 10 bold")
        self.intL.grid(row=1,column=2)
        self.intO = tkinter.Label(self.stats,text=self.ph)
        self.intO.grid(row=1,column=3)

        self.dexL = tkinter.Label(self.stats, text='DEX',font = "Verdana 10 bold")
        self.dexL.grid(row=2,column=0)
        self.dexO = tkinter.Label(self.stats,text=self.ph)
        self.dexO.grid(row=2,column=1)
        self.defL = tkinter.Label(self.stats,text='DEF',font = "Verdana 10 bold")
        self.defL.grid(row=2,column=2)
        self.defO = tkinter.Label(self.stats,text=self.ph)
        self.defO.grid(row=2,column=3)

        self.luckL = tkinter.Label(self.stats, text='LUCK',font = "Verdana 10 bold")
        self.luckL.grid(row=3,column=0)
        self.luckO = tkinter.Label(self.stats,text=self.ph)
        self.luckO.grid(row=3,column=1)
        self.goldL = tkinter.Label(self.stats,text='GOLD',font = "Verdana 10 bold")
        self.goldL.grid(row=3,column=2)
        self.goldO = tkinter.Label(self.stats,text=self.ph)
        self.goldO.grid(row=3,column=3)

        self.xpL = tkinter.Label(self.stats, text='XP',font = "Verdana 10 bold")
        self.xpL.grid(row=4,column=0)
        self.xpO = tkinter.Label(self.stats,text=self.ph)
        self.xpO.grid(row=4,column=1)
        self.lvlL = tkinter.Label(self.stats,text='LEVEL',font = "Verdana 10 bold")
        self.lvlL.grid(row=4,column=2)
        self.lvlO = tkinter.Label(self.stats,text=self.ph)
        self.lvlO.grid(row=4,column=3)


        tabs = ttk.Notebook(self.misc,height=350)
        inv = ttk.Frame(tabs)
        tabs.add(inv, text='Inventory')
        equips = ttk.Frame(tabs)
        tabs.add(equips, text='Equipmets')
        store = ttk.Frame(tabs)
        tabs.add(store, text='Store')
        tabs.pack()
        mainwin.mainloop()
