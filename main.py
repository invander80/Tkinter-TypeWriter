from tkinter import Tk, Button, Frame, Label, Entry



class MainWindow(Tk):
    def __init__(self, parent=None):
        super().__init__()

        self.parent = parent

#=> UI LADEN
        self.setupUI()

#=> TOOLBAR BINDEN
        self.toolBar.bind("<B1-Motion>", self.dragWin)
        self.toolBar.bind("<Button-1>", self.clickWin)

#=> FUNKTIONEN FÜR DIE BUTTON:
        self.exitBtn["command"] = self.destroy
        self.typeButton["command"] = self.changeText

#=> WERTE FÜR DIE BIND FUNKTIONEN:
        self.offsetX = 0
        self.offsetY = 0

###===>>> UI FESTLEGEN
    def setupUI(self):
        self.toolBar = Frame(self)
        self.toolBar.pack(fill="x")

        self.exitBtn = Button(self.toolBar, text="\u26cc", bd=0)
        self.exitBtn.pack(side="right", ipadx=15)

        self.typeButton = Button(self, text="Text ändern", font=("Eraser", 30), fg="#e0f9ff", bg="#1a1e1f", bd=0)
        self.typeButton.pack(side="bottom", pady=30)

        self.textEntry = Entry(self, font=("Eraser", 30))
        self.textEntry.pack(side="bottom", ipadx=30)
        self.textEntry.insert(0, "Text Eingabe")

        self.textLabel = Label(self, font=("Earwig Factory", 130), bg="#1a1e1f", fg="#e0f9ff")
        self.textLabel.pack()

        self.infoLabel = Label(self, text="Der Text muss mindestens drei Chars enthalten!", bg="black", fg="white",
                               font=("Eraser", 30))
        self.infoLabel.place(x=0, y=0, relwidth=0, relheight=1)


###===>>> FUNTKION ZUM BEWEGEN DER APP (ÜBER DIE TOOLBAR)
    def dragWin(self, event):
        x = event.x_root - self.offsetX
        y = event.y_root - self.offsetY
        self.geometry("+%d+%d" % (x,y))

    def clickWin(self, event):
        self.offsetX = event.widget.winfo_rootx() - self.winfo_rootx() + event.x
        self.offsetY = event.widget.winfo_rooty() - self.winfo_rooty() + event.y

###===>>> TEXT EINZELND AUSGEBEN LASSEN
    def typeWiter(self, text, counter=0):
        if counter <= len(text):
            self.textLabel.config(text=text[:counter])
            self.after(100, lambda : self.typeWiter(text, counter +1))
        if len(self.textEntry.get()) < 3:
            self.textLabel.config(text="")
        return text

###===>>> TEXT ÄNDERN
    def changeText(self):
        if len(self.textEntry.get()) < 10:
            if self.showInfo(0.0):
                self.textEntry.delete(0, "end")
                self.typeWiter(self.textEntry.get())
        else:
            self.textEntry.delete(0, "end")
            self.textEntry.insert(0, "Text zu lang")

###===>>> INFO LABEL // WENN DIE LÄNGE DES TEXTES KLEINER ALS 3 CHARS BETRÄGT
    def showInfo(self, relwidth=0.0):
        if len(self.typeWiter(self.textEntry.get())) < 3:
            if relwidth <= 1.05:
                self.infoLabel.place_configure(relwidth=relwidth)
                self.after(10, lambda : self.showInfo(relwidth + 0.05))
            else:
                self.after(2000)
                if relwidth > 0.0:
                    self.textEntry.delete(0, "end")
                    self.infoLabel.place_configure(relwidth=0)


if __name__ == '__main__':
    mw = MainWindow()
    mw.overrideredirect(1)
    x, y = mw.winfo_screenwidth() / 2, mw.winfo_screenheight() / 2.75
    posx, posy = mw.winfo_screenwidth() / 4, mw.winfo_screenheight() / 3
    mw.geometry("%dx%d+%d+%d" % (x,y, posx, posy))
    mw.config(bg="#1a1e1f")
    mw.mainloop()
