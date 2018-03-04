from tkinter import *
from tkinter import ttk

def hesapla(*args):
    try:
        gelirs = float(gelir.get())
        giders = float(gider.get())
        result = gelirs - giders
        if(result > 0):
            state = result," Karlı"
        elif(result == 0):
            state = result," Başabaş"
        else:
            state = result ," Tebrikler BATTINIZ :)"
        durum.set(state)
    except ValueError:
        pass
    
root = Tk()
root.title("İşletme Kar Takip Programı")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

fGelir = StringVar()
pGelir = StringVar()
kGelir = StringVar()

uGider = StringVar()
fGider = StringVar()
pGider = StringVar()
kGider = StringVar()
mGider = StringVar()

durum = StringVar()

fGelir_entry = ttk.Entry(mainframe, width=10, textvariable=fGelir)
pGelir_entry = ttk.Entry(mainframe, width=10, textvariable=fGelir)
kGelir_entry = ttk.Entry(mainframe, width=10, textvariable=fGelir)

#Giderler

uGider_entry = ttk.Entry(mainframe, width=10, textvariable=uGider)
fGider_entry = ttk.Entry(mainframe, width=10, textvariable=uGider)
pGider_entry = ttk.Entry(mainframe, width=10, textvariable=uGider)
kGider_entry = ttk.Entry(mainframe, width=10, textvariable=uGider)
mGider_entry = ttk.Entry(mainframe, width=10, textvariable=uGider)

ttk.Label(mainframe, text="Finansman Geliri ").grid(column=1, row=1, sticky=W)
fGelir_entry.grid(column=2, row=1, sticky=(W, E))

ttk.Label(mainframe, text="Finansman Geliri ").grid(column=1, row=2, sticky=W)
pGelir_entry.grid(column=2, row=2, sticky=(W, E))

ttk.Label(mainframe, text="Kira Geliri ").grid(column=1, row=3, sticky=W)
kGelir_entry.grid(column=2, row=3, sticky=(W, E))

ttk.Label(mainframe, text="--------------------Giderler---------------").grid(column=2, row=4, sticky=W)

#Giderler
ttk.Label(mainframe, text="Ücret Gideri ").grid(column=1, row=5, sticky=W)
uGider_entry.grid(column=2, row=5, sticky=(W, E))

ttk.Label(mainframe, text="Finansman Gideri ").grid(column=1, row=6, sticky=W)
fGider_entry.grid(column=2, row=6, sticky=(W, E))

ttk.Label(mainframe, text="Pazar Gideri ").grid(column=1, row=7, sticky=W)
pGider_entry.grid(column=2, row=7, sticky=(W, E))

ttk.Label(mainframe, text="Kira Gideri ").grid(column=1, row=8, sticky=W)
kGider_entry.grid(column=2, row=8, sticky=(W, E))

ttk.Label(mainframe, text="Muhasebe Gideri ").grid(column=1, row=9, sticky=W)
mGider_entry.grid(column=2, row=9, sticky=(W, E))


ttk.Label(mainframe, textvariable=durum).grid(column=2, row=11, sticky=(W, E))


ttk.Button(mainframe, text="Hesapla", command=hesapla).grid(column=3, row=12, sticky=W)



ttk.Label(mainframe, text="Durum :").grid(column=1, row=12, sticky=E)


for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

#gelir_entry.focus()
#gider_entry.focus()
root.bind('<Return>', hesapla)

root.mainloop()
