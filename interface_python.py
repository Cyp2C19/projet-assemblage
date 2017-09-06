from tkinter import *
from tkinter.filedialog import *
from DNA_manage import *

fenetre = Tk()
DNA_seq = ""

def select_file():
    filepath = askopenfilename(title="Select DNA sequence", filetypes=[('text files','.txt')])
    fichier = open(filepath, "r")
    global DNA_seq
    DNA_seq = fichier.read()
    fichier.close()
    Label(label1,text="Your selected DNA sequence : ").pack()
    Label(label1, text=DNA_seq).pack()
    createReads(DNA_seq,tReads.get(),deltaReads.get(),tOverlap.get(),depth.get())


def buttomAction():
    createReads(DNA_seq,tReads.get(),deltaReads.get(),tOverlap.get(),depth.get())

label1=LabelFrame(fenetre, text="Input DNA sequence", padx=20,pady=20)
label1.pack(fill="both",expand="yes")
Label(label1, text="Select your DNA sequence in txt format : ").pack()
bouton = Button(label1, text="Choose file", command=select_file).pack()

label2=LabelFrame(fenetre, text="Reads building", padx=250, pady=50)
label2.pack(fill="both",expand="yes")
Label(label2,text="Select the length reads that you want : ").pack()
tReads = Spinbox(label2,from_=5,to=10)
tReads.pack()
Label(label2,text="Select the delta variation : ").pack()
deltaReads = Spinbox(label2,from_=1,to=4)
deltaReads.pack()
Label(label2,text="Select the maximum overlap : ").pack()
tOverlap = Spinbox(label2,from_=0,to=4)
tOverlap.pack()
Label(label2,text="Select the depth").pack()
depth = Spinbox(label2,from_=1,to=10)
depth.pack()

Button(label2, text="Change value", command=buttomAction).pack()

label3=LabelFrame(fenetre, text="Output results", padx=20,pady=20)
label3.pack(fill="both",expand="yes")
Label(label3,text="Reads :").pack()

fenetre.mainloop()
