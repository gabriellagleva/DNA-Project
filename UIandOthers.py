
import tkinter as tk
from tkinter import ttk
import codon
class MyGUI:
    def __init__(self):
        #master of UI + notebook
        root=tk.Tk()
        root.geometry("800x800")
        notebook = ttk.Notebook(root)
        tab0 = ttk.Frame(notebook)
        tab1 = ttk.Frame(notebook)
        tab2 = ttk.Frame(notebook)
        tab3 = ttk.Frame(notebook)
        #Starting tab
        notebook.add(tab0, text = "Start")
        lblResults =tk.Label(tab0, text = "Hello, my name is Gabriel Lagleva. I wrote this as a bit of a project to do over Wofford College's Interium. I'll admit, its not the best. Honestly the first time I have sat down and really tried to make something like this, so its definatly rough around the edges. However, I have committed to making it better over the next few months. \n I'm not sure why you would want to, but if you want to talk to me about this project, you can do so at gabelagleva@gmail.com. The entire software is MIT liscenced, so you're free to use it however you want (assuming you follow the rules), so you don't need to ask me for permission or anything. ", wraplength= 500)
        lblResults.pack()

        #tab1
        notebook.add(tab1, text = 'Nucleotide Comparison')

        ttlFrame = ttk.Frame(tab1)
        label = tk.Label(ttlFrame, text="Nucleotide Comparison", font=('Arial', 18))
        ttlFrame.pack()
        label.pack()
        #Grid setup and info filling
        bdyFrame = ttk.Frame(tab1)
        bdyFrame.pack()
        self.strvarDNA1 = tk.StringVar(bdyFrame, "")
        self.strvarDNA2 = tk.StringVar(bdyFrame, "")
        lblDNA1 = tk.Label(bdyFrame, text="Nucleotide Sequence 1: 5'-")
        lblDNA2 = tk.Label(bdyFrame, text="Nucleotide Sequence 2: 5'-")
        lbl3Prime = tk.Label(bdyFrame, text="-3'")
        lbl3Prime2 = tk.Label(bdyFrame, text="-3'")
        etyDNA1 = tk.Entry(bdyFrame, textvariable=self.strvarDNA1)
        etyDNA2 = tk.Entry(bdyFrame, textvariable=self.strvarDNA2)

        #Putting stuff into grid
        lblDNA1.grid(row=0, column=0)
        lblDNA2.grid(row=1, column=0)
        etyDNA1.grid(row=0, column=1)
        etyDNA2.grid(row=1,column=1)
        lbl3Prime.grid(row=0,column=2)
        lbl3Prime2.grid(row=1,column=2)

        #button Frame
        btnFrame = ttk.Frame(tab1)
        btnFrame.pack()

        #Button Creation
        btnCompare = tk.Button(btnFrame, text="Comparison", command=self.bntCompareFct)
        btnCompare.pack()
        #Empty frame for results

        self.resultsFrame = ttk.Frame(tab1)
        self.resultsFrame.pack()

        #tab 2 - automatic translator setup
        notebook.add(tab2, text = "Translation")
        lbltranslation = tk.Label(tab2, text="Translation")
        lbltranslation.pack()
        translationFrame = ttk.Frame(tab2)
        self.strvarTranslation = tk.StringVar(translationFrame)
        lblTranslation1 = tk.Label(translationFrame, text="RNA Sequence 5'-")
        lbltranslation2 = tk.Label(translationFrame, text="-3'")
        etyTranslation = tk.Entry(translationFrame, textvariable=self.strvarTranslation)

        #Label and Entry Packing

        lblTranslation1.grid(row=0, column=0)
        etyTranslation.grid(row=0, column=1)
        lbltranslation2.grid(row=0, column=2)
        translationFrame.pack()

        btnframeTranslation = ttk.Frame(tab2)
        btnframeTranslation.pack()

        #Translation Button creation

        btnTranslation = tk.Button(btnframeTranslation, text="Translation", command=self.bntcmdTranslation)
        btnTranslation.pack()

        #Translation Results Frame

        self.rstframeTranslation = ttk.Frame(tab2)
        self.rstframeTranslation.pack()

        notebook.pack()
        root.mainloop()
    def bntCompareFct(self):
        try:
            for widgets in self.resultsFrame.winfo_children():
                widgets.destroy()
                del widgets
        except:
            pass
        lowerStrVarDNA1 = self.strvarDNA1.get().lower()
        lowerStrVarDNA2 = self.strvarDNA2.get().lower()
        if self.illegal_letters(lowerStrVarDNA1):
            lblResults = tk.Label(self.resultsFrame, text="Sequence 1 contains illegal letters/characters")
            lblResults.pack()
            return
        if self.illegal_letters(lowerStrVarDNA2):
            lblResults = tk.Label(self.resultsFrame, text="Sequence 2 contains illegal letters/characters")
            lblResults.pack()
            return

        results = self.comparison(lowerStrVarDNA1, lowerStrVarDNA2)

        if results[0]:
            if len(lowerStrVarDNA1) == len(lowerStrVarDNA2):
                self.resultPacker(self.resultsFrame,"The results are exactly the same =)")
            elif len(lowerStrVarDNA1) > len(lowerStrVarDNA2):
                self.resultPacker(self.resultsFrame,"Sequence 1 is longer than Sequence 2, so a true comparison is impossible. However, cutting Sequence 1 so it is the same size as Sequence 2 shows that they are the same")
            else:
                self.resultPacker(self.resultsFrame,"Sequence 2 is longer than Sequence 1, so a true comparison is impossible. However, cutting Sequence 2 so it is the same size as Sequence 1 shows that they are the same")
        else:
            strResults = ""
            for keys in results[1]:
                strResults = strResults + str(keys) + results[1][keys][0]+ "->" + results[1][keys][1] + "\n"
            txtResults =tk.Text(self.resultsFrame)
            txtResults.insert(0.0, strResults)
            txtResults.pack()
               
    def illegal_letters(self, nucleotideSequence):
        badletters = ['b', 'd', 'e', 'f', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 'u', 'v', 'w', 'x', 'y', 'z']
        for letter in nucleotideSequence:
            if letter in badletters:
                return True
        return False
    
    def comparison(self, nucleotideSequence1, nucleotideSequence2):
        if nucleotideSequence1 == nucleotideSequence2:
            return [True, []]
        else:
            dctDifferences = {}
            flgDifferences = True
            numofAA=min(len(nucleotideSequence1), len(nucleotideSequence2))
            for i in range(numofAA):
                if nucleotideSequence1[i] != nucleotideSequence2[i]:
                    flgDifferences=False
                    dctDifferences[i+1] = [nucleotideSequence1[i], nucleotideSequence2[i]]
            return [flgDifferences, dctDifferences]
                        
    def resultPacker(self, master, text):
        lblResults = tk.Label(master, text=text)
        lblResults.pack()
    
    def bntcmdTranslation(self):
        try:
            for widgets in self.rstframeTranslation.winfo_children():
                widgets.destroy()
                del widgets
        except:
            pass
        RNAsequence = self.strvarTranslation.get().lower()
        returningString = "5'-"
        first = 0
        third = 3
        for x in range(len(RNAsequence)//3):
            returningString = returningString + codon.codonCompare(RNAsequence[first:third]) + '-'
            first +=3
            third +=3
        returningString = returningString + "'3"
        txtResults =tk.Text(self.rstframeTranslation)
        txtResults.insert(0.0, returningString)
        txtResults.pack()


            

MyGUI()