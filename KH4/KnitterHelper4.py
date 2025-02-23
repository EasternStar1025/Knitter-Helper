# Jennifer Bowers
# Knitter Helper
# 02/17/2025
# Version 4

# This GUI will create an interface for creating project records, retrieval, edits,
# and tracking rows for knitted or crocheted projects.

import tkinter as tk
from tkinter import ttk, PhotoImage, font
# from functools import partial

# Create data text file
file = "knitter_helper4.txt"
try:
    open(file, 'a')
    print("File opened")
except:
    open(file, 'x')
    print("File created")

# Main window
class main_window(tk.Tk):
    def __init__(self):
        super().__init__()
        # Configures Window Design
        self.title('Knitter Helper')
        self.geometry('320x320')
        self.configure(bg="lightblue")
        self.my_font= font = ("Ariel", 14, "bold")
        
        # Setting icon file paths
        self.button_exit_path: str = 'exit1.png'
        # Icon source: <a target="_blank" href="https://icons8.com/icon/23537/close-window">Exit</a> icon by <a target="_blank" href="https://icons8.com">Icons8</a>
        self.button_projects_path: str = 'menu1.png'
        # Icon source: <a target="_blank" href="https://icons8.com/icon/20406/bulleted-list">Bulleted List</a> icon by <a target="_blank" href="https://icons8.com">Icons8</a>
        self.main_image_path: str = 'yarn_100.png'
        # Icon source: <a target="_blank" href="https://icons8.com/icon/ZNv5i4TDioH0/yarn">Yarn</a> icon by <a target="_blank" href="https://icons8.com">Icons8</a>

        # Button Images/Icons
        self.button_exit_png: tk.PhotoImage = tk.PhotoImage(file=self.button_exit_path)
        self.button_projects_png: tk.PhotoImage = tk.PhotoImage(file = self.button_projects_path)
        self.main_image_png: tk.PhotoImage = tk.PhotoImage(file = self.main_image_path)
    
        # Menu Label and buttons
        self.main_image: tk.Label = tk.Label(self, image = self.main_image_png, background = "lightblue")
        self.button_exit = ttk.Button(self, image=self.button_exit_png, command = quit)      
        self.button_projects: tk.Button = tk.Button(self, image=self.button_projects_png, command=lambda: self.button_click_project_menu())
        self.main_menu_label: tk.Label = tk.Label(self, text="Knitter Helper Main Menu", font = ("Ariel", 14, "bold"), foreground ="black", background= "lightblue") 

        # Add widgets to the window
        self.main_menu_label.pack()        
        self.main_image.pack()        
        self.button_projects.pack()
        self.button_exit.pack()


    def button_click_project_menu(self) -> None:
        # Create the project_window and set focus to it
        new_window: projects_window = projects_window(self)
        new_window.grab_set() # force this window to the foreground

# Window displaying current projects
class projects_window(tk.Toplevel):
    def __init__(self, parent: tk.Tk):
        super().__init__(parent)
        self.title('Project List')
        self.geometry('320x320')
        self.configure(bg="lightblue")

        # Setting icon file paths
        self.button_exit_path: str = 'exit1.png'
        # Icon source: <a target="_blank" href="https://icons8.com/icon/23537/close-window">Exit</a> icon by <a target="_blank" href="https://icons8.com">Icons8</a>
        self.button_projects_path: str = 'menu1.png'
        # Icon source: <a target="_blank" href="https://icons8.com/icon/20406/bulleted-list">Bulleted List</a> icon by <a target="_blank" href="https://icons8.com">Icons8</a>
        self.button_back_path: str = 'back1.png'
        # Icon source: <a target="_blank" href="https://icons8.com/icon/3483/return">Return</a> icon by <a target="_blank" href="https://icons8.com">Icons8</a>
        self.button_add_path: str = 'add1.png'
        # Icon source: <a target="_blank" href="https://icons8.com/icon/5271/add-properties">Add properties</a> icon by <a target="_blank" href="https://icons8.com">Icons8</a>

        # Button Images/Icons
        self.button_exit_png: tk.PhotoImage = tk.PhotoImage(file=self.button_exit_path)
        self.button_projects_png: tk.PhotoImage = tk.PhotoImage(file = self.button_projects_path)
        self.button_save_png: tk.PhotoImage = tk.PhotoImage(file = self.button_add_path)
        self.button_back_png: tk.PhotoImage = tk.PhotoImage(file = self.button_back_path)

        # Label Widgets
        self.project_label: tk.Label = tk.Label(self, text="Project List", font = ("Ariel", 14, "bold"), foreground ="black", background= "lightblue")
        self.project_list: tk.Label = tk.Label(text = add_project_window.read_file)

        # Add and Exit Buttons
        self.button_new_project: tk.Button = tk.Button(self, text = "Add a Project", image = self.button_save_png, command = self.button_add)
        self.back_button = ttk.Button(self, text = "Back", image= self.button_back_png, command = self.close_window)
        self.button_exit = ttk.Button(self, text = "Exit", image=self.button_exit_png, command = quit)

        # Adds widgets to the window
        self.project_label.pack()
        self.button_new_project.pack()
        self.back_button.pack()
        self.button_exit.pack()
    
    def button_add(self) -> None:
        # Create the add_project window and set focus to it
        add_window: add_project_window = add_project_window(self)
        add_window.grab_set() # force this window to the foreground

    # def create_radio_buttons(self):
    #     variables = [self.data]

    #     for i in range(variable):
    #         # Create the new variable
    #         variable = tk.IntVar()
    #         variables.append(variable)

    #         # Create the command using partial
    #         command = partial(function, i)

    #         # Create the radio button
    #         list_button = tk.Radiobutton(self, variable=variable, value=i, command=command)
    #         list_button.pack()

    def close_window(self):
        add_project_window.destroy(self)

    def read_file(self):
        self.file_path = "knitter_helper4.txt"
    # Read the file contents 
        with open(self.file_path, "r") as file:
            print(file.read())
            file.close()

# Window to add new projects to the list
class add_project_window(tk.Toplevel):
    def __init__(self, parent: tk.Tk):
        super().__init__(parent)
        self.title('Add A New Project')
        self.geometry('320x350')
        self.configure(bg="lightblue")

        # Setting icon file paths
        self.button_exit_path: str = 'exit1.png'
        # Icon source: <a target="_blank" href="https://icons8.com/icon/23537/close-window">Exit</a> icon by <a target="_blank" href="https://icons8.com">Icons8</a>
        self.button_projects_path: str = 'menu1.png'
        # Icon source: <a target="_blank" href="https://icons8.com/icon/20406/bulleted-list">Bulleted List</a> icon by <a target="_blank" href="https://icons8.com">Icons8</a>
        self.button_back_path: str = 'back1.png'
        # Icon source: <a target="_blank" href="https://icons8.com/icon/3483/return">Return</a> icon by <a target="_blank" href="https://icons8.com">Icons8</a>
        self.button_add_path: str = 'add1.png'
        # Icon source: <a target="_blank" href="https://icons8.com/icon/5271/add-properties">Add properties</a> icon by <a target="_blank" href="https://icons8.com">Icons8</a>

        # Button Images/Icons
        self.button_exit_png: tk.PhotoImage = tk.PhotoImage(file=self.button_exit_path)
        self.button_projects_png: tk.PhotoImage = tk.PhotoImage(file = self.button_projects_path)
        self.button_save_png: tk.PhotoImage = tk.PhotoImage(file = self.button_add_path)
        self.button_back_png: tk.PhotoImage = tk.PhotoImage(file = self.button_back_path)

        # Entry labels
        self.name_label: tk.Label = tk.Label(self, text = "Project Name" ,foreground="black", background= "lightblue", border= 1, borderwidth= 2)
        self.type_label: tk.Label = tk.Label(self, text = "Project Type", foreground="black", background= "lightblue", border= 1, borderwidth= 2)
        self.yarn_label: tk.Label = tk.Label(self, text = "Yarn Weight",  foreground="black", background= "lightblue", border= 1, borderwidth= 2)
        self.needle_label: tk.Label = tk.Label(self,text = "Needle Size", foreground="black", background= "lightblue", border= 1, borderwidth= 2)

        # Entry Text Boxes
        self.name_entry: tk.Entry = tk.Entry(self, foreground= "black", bg= "white", border= 1, borderwidth= 2)
        self.type_entry: tk.Entry = tk.Entry(self, foreground= "black", bg= "white", border= 1, borderwidth= 2)
        self.yarn_entry: tk.Entry = tk.Entry(self, foreground= "black", bg= "white", border= 1, borderwidth= 2)

        self.needle_entry: tk.Entry = tk.Entry(self, bg= "white", border= 1, borderwidth= 2)
        # Save and Exit Buttons
        self.button_exit = ttk.Button(self, text = "Exit", image= self.button_exit_png, command = quit)
        self.back_button = ttk.Button(self, text = "Back", image= self.button_back_png, command = self.close_window)
        self.save_button: tk.Button = tk.Button(self, text='Save Project', image = self.button_save_png, command = self.write_to_file)

        # Adding widgets to the window
        self.name_label.pack()        
        self.name_entry.pack()
        self.type_label.pack()
        self.type_entry.pack()
        self.yarn_label.pack()
        self.yarn_entry.pack()
        self.needle_label.pack()
        self.needle_entry.pack()
        self.save_button.pack()
        self.back_button.pack() 
        self.button_exit.pack() 

        # Creates project lists
        self.name = []
        self.type = []
        self.yarn = []
        self.needle = []
     
    def write_to_file(self):
        # Create list appendments from newest entries
        self.name.append(self.name_entry.get())
        self.type.append(self.type_entry.get())
        self.yarn.append(self.yarn_entry.get())
        self.needle.append(self.needle_entry.get())
        self.data = [self.name, self.type, self.yarn, self.needle]  

        # Set save text file path
        self.file_path = "knitter_helper4.txt"

        # Save to file
        with open(self.file_path, 'a') as file:
            file.write((str(self.data) + '\n'))
            print("Saved Successfully")
            file.close()
        self.read_file()

    def read_file(self):
        # Read the file contents 
        with open(self.file_path, "r") as file:
            print(file.read())
            file.close()
    
    def close_window(self):
        add_project_window.destroy(self)
    
# Run program
main_menu = main_window()
main_menu.mainloop()