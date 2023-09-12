from UI.ui import *
from UI.gui import *
if __name__ == '__main__':

    command=input('Choose between UI and GUI:')
    if command.lower()=='gui':
        g = GUI()
        g.mainloop()
    else:
        u=UI()
        u.start()