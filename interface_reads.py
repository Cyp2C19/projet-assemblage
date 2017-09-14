from tkinter.filedialog import *
from DNA_manage import *
from assembly import *

fenetre = Tk()
fenetre.wm_state(newstate="zoomed")

reads = []

def select_file():
    filepath = askopenfilename(title="Select DNA sequence", filetypes=[('csv files','.csv')])
    fichier = open(filepath, "r")
    global reads
    for i in fichier:
        for j in i.split("\t"):
            reads.append(j)
    print(reads)
    fichier.close()
    displaySelectedReads()

def displaySelectedReads():
    global reads
    txt.delete('1.0', END)
    txt.insert(END, reads)
    txt.pack()
    displayButton.config(state=NORMAL)

def goResult():
    global reads
    seqFinal,res = main(reads,int(tOverlap.get()))
    text.delete('1.0', END)
    text.insert(END, res)
    text.pack()


####################### INTERFACE ##############################

################### PART 1 #######################
label1=LabelFrame(fenetre, text="Input Reads", padx=20,pady=14)
label1.pack(fill="both",expand="yes")

p0 = PanedWindow(label1, orient=HORIZONTAL)
p0.pack(side=TOP, expand=Y, fill=BOTH, pady=2, padx=250)
ssp01 = PanedWindow(p0, orient=VERTICAL)
ssp01.pack(side=LEFT, expand=Y, fill=BOTH, pady=2, padx=10)

ssp01.add(Label(label1, text="Select your reads in csv format", font = "Helvetica 8 bold",pady=30, padx=10))
ssp01.add(Button(label1, text="Choose file", command=select_file))
p0.add(ssp01)


Label(label1, text="Your selected reads : ", pady=10, padx=2).pack()
scr = Scrollbar(label1, orient=VERTICAL)
txt = Text(label1, height=4, width=50)
scr.pack(side=RIGHT, fill=Y)
txt.pack(side=TOP, fill=BOTH, expand=TRUE)
scr.config(command=txt.yview)
txt.config(yscrollcommand=scr.set)

Label(label1,text="Select the maximum overlap : ").pack()
tOverlap = Spinbox(label1,from_=1,to=4)
tOverlap.pack()

displayButton = Button(label1, text="Display results", command=goResult)
displayButton.pack(side = BOTTOM)
displayButton.config(state=DISABLED)


################### PART 3 #######################
label3=LabelFrame(fenetre, text="Output results", padx=20,pady=20)
label3.pack(fill="both",expand="yes")
Label(label3,text="Results :").pack()

scroll = Scrollbar(label3,orient=VERTICAL)
text = Text(label3)
scroll.pack(side=RIGHT,fill=Y)
text.pack(side=TOP,fill=BOTH,expand=TRUE)
scroll.config(command=text.yview)
text.config(yscrollcommand=scroll.set)
text.insert(END,"Select list of reads")




fenetre.mainloop()
