# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 20:06:11 2019

@author: georg
"""

import webbrowser
import tkinter
from tkinter import filedialog
from tkinter import messagebox


class Gui:
    
    """
    tkinter GUI
    """
    
    def __init__(self, ip, logger):
        
        # Logger
        self.logger = logger
        
        # Image Processor
        self.ip = ip
        
        # Create the window
        self.create_window()
        
        # Creates the menu bar
        self.create_menu()
        
    # TODO: Delete once no further use exists for this
    def dummy(self):
        pass
    
    def create_window(self):
        
        """
        create_window creates a new tkinter window including basic setup
        """
        
        # TODO: When window resizes, resize all widgets. Prevent window from becoming too small
        
        # Main tkinter window
        self.root = tkinter.Tk()
        
        # Window Setup
        self.root.title("Image Filters")
        self.root.geometry("400x400")
        
        self.logger.debug("Successfully created a new window.")

    def create_menu(self):
        
        """
        create_menu creates the menu and submenus inside of it
        """
        
        self.menu = tkinter.Menu(self.root)
        self.root.config(menu=self.menu)
        
        self.logger.debug("Successfully created the base menu.")
        
        # File Menu
        self.fileMenu = tkinter.Menu(self.menu)
        self.menu.add_cascade(label="File", underline=0, menu = self.fileMenu)
        self.fileMenu.add_command(
                label="Open", 
                underline=1,
                command=self.open_dialog,
                accelerator="Ctrl+O"
                )
        self.fileMenu.add_command(
                label="Save", 
                underline=1,
                command=self.save_dialog,
                accelerator="Ctrl+S"
                )
        self.fileMenu.add_separator()
        self.fileMenu.add_command(
                label="Quit", 
                underline=1,
                command=self.close_window,
                accelerator="Ctrl+Q"
                )
        
        self.logger.debug("Successfully created the File menu.")
        
        # Help Menu
        self.helpMenu = tkinter.Menu(self.menu)
        self.menu.add_cascade(label="Help", menu=self.helpMenu)
        self.helpMenu.add_command(
                label="How to use",
                command=self.how_to
                )
        self.helpMenu.add_command(
                label="Open Logs Folder",
                # TODO: Open log directory
                command=self.show_logs
                )
        self.helpMenu.add_command(
                label="Repository & Documentation",
                command=self.repo_docs
                )
        
        self.logger.debug("Successfully created the Help menu.")

    def open_dialog(self):
        
        """
        open_dialog creates a new window allowing the user to get the filepath of the file they want to open
        """
        
        self.logger.debug("User has opened the open_dialog.")
        
        try:
            self.root.filename = filedialog.askopenfilename(
                initialdir="/", 
                title = "Select a File", 
                filetypes=(
                        ("All files", "*.*"),
                        (".bmp files", "*.bmp"),
                        (".jpg files", "*jpg"), 
                        (".png files", "*.png"), 
                        (".tiff files", "*.tiff")
                        )
                )
        except:
            self.logger.exception(f"Failed to acquire the filepath: {self.root.filename}")
            raise
        else:
            self.logger.debug(f"Successfully acquired the filepath: {self.root.filename}")
        
        # TODO: Check to make sure filepath ends in compatible format extension
        
        if len(self.root.filename) > 0:
            
            # Calls ip.load_image to open the specified image file
            self.logger.debug("Calling ip.load_image.")
            self.ip.load_image(self.root.filename)

    def save_dialog(self):
        
        """
        save_dialog creates a new window allowing user to specify the save file path for the modified file
        """
        
        # TODO: Make sure user specified a file extension. Pop up message box advising to use an available extension
        
        self.logger.debug("User has opened the save_dialog.")
        
        #Check if a file has actually been opened        
        if self.ip.image_opened == False:
            
            # Warn user that there is no file open and file cannot be saved
            messagebox.showinfo("Image Filters: Unable to save file", "There is no file to save. Please open and modify a file first.")
        
        else: 
        
            try: 
                # Ask user to select file save location
                self.root.savepath = filedialog.asksaveasfilename(
                    initialdir="/",
                    title="Save file",
                    filetypes=(
                            ("All files", "*.*"),
                            (".bmp files", "*.bmp"),
                            (".jpg files", "*jpg"), 
                            (".png files", "*.png"), 
                            (".tiff files", "*.tiff")
                            )
                    )
            except:
                self.logger.exception(f"Failed to acquire the save path: {self.root.filename}")
                raise
            else:
                self.logger.debug(f"Successfully acquired the save path: {self.root.filename}")
                
            # Calls ip.save_image to save the image at specified path
            self.logger.debug("Calling ip.save_image.")
            self.ip.save_image(self.root.savepath)
    
    def close_window(self):
        
        """
        close_window destroys the tkinter window and closes the program
        """
        
        self.logger.debug("User selected Quit from the File menu. Quitting program.")
        
        # Destroys window and closes program
        self.root.destroy()
        
    def how_to(self):
        
        """
        Shows a how to use screen in a message box
        """
        
        how_to_instructions = """HOW TO USE:
            
1. Open a file using File > Open, or Ctrl+O
2. Modify image using sliders
3. Save modified file using File > Save, or Ctrl+S

In case of any bugs, export the logs and submit them as a bug at the repository which can be found by clicking: 

Help > Repository & Documentation.
"""
        
        tkinter.messagebox.showinfo("Instructions", how_to_instructions)

    def show_logs(self):
        
        # Export Logs
        print("Exporting logs")
        pass
        
    def repo_docs(self):
        
        """
        repo_docs opens a new window advising user that they are about to visit the repository link.
        If the user clicks yes, it goes to url and closes window. If they click no, it simply closes
        the window.
        """
        
        # TODO: Improve the look of the window
    
        # Repository URL
        self.repo_url = "https://github.com/GeorgeCiesinski/image-filters"
    
        # Create new window
        self.links = tkinter.Tk()
        
        # Window Setup
        self.links.title("Repository & Documentation")
        self.links.geometry("320x150")
        
        # Create Labels
        self.open_link_label = tkinter.Label(
                self.links,
                text="You are about to open the project repository link:"
                )
        self.link_url_label = tkinter.Label(
                self.links,
                text=self.repo_url
                )
        self.empty = tkinter.Label(
                self.links,
                text=""
                )
        
        # Create Buttons
        self.yes_button = tkinter.Button(
                self.links,
                text="YES",
                width=6,
                height=1,
                bd=4,
                command=self.open_link
                )
        self.no_button = tkinter.Button(
                self.links,
                text="NO",
                width=6,
                height=1,
                bd=4,
                command=self.close_links_window
                )
        
        # Pack widgets into Window
        # Labels
        self.open_link_label.grid(row=1, column=0, columnspan=3)
        self.link_url_label.grid(row=2, column=0, columnspan=3)
        self.empty.grid(row=3, column=0, columnspan=3)
        # Buttons
        self.yes_button.grid(row=4, column=0)
        self.no_button.grid(row=4, column=2)
    
    def open_link(self):
        
        # Opens link after user presses yes. Opens as a tab and raises the window
        webbrowser.open(self.repo_url, new=0, autoraise=True)
        
        # Calls function to close window
        self.close_links_window()
    
    def close_links_window(self):
        
        # Closes Repository & Documentation window
        self.links.destroy()