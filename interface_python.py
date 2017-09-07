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
    displayDNASeq()
    displayReads()

def generateDNASeq():
    global DNA_seq
    DNA_seq = createRandomDNASeq(int(length.get()))
    displayDNASeq()
    displayReads()

def displayReads():
    reads = createReads(DNA_seq,int(tReads.get()),int(deltaReads.get()),int(tOverlap.get()),int(depth.get()))
    global text
    val = ""
    for i in range(0, len(reads)):
        val += reads[i] + " "
    text.delete('1.0', END)
    text.insert(END, val)
    text.pack()

def displayDNASeq():
    global txt
    txt.delete('1.0', END)
    txt.insert(END, DNA_seq)
    txt.pack()

label1=LabelFrame(fenetre, text="Input DNA sequence", padx=20,pady=14)
label1.pack(fill="both",expand="yes")
Label(label1, text="Select your DNA sequence in txt format", font = "Helvetica 8 bold").pack()
Button(label1, text="Choose file", command=select_file).pack()

Label(label1, text="OR").pack()
Label(label1, text="Generate a random DNA sequence", font = "Helvetica 8 bold").pack()
Label(label1,text="Select the length").pack()
length = Spinbox(label1,from_=1,to=10)
length.pack()
Button(label1, text="Generate", command=generateDNASeq).pack()

Label(label1, text="Your selected DNA sequence : ").pack()
scr = Scrollbar(label1, orient=VERTICAL)
txt = Text(label1, height=4, width=50)
scr.pack(side=RIGHT, fill=Y)
txt.pack(side=TOP, fill=BOTH, expand=TRUE)
scr.config(command=txt.yview)
txt.config(yscrollcommand=scr.set)

label2=LabelFrame(fenetre, text="Reads building", padx=250, pady=20)
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

Button(label2, text="Build", command=displayReads).pack()

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