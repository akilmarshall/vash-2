'''
the home tab of the application. this is the default tab to be shown when the application is run
'''
import tkinter as tk


def Home_tab(root):
    # setup the home tab
    welcome_text = tk.Label(root, text='Welcome to the VASH Report Helper')
    welcome_text.grid(column=0, row=0, padx=20, pady=20)


class Home(tk.Tk):
    def __init__(self):
        welcome_text = tk.Label(self, text='Welcome to the VASH Report Helper')
        welcome_text.grid(column=0, row=0, padx=20, pady=20)


if __name__ == '__main__':
    # root = tk.Tk()
    # Home_tab(root)
    # root.mainloop()
    root = Home()
    root.mainloop()
