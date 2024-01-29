from tkinter import *
from player import Player

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

    def _new_game(self, no_name = 0):
        Player()
        self._new_window('New Game')
        if no_name == 1:
            invalid = Label(self.window, text = 'Please enter a name.', fg='red', font=('times new roman', 20))
            invalid.place(relx=0.5, rely=0.3, anchor=CENTER)
        self._menu_header("What is your name?")
        name_entry = Entry(self.window)
        name_entry.place(relx=0.5, rely=0.5, anchor=CENTER)
        self._menu_button(self.window, 'Confirm', 18, 0.9, lambda: self._store_name(name_entry.get()))

    def _store_name(self, name_entry):
        if len(name_entry) == 0:
            self._new_game(1)
        else:  
            Player._player_name = name_entry
            self._choose_class()
        
    def _choose_class(self):
        self._new_window('Choose Class')
        self._menu_header('Choose your class.')
        self._menu_button(self.window, 'Warrior', 18, 0.5, self._warrior_chosen)
        self._menu_button(self.window, 'Wizard', 18, 0.6, self._wizard_chosen)
        self._menu_button(self.window, 'Back', 18, 0.9, self._back_button)

    def _warrior_chosen(self):
        Player._warrior(Player)
        self._game_start()

    def _wizard_chosen(self):
        Player._wizard(Player)
        self._game_start()

    def _game_start(self):
        self._new_window('The Journey Begins', '700x700')
        self._menu_button(self.window, 'Next', 18, 0.9)

    def _back_button(self):
        self.window.destroy()
        self.window = self.previous_menu()

