from tkinter.filedialog import *
from DNA_manage import *
#from Interface_result import *




fenetre = Tk()
fenetre.wm_state(newstate="zoomed")


DNA_seq = ""
reads = []

def select_file():
    filepath = askopenfilename(title="Select DNA sequence", filetypes=[('text files','.txt')])
    fichier = open(filepath, "r")
    global DNA_seq
    DNA_seq = fichier.read()
    fichier.close()
    displayDNASeq()
    calculateReads()

def generateDNASeq():
    global DNA_seq
    DNA_seq = createRandomDNASeq(int(length.get()))
    displayDNASeq()
    calculateReads()

def calculateReads():
    global reads
    reads = createReads(DNA_seq, int(tReads.get()), int(deltaReads.get()), int(tOverlap.get()), int(depth.get()), int(checkboxVal.get()))
    displayReads(reads)

def displayReads(reads):
    global text
    val = ""
    for i in range(0, len(reads)):
        val += reads[i] + " "
    text.delete('1.0', END)
    text.insert(END, val)
    text.pack()
    dlButton.config(state=NORMAL)
    #displayButton.config(state=NORMAL)

def displayDNASeq():
    global txt
    txt.delete('1.0', END)
    txt.insert(END, DNA_seq)
    txt.pack()

def select_output_path():
    filepath = asksaveasfilename(title="Select DNA sequence", filetypes=[('csv files', '.csv')])
    if filepath[-4:] != '.csv':
        filepath += '.csv'
    return(filepath)

def dlResults():
    path=select_output_path()
    outputfile = open(path,'w')
    for i in range(0,len(reads)):
        if i%10==0 and i!=0:
            outputfile.write("\n")
        outputfile.write(reads[i])
        outputfile.write("\t")
    outputfile.close()




####################### INTERFACE ##############################

################### PART 1 #######################
label1=LabelFrame(fenetre, text="Input DNA sequence", padx=20,pady=14)
label1.pack(fill="both",expand="yes")

p0 = PanedWindow(label1, orient=HORIZONTAL)
p0.pack(side=TOP, expand=Y, fill=BOTH, pady=2, padx=250)
ssp01 = PanedWindow(p0, orient=VERTICAL)
ssp01.pack(side=LEFT, expand=Y, fill=BOTH, pady=2, padx=10)

ssp01.add(Label(label1, text="Select your DNA sequence in txt format", font = "Helvetica 8 bold",pady=30, padx=10))
ssp01.add(Button(label1, text="Choose file", command=select_file))

ssp02 = PanedWindow(p0, orient=VERTICAL)
ssp02.pack(side=LEFT, expand=Y, fill=BOTH, pady=2, padx=2)
ssp02.add(Label(label1, text="OR", pady=2, padx=140))

ssp03 = PanedWindow(p0, orient=VERTICAL)
ssp03.pack(side=LEFT, expand=Y, fill=BOTH, pady=2, padx=10)

ssp03.add(Label(label1, text="Generate a random DNA sequence", font = "Helvetica 8 bold"))
ssp03.add(Label(label1,text="Select the length", pady=7, padx=2))
length = Spinbox(label1,from_=200,to=50000, increment = 50)
ssp03.add(length)
ssp03.add(Button(label1, text="Generate", command=generateDNASeq))
p0.add(ssp01)
p0.add(ssp02)
p0.add(ssp03)

Label(label1, text="Your selected DNA sequence : ", pady=10, padx=2).pack()
scr = Scrollbar(label1, orient=VERTICAL)
txt = Text(label1, height=4, width=50)
scr.pack(side=RIGHT, fill=Y)
txt.pack(side=TOP, fill=BOTH, expand=TRUE)
scr.config(command=txt.yview)
txt.config(yscrollcommand=scr.set)

################### PART 2 #######################
label2=LabelFrame(fenetre, text="Reads building", padx=300, pady=10)
label2.pack(fill="both",expand="yes")

p = PanedWindow(label2, orient=HORIZONTAL)
p.pack(side=TOP, expand=Y, fill=BOTH, pady=2, padx=2)

ssp1 = PanedWindow(p, orient=VERTICAL)
ssp1.pack(side=LEFT, expand=Y, fill=BOTH, pady=2, padx=10)
ssp1.add(Label(label2,text="Select the length reads :    "))
tReads = Spinbox(label2,from_=8,to=15)
ssp1.add(tReads)

ssp2 = PanedWindow(p, orient=VERTICAL)
ssp2.pack(side=LEFT, expand=Y, fill=BOTH, pady=2, padx=10)
ssp2.add(Label(label2,text="Select the delta variation :   "))
deltaReads = Spinbox(label2,from_=1,to=3)
ssp2.add(deltaReads)

ssp3 = PanedWindow(p, orient=VERTICAL)
ssp3.pack(side=LEFT, expand=Y, fill=BOTH, pady=2, padx=10)
ssp3.add(Label(label2,text="Select the maximum overlap : "))
tOverlap = Spinbox(label2,from_=1,to=4)
ssp3.add(tOverlap)

ssp4 = PanedWindow(p, orient=VERTICAL)
ssp4.pack(side=LEFT, expand=Y, fill=BOTH, pady=2, padx=10)
ssp4.add(Label(label2,text="Select the depth : "))
depth = Spinbox(label2,from_=1,to=10)
ssp4.add(depth)

ssp5 = PanedWindow(p, orient=VERTICAL)
ssp5.pack(side=LEFT, expand=Y, fill=BOTH, pady=2, padx=10)
ssp5.add(Label(label2,text="Randomize the reads : "))
checkboxVal = IntVar()
checkbox = Checkbutton(fenetre, text="Randomize?",variable=checkboxVal)
print(checkboxVal.get())
ssp5.add(checkbox)

p.add(ssp1)
p.add(ssp2)
p.add(ssp3)
p.add(ssp4)
p.add(ssp5)

Button(label2, text="Build", command=calculateReads).pack()

################### PART 3 #######################
label3=LabelFrame(fenetre, text="Output results", padx=20,pady=20)
label3.pack(fill="both",expand="yes")
Label(label3,text="Reads :").pack()
p3 = PanedWindow(label3, orient=HORIZONTAL)
p3.pack(side=BOTTOM, expand=Y, fill=BOTH, pady=2, padx=550)
dlButton = Button(label3, text="Download results", command=dlResults)
dlButton.pack(side = BOTTOM)
dlButton.config(state=DISABLED)
p3.add(dlButton)
# displayButton = Button(p3, text="Display results", command=goResult)
# displayButton.pack(side = BOTTOM)
# displayButton.config(state=DISABLED)
# p3.add(displayButton)


scroll = Scrollbar(label3,orient=VERTICAL)
text = Text(label3)
scroll.pack(side=RIGHT,fill=Y)
text.pack(side=TOP,fill=BOTH,expand=TRUE)
scroll.config(command=text.yview)
text.config(yscrollcommand=scroll.set)
text.insert(END,"Select DNA seq to calculate the reads.")



Button(fenetre, text="Build", command=calculateReads).pack()



fenetre.mainloop()
