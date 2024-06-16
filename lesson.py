import tkinter as tk
from tkinter import ttk

class App():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("550x450")
        self.root.title("Dzhanbekov's app")
        self.mainframe = tk.Frame(self.root, background='yellow')
        self.mainframe.pack(fill='both', expand=True)


        self.text = ttk.Label(self.mainframe, text="wassup!!!", background='lightgreen', font=('Brass Mono', 25))
        self.text.grid(row=0, column=0)

        self.set_text_field = ttk.Entry(self.mainframe)
        self.set_text_field.grid(row=1, column=0, pady=30, sticky="NWES")
        set_text_button = ttk.Button(self.mainframe, text='click it, babe', command=self.set_text)
        set_text_button.grid(row=1, column=1, pady=30)

        color_options = ['red', 'green', 'blue', 'black', 'white', 'cyan', 'purple', 'pink']
        self.set_color_field = ttk.Combobox(self.mainframe, values=color_options)
        self.set_color_field.grid(row=2, column=0, sticky='NWES', pady=10)
        set_color_button = ttk.Button(self.mainframe, text='click to confirm', command=self.set_color)
        set_color_button.grid(row=2, column=1, pady=10)

        self.reverse_text = ttk.Button(self.mainframe, text="Reverse text", command=self.reverse)
        self.reverse_text.grid(row=3, column=0, sticky='NWES', pady=10)
        self.root.mainloop()
        return

    def set_text(self):
        newtext = self.set_text_field.get()
        self.text.config(text=newtext)

    def set_color(self):
        newcolor = self.set_color_field.get()
        self.text.config(foreground=newcolor)

    def reverse(self):
        newtext = self.text.cget('text')
        reversed = newtext[::-1]
        self.text.config(text=reversed)

if __name__ == '__main__':
    App()