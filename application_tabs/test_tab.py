import tkinter as tk


def Test_tab(root):
    test_text = tk.Label(master=root, text='test text')
    test_text.grid(column=0, row=0)


if __name__ == '__main__':
    root = tk.Tk()
    Test_tab(root)
    root.mainloop()
