import webview
import tkinter as tk
from tkinter import ttk

class PokiApp:
    def __init__(self, master):
        self.master = master
        self.master.title("QuickSearch")
        self.master.geometry("330x35")
		
        self.frame = tk.Frame(self.master)
		
		
        # Dodanie przycisku w GUI
        self.open_button = ttk.Button(self.frame, text="Open", command=self.open_webview)
        self.open_button.grid(column=0, row=0)
        self.url_bar = tk.Entry(self.frame, width=30)
        self.url_bar.grid(column=1, row=0)
        self.frame.pack()
		

    def open_webview(self):
        # Tworzenie i uruchamianie WebView
        webview.create_window(str(self.url_bar.get()), str(self.url_bar.get()))
        webview.start()

if __name__ == "__main__":
    root = tk.Tk()
    app = PokiApp(root)
    root.mainloop()

