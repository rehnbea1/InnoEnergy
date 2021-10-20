#fil för antingen styling av guin eller som samlingssida för olika funktioner, vi får se när jag kommit så långt
#just nu bara en test-sida

def Select_file(self):
    print("hej")
    filetypes = (('csv-files', '*.pdf'),('All files', '*.*'))
    filename = fd.askopenfilename(title='Open a file',initialdir='documents/',filetypes=filetypes)
    file_info=Label(gui,text="The file you chose is: " + filename).pack()
    return filename

def Read_file(self, filename):
    with open(filename,'r') as file:
        file = file.read()
