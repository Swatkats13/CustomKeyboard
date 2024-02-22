import tkinter as tk

class KeyboardApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Keyboard GUI")

        
        screen_width = self.master.winfo_screenwidth()
        third_width = screen_width // 3

        
        self.groups = ["ABCDE", "FGHIJ", "KLMNO", "PQRST", "UVWXY", "Z"]
        self.group_index = 0  
        self.selected_group = self.groups[self.group_index]
        self.letter_index = 0

        
        self.group_label = tk.Label(self.master, text=self.selected_group, width=5, height=2, relief="solid", bg="green", font=("Arial", 14), fg="black")
        self.group_label.pack(side="left", fill="both", expand=True)
        self.group_label.bind("<Enter>", self.cycle_groups)

        
        self.cursor_area = tk.Label(self.master, text="", width=30, height=10, relief="solid", bg="white", font=("Arial", 16), fg="black")
        self.cursor_area.pack(side="left", fill="both", expand=True)
        self.cursor_area.bind("<Enter>", self.type_selected_letter)

        
        self.individual_letters_area = tk.Label(self.master, text="", width=10, height=10, relief="solid", bg="lightyellow", font=("Arial", 16), fg="black")
        self.individual_letters_area.pack(side="left", fill="both", expand=True)
        self.individual_letters_area.bind("<Enter>", self.display_next_letter)

    def cycle_groups(self, event):
        
        self.group_index = (self.group_index + 1) % len(self.groups)
        self.selected_group = self.groups[self.group_index]
        self.group_label.config(text=self.selected_group)

        
        self.letter_index = 0
        self.individual_letters_area.config(text="")

        
        self.display_group_letters()

    def display_group_letters(self):
        if self.selected_group:
           
            
            self.individual_letters_area.config(text="")

            
            self.display_next_letter()

    def display_next_letter(self, event=None):
        if self.letter_index < len(self.selected_group):
            current_letter = self.selected_group[self.letter_index]
            self.individual_letters_area.config(text=current_letter)
            self.master.update()  
            self.letter_index += 1

    def type_selected_letter(self, event=None):
        
        if self.selected_group and self.letter_index > 0 and self.letter_index <= len(self.selected_group):
            selected_letter = self.selected_group[self.letter_index - 1]
            self.cursor_area.config(text=f"Typed: {selected_letter}")
            self.master.focus_set()
            self.master.event_generate('<Key>', keysym=selected_letter)

if __name__ == "__main__":
    root = tk.Tk()

    
    root.geometry(f"{root.winfo_screenwidth() // 3}x{root.winfo_screenheight()}+0+0")

    app = KeyboardApp(root)
    root.mainloop()
