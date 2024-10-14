import tkinter as tk

class Window:
    def __init__(self, title: str = "Tk", size: tuple[int, int] = (800, 400)):
        self.context = tk.Tk()
        self.context.title(title)
        self.context.geometry(str(size[0])+"x"+str(size[1]))

        label = tk.Label(self.context, text="Welcome to the Wahrolator!", justify="center")
        label.config(font=("Arial", 22))
        label.pack(pady=(20, 40))

        self.context.mainloop()