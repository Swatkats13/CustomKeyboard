import tkinter as tk

class KeyboardApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Keyboard GUI")

        
        screen_width = self.master.winfo_screenwidth()
        half_width = screen_width // 2

        
        self.selected_group = None

        
        self.groups = ["ABCDE", "FGHIJ", "KLMNO", "PQRST", "UVWXY", "Z"]
        self.group_index = 0  
        self.group_label = tk.Label(self.master, text=self.groups[self.group_index], width=5, height=2, relief="solid", bg="green", font=("Arial", 14), fg="black")
        self.group_label.pack(side="left", fill="both", expand=True)
        self.group_label.bind("<Enter>", self.cycle_groups)

        
        self.cursor_area = tk.Label(self.master, text="", width=30, height=10, relief="solid", bg="white", font=("Arial", 16), fg="black")
        self.cursor_area.pack(side="right", fill="both", expand=True)

    def cycle_groups(self, event):
        
        self.group_index = (self.group_index + 1) % len(self.groups)
        self.group_label.config(text=self.groups[self.group_index])

        
        self.selected_group = self.groups[self.group_index]

        
        self.display_group_letters()

    def display_group_letters(self):
        if self.selected_group:
            for char in self.selected_group:
                self.master.after(1000, lambda c=char: self.show_typed_letter(c))

    def show_typed_letter(self, letter):
        
        current_text = self.cursor_area.cget("text")
        self.cursor_area.config(text=current_text + letter)
        self.master.focus_set()

if __name__ == "__main__":
    root = tk.Tk()

    
    root.geometry(f"{root.winfo_screenwidth() // 2}x{root.winfo_screenheight()}+0+0")

    app = KeyboardApp(root)
    root.mainloop()
