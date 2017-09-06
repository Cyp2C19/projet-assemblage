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
    scr = Scrollbar(label1,orient=VERTICAL)
    txt = Text(label1,height=4, width=50)
    scr.pack(side=RIGHT,fill=Y)
    txt.pack(side=TOP,fill=BOTH,expand=TRUE)
    scr.config(command=txt.yview)
    txt.config(yscrollcommand=scr.set)
    txt.insert(END, DNA_seq)

    reads = createReads(DNA_seq,int(tReads.get()),int(deltaReads.get()),int(tOverlap.get()),int(depth.get()))
    global text
    val = ""
    for i in range(0, len(reads)):
        val += reads[i] + " "
    text.delete('1.0',END)
    text.insert(END, val)
    text.pack()


def buttomAction():
    reads = createReads(DNA_seq,int(tReads.get()),int(deltaReads.get()),int(tOverlap.get()),int(depth.get()))
    global text
    val = ""
    for i in range(0, len(reads)):
        val += reads[i] + " "
    text.delete('0.0', END)
    text.insert(END, val)
    text.pack()

label1=LabelFrame(fenetre, text="Input DNA sequence", padx=20,pady=20)
label1.pack(fill="both",expand="yes")
Label(label1, text="Select your DNA sequence in txt format : ").pack()
bouton = Button(label1, text="Choose file", command=select_file).pack()

label2=LabelFrame(fenetre, text="Reads building", padx=250, pady=50)
label2.pack(fill="both",expand="yes")
Label(label2,text="Select the length reads that you want : ").pack()
tReads = Spinbox(label2,from_=8,to=15)
tReads.pack()
Label(label2,text="Select the delta variation : ").pack()
deltaReads = Spinbox(label2,from_=1,to=3)
deltaReads.pack()
Label(label2,text="Select the maximum overlap : ").pack()
tOverlap = Spinbox(label2,from_=1,to=4)
tOverlap.pack()
Label(label2,text="Select the depth").pack()
depth = Spinbox(label2,from_=1,to=10)
depth.pack()

Button(label2, text="Change value", command=buttomAction).pack()

label3=LabelFrame(fenetre, text="Output results", padx=20,pady=20)
label3.pack(fill="both",expand="yes")
Label(label3,text="Reads :").pack()

scroll = Scrollbar(label3,orient=VERTICAL)
text = Text(label3)
scroll.pack(side=RIGHT,fill=Y)
text.pack(side=TOP,fill=BOTH,expand=TRUE)
scroll.config(command=text.yview)
text.config(yscrollcommand=scroll.set)
text.insert(END,"Select DNA seq to calculate the reads.")

fenetre.mainloop()
