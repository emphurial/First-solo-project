from tkinter import *

class Window():
    def __init__(self):
        self.window = Tk()
        self.window.title('Game Window')
        self.window.geometry('500x500')
        
        #game introduction
        self._menu_header("Welcome to the World \nof \nINSERT NAME HERE")
        self._menu_button(self.window, "Start", 18, 0.5, self._start_menu)
        self._menu_button(self.window, 'Options', 18, 0.6)
        self._menu_button(self.window, 'Quit', 18, 0.9, self.window.destroy)

        self.previous_menu = None

        self.window.mainloop()

    def _new_window(self, title = None, geometry = '500x500'):
        self.window.destroy()
        self.window = Tk()
        self.window.title(title)
        self.window.geometry(geometry)
    
    def _menu_button(self, window, text, fontsize, ypos, command=None):
        button = Button(window, text=text, font=('times new roman', fontsize), width=8, command=command)
        button.place(relx=0.5, rely=ypos, anchor=CENTER)     

    def _menu_header(self, text):
        menu_header = Label(self.window, text=text, fg='dark blue', font=('times new roman', 30))
        menu_header.place(relx= 0.5, rely=0.2, anchor=CENTER)

    def _start_menu(self):
        self._new_window('Start Menu')
        self.previous_menu = self.__init__
        
        self._menu_header("Choose your adventure.")
        self._menu_button(self.window, 'New Game', 18, 0.5, self._new_game)
        #Need to add Load Game Function
        self._menu_button(self.window, 'Load Game', 18, 0.6)
        self._menu_button(self.window, 'Back', 18, 0.9, self._back_button)

    def _new_game(self):
        self._new_window('New Game')
        self._menu_header('Choose your class.')
        #Need to add warrior
        self._menu_button(self.window, 'Warrior', 18, 0.5)
        #Need to add wizard
        self._menu_button(self.window, 'Wizard', 18, 0.6)
        self._menu_button(self.window, 'Back', 18, 0.9, self._back_button)



    def _back_button(self):
        self.window.destroy()
        self.window = self.previous_menu()

