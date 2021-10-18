
def style(self):
    style = Style()
    # This will be adding style, and
    # naming that style variable as
    # W.Tbutton (TButton is used for ttk.Button).
    style.configure('W.TButton', font =
                   ('calibri', 10, 'bold', 'underline'),
                    foreground = 'red')

    # Style will be reflected only on
    # this button because we are providing
    # style only on this Button.
    ''' Button 1'''
    btn1 = Button(root, text = 'Quit !',
                    style = 'W.TButton',
                 command = root.destroy)
    btn1.grid(row = 0, column = 3, padx = 100)
