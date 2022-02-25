import tkinter
from tkinter import ttk
from tkinter import filedialog
from tkinter.filedialog import askopenfile
import abc
from ImageInsideImage import *
from PIL import Image, ImageTk
from Menu import EncryptImage,DecryptImage,HideImage,RevealImage
import tkinter.font as font

class Window(ttk.Frame):
    __metaclass__ = abc.ABCMeta
    def __init__(self, parent):
        ''' Constructor '''
        ttk.Frame.__init__(self, parent)
        self.parent = parent
        self.parent.resizable(width=False, height=False) 
        self.validate_notempty = (self.register(self.notEmpty), '%P') 
        self.init_gui()

    @abc.abstractmethod 
    def init_gui(self):
        pass

    @abc.abstractmethod
    def do_something(self):
        pass

    def notEmpty(self, P):
        if P.strip():
            valid = True
        else:
            print("Error: Field must not be empty.") 
            valid = False
        return valid

    def close_win(self):
        self.parent.destroy()

class SomethingWindow(Window):
    filename1 = ""
    filename2 = ""
    def upload_image1(self):
        global img
        f_types = [('Jpg Files', '*.jpg')]
        self.filename1 = filedialog.askopenfilename(filetypes=f_types)
        img=Image.open(self.filename1)
        img_resized=img.resize((500,500)) 
        img=ImageTk.PhotoImage(img_resized)
        b1=ttk.Button(self.parent,image=img) 
        b1.grid(row=0,column=0,columnspan=1,rowspan=5)

    def upload_image2(self):
        global img2
        f_types = [('Jpg Files', '*.jpg')]
        self.filename2 = filedialog.askopenfilename(filetypes=f_types)
        img2=Image.open(self.filename2)
        img_resized2=img2.resize((500,500)) 
        img2=ImageTk.PhotoImage(img_resized2)
        b2 =ttk.Button(self.parent,image=img2) 
        b2.grid(row=0,column=2,columnspan=1,rowspan=5)

    def init_gui(self):
        self.parent.title("Hide Image Inside Image")
        self.parent.columnconfigure(3, weight=1)
        self.parent.rowconfigure(6, weight=1)

        self.label_title = ttk.Label(self.parent, text="Hide Image")

        myFont = font.Font(family='Helvetica',size=17, weight='bold')
        self.label_title['font'] = myFont

        self.btn_do = ttk.Button(self.parent,text='Hide Image',width=20,command=self.do_something)
        self.btn_upload_1 = ttk.Button(self.parent,text='Upload Image 1',width=20,command=self.upload_image1)
        self.btn_upload_2 = ttk.Button(self.parent,text='Upload Image 2',width=20,command=self.upload_image2)
        self.btn_cancel = ttk.Button(self.parent, text='Cancel',width=20,command=self.close_win)

        self.label_title.grid(row=0, column=1, sticky='ew')

        self.btn_do.grid(row=4,column=1,columnspan=1, sticky='nsew')
        self.btn_upload_1.grid(row=1,column = 1,columnspan=1,sticky='nsew')
        self.btn_upload_2.grid(row=2,column = 1,columnspan=1,sticky='nsew')
        self.btn_cancel.grid(row=3, column=1, columnspan=1,sticky='nsew')

    def do_something(self):
        if self.filename1 and self.filename2:
            RevealImage  = HideImage(self.filename1,self.filename2)
            self.label_title = ttk.Label(self.parent, text="Output Image")
            self.label_title.grid(row=5,column=1,sticky='ew')
            myFont = font.Font(family='Helvetica',size=17, weight='bold')
            self.label_title['font'] = myFont
            global imge
            imge=Image.open(RevealImage)
            imge_resized=imge.resize((500,500)) 
            imge=ImageTk.PhotoImage(imge_resized)
            b=ttk.Button(self.parent,image=imge) 
            b.grid(row=6,column=1)
        else:
            print("Error: But for real though, field must not be empty.")

class SomethingWindow4(Window):
    filename1 = ""
    def upload_image1(self):
        global img
        f_types = [('PNG Files', '*.png')]
        self.filename1 = filedialog.askopenfilename(filetypes=f_types)
        img=Image.open(self.filename1)
        img_resized=img.resize((500,500)) 
        img=ImageTk.PhotoImage(img_resized)
        b1=ttk.Button(self.parent,image=img) 
        b1.grid(row=0,column=0,columnspan=1,rowspan=5)

    def init_gui(self):
        self.parent.title("Reveal Hidden Image Inside Image")
        self.parent.columnconfigure(2, weight=1)
        self.parent.rowconfigure(4, weight=1)

        self.label_title = ttk.Label(self.parent, text="Reveal Hidden Image")

        myFont = font.Font(family='Helvetica',size=17, weight='bold')
        self.label_title['font'] = myFont

        self.btn_do = ttk.Button(self.parent,text='Reveal Image',width=20,command=self.do_something)
        self.btn_upload_1 = ttk.Button(self.parent,text='Upload Image',width=20,command=self.upload_image1)
        self.btn_cancel = ttk.Button(self.parent, text='Cancel',width=20,command=self.close_win)

        self.label_title.grid(row=0, column=1, sticky='nsew')

        self.btn_do.grid(row=3,column=1,columnspan=1, sticky='nsew')
        self.btn_upload_1.grid(row=1,column = 1,columnspan=1,sticky='nsew')
        self.btn_cancel.grid(row=2, column=1, columnspan=1,sticky='nsew')


    def do_something(self):
        if self.filename1:
            HiddenImage = RevealImage(self.filename1)
            global imge
            imge=Image.open(HiddenImage)
            imge_resized=imge.resize((500,500)) 
            imge=ImageTk.PhotoImage(imge_resized)
            b2=ttk.Button(self.parent,image=imge) 
            b2.grid(row=0,column=2,columnspan=1,rowspan=5)

        else:
            print("Error: But for real though, field must not be empty.")


class SomethingWindow2(Window):
    filename = ""
    def upload_image(self):
        global img
        f_types = [('PNG Files', '*.png')]
        self.filename = filedialog.askopenfilename(filetypes=f_types)
        img=Image.open(self.filename)
        img_resized=img.resize((400,200)) 
        img=ImageTk.PhotoImage(img_resized)
        b2 =ttk.Button(self.parent,image=img) 
        b2.grid(row=0,column=3,columnspan=3,rowspan=5)
        myFont = font.Font(family='Helvetica',size=13, weight='bold')

        self.label_title.grid(row=0,column=1,columnspan=3,sticky='nsew')
        self.label_title['font'] = myFont


    def init_gui(self):
        self.parent.title("Encrypt Message Inside Image")
        self.parent.columnconfigure(5, weight=1)
        self.parent.rowconfigure(5, weight=1)

        self.label_title = ttk.Label(self.parent, text="Encryption")
        self.contentframe = ttk.Frame(self.parent, relief="sunken")

        self.label_test1 = ttk.Label(self.contentframe, text='Enter Message: ')
        self.input_test1 = ttk.Entry(self.contentframe, width=30, validate='focusout', validatecommand=(self.validate_notempty))

        self.label_test2 = ttk.Label(self.contentframe, text='Enter Key: ')
        self.input_test2 = ttk.Entry(self.contentframe, width=30, validate='focusout', validatecommand=(self.validate_notempty))

        self.label_test3 = ttk.Label(self.contentframe, text='Enter Vector: ')
        self.input_test3 = ttk.Entry(self.contentframe, width=30, validate='focusout', validatecommand=(self.validate_notempty))

        self.btn_image = ttk.Button(self.parent, text='Upload Image',command = lambda:self.upload_image())
        self.btn_do = ttk.Button(self.parent, text='Encrypt Image', command=self.do_something)
        self.btn_cancel = ttk.Button(self.parent, text='Cancel', command=self.close_win)

        self.label_title.grid(row=0, column=1, columnspan=3, sticky='nsew')
        self.contentframe.grid(row=1, column=0, columnspan=3, sticky='nsew')

        self.label_test1.grid(row=0, column=0)
        self.input_test1.grid(row=0, column=1,columnspan=3, sticky='w')

        self.label_test2.grid(row=1, column=0)
        self.input_test2.grid(row=1, column=1, columnspan=3,sticky='w')

        self.label_test3.grid(row=2, column=0)
        self.input_test3.grid(row=2, column=1, columnspan=3,sticky='w')

        self.btn_image.grid(row=3, column=0, sticky='e')
        self.btn_do.grid(row=3, column=1, sticky='e')
        self.btn_cancel.grid(row=3, column=2, sticky='e')

        myFont = font.Font(family='Helvetica',size=13, weight='bold')
        self.label_title['font'] = myFont

        for child in self.parent.winfo_children():
            child.grid_configure(padx=10, pady=5)
        for child in self.contentframe.winfo_children():
            child.grid_configure(padx=5, pady=2)

    def do_something(self):
        text = self.input_test1.get().strip()
        key = self.input_test2.get().strip()
        vector = self.input_test3.get().strip()

        if text and key and vector:
            EncryptImage(self.filename,text,key,vector)

        else:
            print("Error: But for real though, field must not be empty.")    

class SomethingWindow3(Window):
    filename = ""
    def upload_file(self):
        global img
        f_types = [('PNG Files', '*.png')]
        self.filename = filedialog.askopenfilename(filetypes=f_types)
        img=Image.open(self.filename)
        img_resized=img.resize((400,200)) 
        img=ImageTk.PhotoImage(img_resized)
        b2 =ttk.Button(self.parent,image=img) 
        b2.grid(row=0,column=0,columnspan=1,rowspan=5)
        self.btn_cancel.grid(row=3,column=1)
        self.btn_image.grid(row=1, column=1)
        self.btn_do.grid(row=2, column=1)
        self.label_title.grid(row=0,column=1,columnspan=1,rowspan=1,sticky='w')

    def init_gui(self):
        self.parent.title("Decrypt Message Inside Image")
        self.parent.columnconfigure(3, weight=1)
        self.parent.rowconfigure(5, weight=1)

        self.label_title = ttk.Label(self.parent, text="Decryption")
        self.contentframe = ttk.Frame(self.parent, relief="sunken")

        self.label_test2 = ttk.Label(self.contentframe, text='Enter Key: ')
        self.input_test2 = ttk.Entry(self.contentframe, width=30, validate='focusout', validatecommand=(self.validate_notempty))

        self.label_test3 = ttk.Label(self.contentframe, text='Enter Vector: ')
        self.input_test3 = ttk.Entry(self.contentframe, width=30, validate='focusout', validatecommand=(self.validate_notempty))

        self.btn_image = ttk.Button(self.parent, text='Upload Image',command = lambda:self.upload_file())
        self.btn_do = ttk.Button(self.parent, text='Decrypt Image', command=self.do_something)
        self.btn_cancel = ttk.Button(self.parent, text='Cancel', command=self.close_win)

        myFont = font.Font(family='Helvetica',size=16, weight='bold')
        self.label_title.grid(row=0, column=1, columnspan=2, sticky='nsew')
        self.label_title['font'] = myFont

        self.contentframe.grid(row=1, column=0, columnspan=3, sticky='nsew')

        self.label_test2.grid(row=1, column=0)
        self.input_test2.grid(row=1, column=1, columnspan=2,sticky='w')

        self.label_test3.grid(row=2, column=0)
        self.input_test3.grid(row=2, column=1, columnspan=2,sticky='w')

        self.btn_image.grid(row=3, column=0, sticky='e')
        self.btn_do.grid(row=3, column=1, sticky='e')
        self.btn_cancel.grid(row=3, column=2, sticky='e')

        for child in self.parent.winfo_children():
            child.grid_configure(padx=10, pady=5)
        for child in self.contentframe.winfo_children():
            child.grid_configure(padx=5, pady=2)

    def do_something(self):

        name=self.filename
        key = self.input_test2.get().strip()
        vector = self.input_test3.get().strip()

        if name:
            DecText = "Decrypted Text : " + DecryptImage(name,key,vector)
            self.label_title2=ttk.Label(self.parent,text = DecText)
            self.label_title2.grid(row=6,column=0, sticky='nsew')
            myFont = font.Font(family='Helvetica',size=13, weight='bold')
            self.label_title2['font'] = myFont
        else:
            print("Error: But for real though, field must not be empty.")            

class GUI(ttk.Frame):
    """Main GUI class"""
    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.root = parent
        self.init_gui()

    def openwindow4(self):
        self.new_win = tkinter.Toplevel(self.root) 
        SomethingWindow3(self.new_win)

    def openwindow3(self):
        self.new_win = tkinter.Toplevel(self.root) 
        SomethingWindow2(self.new_win)

    def openwindow1(self):
        self.new_win = tkinter.Toplevel(self.root) 
        SomethingWindow(self.new_win)
    
    def openwindow2(self):
        self.new_win = tkinter.Toplevel(self.root) 
        SomethingWindow4(self.new_win)

    def init_gui(self):
        self.root.title('Image Stegnography')
        self.grid(column=0, row=0, sticky='nsew')
        self.grid_columnconfigure(0, weight=1) 
        self.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(3, weight=1)
        self.root.grid_rowconfigure(3, weight=1)
        self.root.option_add('*tearOff', 'FALSE') 
        
        self.label_title = ttk.Label(self, text="   IMAGE STEGNOGRAPHY")
        myFont = font.Font(family='Sans-Serif', size=24, weight='bold')
        self.label_title['font'] = myFont

        self.btn1 = ttk.Button(self, text='Hide Image Inside Image', command=self.openwindow1)
        self.btn2 = ttk.Button(self, text='Reveal Image Inside Image', command=self.openwindow2)
        self.btn3 = ttk.Button(self, text='Encrypt Message Inside Image', command=self.openwindow3)
        self.btn4 = ttk.Button(self,text='Decrypt Message Inside Image',command=self.openwindow4)

        self.label_title.grid(row=0, column=0);
        self.btn1.grid(row=1, column=0, sticky='ew')
        self.btn2.grid(row=2, column=0, sticky='ew')
        self.btn3.grid(row=3, column=0, sticky='ew')
        self.btn4.grid(row=4, column=0, sticky='ew')

        for child in self.winfo_children():
            child.grid_configure(ipadx=10, ipady=10)

if __name__ == '__main__':
    root = tkinter.Tk()
    GUI(root)
    root.mainloop()