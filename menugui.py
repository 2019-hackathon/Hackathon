import tkinter 
import os     
from tkinter import *
from tkinter.ttk import *
import webbrowser
from tkinter.messagebox import *
from tkinter.filedialog import *


class Notepad: 
    __root = Tk()
    koot = Tk()
    __root.title("The Meal Deal")
    text = Label(__root, text="What type of receipe would you like? ", font=("Comic Sans",15))
    text.grid(column=0,row=0)

    def beef():
        new = 1
        koot = Tk()
    def breakfast():
        new = 1
        url = "https://www.google.com"
        webbrowser.open(url, new=new)
    def chicken():
        new = 1
        url = "https://www.google.com"
        webbrowser.open(url, new=new)
    def desert():
        new = 1
        url = "https://www.google.com"
        webbrowser.open(url, new=new)
    def goat():
        new = 1
        url = "https://www.google.com"
        webbrowser.open(url, new=new)
    def lamb():
        new = 1
        url = "https://www.google.com"
        webbrowser.open(url, new=new)
    def miscellaneous():
        new = 1
        url = "https://www.google.com"
        webbrowser.open(url, new=new)
    def pasta():
        new = 1
        url = "https://www.google.com"
        webbrowser.open(url, new=new)
    def pork():
        new = 1
        url = "https://www.google.com"
        webbrowser.open(url, new=new)
    def seafood():
        new = 1
        url = "https://www.google.com"
        webbrowser.open(url, new=new)
    def side():
        new = 1
        url = "https://www.google.com"
        webbrowser.open(url, new=new)
    def starter():
        new = 1
        url = "https://www.google.com"
        webbrowser.open(url, new=new)
    def vegan():
        new = 1
        url = "https://www.google.com"
        webbrowser.open(url, new=new)
    def vegetarian():
        new = 1
        url = "https://www.google.com"
        webbrowser.open(url, new=new)

    # default window width and height 
    __thisWidth = 300
    __thisHeight = 300
    __thisTextArea = Text(__root) 
    __thisMenuBar = Menu(__root) 
    __thisFileMenu = Menu(__thisMenuBar, tearoff=0) 
    __thisEditMenu = Menu(__thisMenuBar, tearoff=0) 
    __thisHelpMenu = Menu(__thisMenuBar, tearoff=0)

    thisTextArea = Text(koot)
    thisMenuBar = Menu(koot)
    thisFileMenu = Menu(thisMenuBar, tearoff=0) 
    thisEditMenu = Menu(thisMenuBar, tearoff=0) 
    thisHelpMenu = Menu(thisMenuBar, tearoff=0)
    
    # To add scrollbar 
    __thisScrollBar = Scrollbar(__thisTextArea)
    thisScrollBar = Scrollbar(thisTextArea)
    __file = None

    check = IntVar()
    c = Checkbutton(koot, text='Choice', var=check)
    c.place(x=45, y=200)

    btn = Button(__root, text = "Quit", bd = "5", command = __root.destroy)
    btn.place(x=0,y=0)

    goot = Button(koot, text = "Quit", bd = "5", command = koot.destroy)
    goot.place(x=0,y=0)

    beef = Button(__root, text = "Beef", bd = "5", command=beef)
    beef.place(x=50,y=50)
    
    breakfast = Button(__root, text = "Breakfast", bd = "5", command=breakfast)
    breakfast.place(x=100,y=50)

    chicken = Button(__root, text = "Chicken", bd = "5", command=chicken)
    chicken.place(x=175,y=50)
    
    desert = Button(__root, text = "Desert", bd = "5",command=desert)
    desert.place(x=250,y=50)
    
    goat = Button(__root, text = "Goat", bd = "5",command=goat)
    goat.place(x=315,y=50)
    
    lamb = Button(__root, text = "Lamb", bd = "5",command=lamb)
    lamb.place(x=370,y=50)
    
    miscellaneous = Button(__root, text = "Miscellneous", bd = "5",command=miscellaneous)
    miscellaneous.place(x=425,y=50)
    
    pasta = Button(__root, text = "Pasta", bd = "5",command=pasta)
    pasta.place(x=520,y=50)
    
    pork = Button(__root, text = "Pork", bd = "5",command=pork)
    pork.place(x=50,y=100)
    
    seafood = Button(__root, text = "Seafood", bd = "5",command=seafood)
    seafood.place(x=100,y=100)
    
    side = Button(__root, text = "Side", bd = "5",command=side)
    side.place(x=175,y=100)
    
    starter = Button(__root, text = "Starter", bd = "5",command=starter)
    starter.place(x=250,y=100)
    
    vegan = Button(__root, text = "Vegan", bd = "5",command=vegan)
    vegan.place(x=315,y=100)
    
    vegetarian = Button(__root, text = "Vegetarian", bd = "5",command=vegetarian)
    vegetarian.place(x=370,y=100)

    def __init__(self,**kwargs): 
  
        # Set icon 
        try: 
                self.__root.wm_iconbitmap("Notepad.ico")
                self.koot.wm_iconbitmap("Notepad.ico")
        except: 
                pass
  
        # Set window size (the default is 300x300) 
  
        try: 
            self.__thisWidth = kwargs['width'] 
        except KeyError: 
            pass
  
        try: 
            self.__thisHeight = kwargs['height'] 
        except KeyError: 
            pass
            
        # Set the window text 
        self.__root.title("Untitled - Notepad")
        self.koot.title("Untitled - Notepad")
  
        # Center the window 
        screenWidth = self.__root.winfo_screenwidth() 
        screenHeight = self.__root.winfo_screenheight()
        AscreenWidth = self.koot.winfo_screenwidth() 
        AscreenHeight = self.koot.winfo_screenheight()
      
        # For left-alling 
        left = (screenWidth / 2) - (self.__thisWidth / 2)
        Aleft = (AscreenWidth / 2) - (self.__thisWidth / 2)
          
        # For right-allign 
        top = (screenHeight / 2) - (self.__thisHeight /2)
        Atop = (AscreenHeight / 2) - (self.__thisHeight /2)
          
        # For top and bottom 
        self.__root.geometry('%dx%d+%d+%d' % (self.__thisWidth, 
                                              self.__thisHeight, 
                                              left, top))
        self.koot.geometry('%dx%d+%d+%d' % (self.__thisWidth, 
                                              self.__thisHeight, 
                                              Aleft, Atop))
  
        # To make the textarea auto resizable 
        self.__root.grid_rowconfigure(0, weight=1) 
        self.__root.grid_columnconfigure(0, weight=1)
        self.koot.grid_rowconfigure(0, weight=1) 
        self.koot.grid_columnconfigure(0, weight=1)
  
        # Add controls (widget) 
        self.__thisTextArea.grid(sticky = N + E + S + W)
        self.thisTextArea.grid(sticky = N + E + S + W)
          
        # To open new file 
        self.__thisFileMenu.add_command(label="New", 
                                        command=self.__newFile)
        self.thisFileMenu.add_command(label="New", 
                                        command=self.__newFile)
          
        # To open a already existing file 
        self.__thisFileMenu.add_command(label="Open", 
                                        command=self.__openFile)
        self.thisFileMenu.add_command(label="Open", 
                                        command=self.__openFile)
          
        # To save current file 
        self.__thisFileMenu.add_command(label="Save", 
                                        command=self.__saveFile)
        self.thisFileMenu.add_command(label="Save", 
                                        command=self.__saveFile)
  
        # To create a line in the dialog         
        self.__thisFileMenu.add_separator()                                          
        self.__thisFileMenu.add_command(label="Exit", 
                                        command=self.__quitApplication) 
        self.__thisMenuBar.add_cascade(label="File", 
                                       menu=self.__thisFileMenu)
        self.thisFileMenu.add_separator()                                          
        self.thisFileMenu.add_command(label="Exit", 
                                        command=self.__quitApplication) 
        self.thisMenuBar.add_cascade(label="File", 
                                       menu=self.thisFileMenu)
          
        # To give a feature of cut  
        self.__thisEditMenu.add_command(label="Cut", 
                                        command=self.__cut)
        self.thisEditMenu.add_command(label="Cut", 
                                        command=self.__cut)
      
        # to give a feature of copy     
        self.__thisEditMenu.add_command(label="Copy", 
                                        command=self.__copy)
        self.thisEditMenu.add_command(label="Copy", 
                                        command=self.__copy)
          
        # To give a feature of paste 
        self.__thisEditMenu.add_command(label="Paste", 
                                        command=self.__paste)
        self.thisEditMenu.add_command(label="Paste", 
                                        command=self.__paste)
          
        # To give a feature of editing 
        self.__thisMenuBar.add_cascade(label="Edit", 
                                       menu=self.__thisEditMenu)
        self.thisMenuBar.add_cascade(label="Edit", 
                                       menu=self.thisEditMenu)
          
        # To create a feature of description of the notepad 
        self.__thisHelpMenu.add_command(label="About Notepad", 
                                        command=self.__showAbout)  
        self.__thisMenuBar.add_cascade(label="Help", 
                                       menu=self.__thisHelpMenu) 
  
        self.__root.config(menu=self.__thisMenuBar) 
  
        self.__thisScrollBar.pack(side=RIGHT,fill=Y)

        self.thisHelpMenu.add_command(label="About Notepad", 
                                        command=self.__showAbout)  
        self.thisMenuBar.add_cascade(label="Help", 
                                       menu=self.thisHelpMenu) 
  
        self.koot.config(menu=self.thisMenuBar) 
  
        self.thisScrollBar.pack(side=RIGHT,fill=Y)
          
        # Scrollbar will adjust automatically according to the content         
        self.__thisScrollBar.config(command=self.__thisTextArea.yview)      
        self.__thisTextArea.config(yscrollcommand=self.__thisScrollBar.set)

        self.thisScrollBar.config(command=self.thisTextArea.yview)      
        self.thisTextArea.config(yscrollcommand=self.thisScrollBar.set)
      
          
    def __quitApplication(self): 
        self.__root.destroy()
        self.koot.destroy()
        # exit() 
  
    def __showAbout(self): 
        showinfo("Notepad","Mrinal Verma") 
  
    def __openFile(self): 
          
        self.__file = askopenfilename(defaultextension=".txt", 
                                      filetypes=[("All Files","*.*"), 
                                        ("Text Documents","*.txt")]) 
  
        if self.__file == "": 
              
            # no file to open 
            self.__file = None
        else: 
              
            # Try to open the file 
            # set the window title 
            self.__root.title(os.path.basename(self.__file) + " - Notepad") 
            self.__thisTextArea.delete(1.0,END) 
  
            file = open(self.__file,"r") 
  
            self.__thisTextArea.insert(1.0,file.read()) 
  
            file.close() 
  
          
    def __newFile(self): 
        self.__root.title("Untitled - Notepad") 
        self.__file = None
        self.__thisTextArea.delete(1.0,END)

    def __saveFile(self): 
  
        if self.__file == None: 
            # Save as new file 
            self.__file = asksaveasfilename(initialfile='Untitled.txt', 
                                            defaultextension=".txt", 
                                            filetypes=[("All Files","*.*"), 
                                                ("Text Documents","*.txt")]) 
  
            if self.__file == "": 
                self.__file = None
            else: 
                  
                # Try to save the file 
                file = open(self.__file,"w") 
                file.write(self.__thisTextArea.get(1.0,END)) 
                file.close() 
                  
                # Change the window title 
                self.__root.title(os.path.basename(self.__file) + " - Notepad") 
                  
              
        else: 
            file = open(self.__file,"w") 
            file.write(self.__thisTextArea.get(1.0,END)) 
            file.close() 
  
    def __cut(self): 
        self.__thisTextArea.event_generate("<<Cut>>")
        self.thisTextArea.event_generate("<<Cut>>")
  
    def __copy(self): 
        self.__thisTextArea.event_generate("<<Copy>>")
        self.thisTextArea.event_generate("<<Copy>>")
  
    def __paste(self): 
        self.__thisTextArea.event_generate("<<Paste>>")
        self.thisTextArea.event_generate("<<Paste>>")
  
    def run(self): 
  
        # Run main application 
        self.__root.mainloop()
        self.koot.mainloop()
  
  
# Run main application 
notepad = Notepad(width=600,height=400) 
notepad.run()
