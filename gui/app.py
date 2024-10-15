import tkinter as tk

class Window:
    def __init__(self, title: str = "Tk", size: tuple[int, int] = (800, 400)):
        self.context = tk.Tk()
        self.context.title(title)
        self.context.geometry(str(size[0])+"x"+str(size[1]))
        self.context.config(bg="#1d1d1d")
        self.main_panel = tk.PanedWindow(self.context, orient="horizontal")
        self.main_panel.pack(fill="both", expand=True)

        self.main_frame = tk.Frame(self.main_panel, bg="#1d1d1d")
        self.left = tk.Frame(self.main_panel, width=200, bg="#171717")
        self.main_frame.pack()
        self.left.pack()
        self.main_panel.add(self.left)
        self.main_panel.add(self.main_frame)

        label = tk.Label(self.main_frame, text="Welcome to the Wahrolator!", justify="center")
        label.config(font=("Arial", 25), bg="#1d1d1d")
        label.pack(pady=(20, 0))
        
        sub = tk.Label(self.main_frame, text="No image opened yet.", justify="center")
        sub.config(font=("Arial", 15), fg="gray", bg="#1d1d1d")
        sub.pack(pady=(0, 40))

        button = tk.Button(self.main_frame, justify="center", text="Open image")
        button.config(font=("Arial", 18), bg="#1d1d1d")
        button.pack()

        self.context.mainloop()