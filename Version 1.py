import tkinter as tk

class KeyboardApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Keyboard GUI")

        
        screen_width = self.master.winfo_screenwidth()
        half_width = screen_width // 2

        
        self.cursor_area = tk.Label(self.master, text="Cursor Rest Area", width=30, height=10, relief="solid", bg="white", font=("Arial", 16), fg="black")
        self.cursor_area.pack(side="right", fill="both", expand=True)

        
        self.groups = ["ABCDE", "FGHIJ", "KLMNO", "PQRST", "UVWXY", "Z"]
        self.group_index = 0  
        self.group_label = tk.Label(self.master, text=self.groups[self.group_index], width=5, height=2, relief="solid", bg="green", font=("Arial", 14), fg="black")
        self.group_label.pack(side="left", fill="both", expand=True)
        self.group_label.bind("<Enter>", self.cycle_groups)
        self.group_label.bind("<Button-1>", self.type_letter)

    def cycle_groups(self, event):
        
        self.group_index = (self.group_index + 1) % len(self.groups)
        self.group_label.config(text=self.groups[self.group_index])

    def type_letter(self, event):
        
        selected_letter = self.group_label.cget("text")[0]
        self.cursor_area.config(text=f"Typed: {selected_letter}")
        self.master.focus_set()
        self.master.event_generate('<Key>', keysym=selected_letter)

if __name__ == "__main__":
    root = tk.Tk()

    
    root.geometry(f"{root.winfo_screenwidth() // 2}x{root.winfo_screenheight()}+0+0")

    app = KeyboardApp(root)
    root.mainloop()
