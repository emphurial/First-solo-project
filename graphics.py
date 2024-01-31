from tkinter import *
from player import Player

class Window():
    def __init__(self):
        self.window = Tk()
        self.window.title('Game Window')
        self.width = int(self.window.winfo_screenwidth() // 2.21)
        self.height = int(self.window.winfo_screenheight() // 6)
        self.window.geometry(f'600x600+{self.width}+{self.height}')
        self.screen = []
        self.entry = None
        self.previous_menu = None
        self.canvas = None
        Player.__init__(Player)
        #game introduction
        self._menu_header("Welcome to the World \nof \nINSERT NAME HERE")
        self._menu_button("Start", 18, 0.5, self._start_menu)
        self._menu_button('Options', 18, 0.6)
        self._menu_button('Quit', 18, 0.9, self.window.destroy)

        self.window.mainloop()
    
    def _menu_header(self, text, textfont = ('times new roman', 30), rely = 0.2, fg = 'dark blue'):
        menu_header = Label(self.window, text=text, fg=fg, font=textfont)
        menu_header.place(relx= 0.5, rely=rely, anchor=CENTER)
        self.screen.append(menu_header)

    def _menu_button(self, text, fontsize, ypos, command=None, width=8, xpos = 0.5):
        button = Button(self.window, text=text, font=('times new roman', fontsize), width=width, command=command)
        button.place(relx=xpos, rely=ypos, anchor=CENTER)
        self.screen.append(button)     

    def _game_header(self, text, textfont = ('times new roman', 30), relx=0.02, rely=0.1, fg='dark blue'):
        menu_header = Label(self.window, text=text, fg=fg, font=textfont)
        menu_header.place(relx=relx, rely=rely)
        self.screen.append(menu_header)

    def _game_button(self, text, fontsize, ypos, command=None, width=15):
        button = Button(self.window, text=text, font=('times new roman', fontsize), width=width, command=command)
        button.place(relx=0.2, rely=ypos)
        self.screen.append(button)

    def _back_button(self):
        self._clear_screen()
        self.previous_menu()

    def _game_menu(self):
        self.canvas = Canvas(self.window)
        self.canvas.create_line(638, 0, 638, 600, fill='dark gray', width=2)
        self.canvas.pack(fill=BOTH, expand=1)
        def _game_menu_button(text, rely, command = None):
            button = Button(self.window, text=text, font=('times new roman', 18), width=9, command=command)
            button.place(relx=0.8, rely=rely)
            self.screen.append(button)
        # Stat Screen
        def _display_stats():
            self._clear_screen()
            self._game_menu()
            def _stat_menu_label(text, ypos, xpos = 0.0):
                label = Label(self.window, text=text, font=('times new roman', 18), fg='black')
                label.place(relx=xpos, rely=ypos)
                self.screen.append(label)
            
            name = Label(self.window, text=f'{Player._player_name} the {Player._player_gender} {Player._player_class}.', font=('times new roman', 25))
            name.place(relx=0.0, rely=0.02)
            self.screen.append(name)
            _stat_menu_label(f'Level : {Player._player_level}', 0.2)
            _stat_menu_label(f'Experience : {Player._player_xp}', 0.2, 0.2)
            _stat_menu_label(f'Gold : {Player._player_gold}', 0.2, 0.5)
            _stat_menu_label(f'Health : ({Player._player_current_health} / {Player._player_max_health})', 0.3)
            _stat_menu_label(f'Mana : ({Player._player_max_mana} / {Player._player_max_mana})', 0.4)
            _stat_menu_label(f'Attack : {Player._player_attack}', 0.5)
            _stat_menu_label(f'Defence : {Player._player_defence}', 0.6)
            self._menu_button('Back', 18, 0.9, self._back_button, 8, 0.4)

        _game_menu_button('Stats', 0.0, _display_stats)
        ################
        #Add Items Menu
        _game_menu_button('Items', 0.07)
        ################
        #Add Save Function
        _game_menu_button('Save', 0.79)
        ################
        #Add Load Function
        _game_menu_button('Load', 0.86)
        _game_menu_button('Quit', 0.93, self._quit_confirm)

    #Empties the screen
    def _clear_screen(self):
        for widget in self.screen:
            widget.place_forget()
        if self.entry != None:
            self.entry.place_forget()
        if self.canvas != None:
            self.canvas.pack_forget()
        

    #Quit confirmation
    def _quit_confirm(self):
        self._clear_screen()
        self._menu_header('Are you sure you want to quit?')
        self._menu_header("All unsaved progress will be lost.", ('times new roman', 20), 0.4, 'dark red')
        self._menu_button('Back', 18, 0.8, self._back_button)
        self._menu_button('Confirm', 18, 0.9, self.window.destroy)




    #Start Menu
    def _start_menu(self):
        self._clear_screen()
        self.previous_menu = self.__init__
        self._menu_header("Choose your adventure.")
        self._menu_button('New Game', 18, 0.5, self._new_game)
        ###############################
        #Need to add Load Game Function
        self._menu_button('Load Game', 18, 0.6)
        self._menu_button('Back', 18, 0.9, self._back_button)

    #Character Creation
    def _new_game(self, no_name = 0, no_gender = 0):
        self._clear_screen()
        str = StringVar()
        str.set('Male')
        if no_name == 1:
            invalid = Label(self.window, text = 'Please enter a name.', fg='red', font=('times new roman', 20))
            invalid.place(relx=0.5, rely=0.3, anchor=CENTER)
            self.screen.append(invalid)
        if no_gender == 1:
            invalid_gender = Label(self.window, text='Please chosoe a gender.', fg='red', font=('times new roman', 20))
            invalid_gender(relx=0.5, rely=0.3, anchor=CENTER)
        self._menu_header("Who are you?")
        self.entry = Entry(self.window)
        self.entry.place(relx=0.5, rely=0.5, anchor=CENTER)
        male = Radiobutton(self.window, text='Male', variable=str, value='Male')
        female = Radiobutton(self.window, text='Female', variable=str, value='Female')
        other = Radiobutton(self.window, text='Other', variable=str, value='')
        self.screen.append(male)
        self.screen.append(female)
        self.screen.append(other)
        male.place(relx=0.4, rely=0.6)
        female.place(relx=0.4, rely=0.65)
        other.place(relx=0.4, rely=0.7)
        self._menu_button('Confirm', 18, 0.9, lambda: self._store_name(self.entry.get(), str.get()))

    #Stores player name and gender
    def _store_name(self, name_entry, gender):
        if len(name_entry) == 0:
            self._new_game(1)
        else:  
            Player._player_name = name_entry
            Player._player_gender = gender
            self._choose_class()
    
    #Class selection
    def _choose_class(self):
        self._clear_screen()
        self._menu_header('Choose your class.')
        self._menu_button('Warrior', 18, 0.5, self._warrior_chosen)
        self._menu_button('Wizard', 18, 0.6, self._wizard_chosen)
        self._menu_button('Back', 18, 0.9, self._back_button)

    def _warrior_chosen(self):
        Player._warrior(Player)
        self.window.geometry('800x600')
        self._game_start()

    def _wizard_chosen(self):
        Player._wizard(Player)
        self.window.geometry('800x600')
        self._game_start()

    #The beginning of the game
    def _game_start(self):
        self._clear_screen()
        self._game_menu()
        self.previous_menu = self._game_start
        self._game_header("You awaken groggily in a firm cushioned bed.\n Around you is a well-furnished wooden room.\n Sounds of glass clinking and loud banter\n can be heard through the door.\n You don't remember how you got here,\n or where you were before.", ('times new roman', 18))
        self._game_header("What would you like to do?", ('times new roman', 20), 0.12, 0.6, 'blue')
        ###############################
        self._game_button('Search the room', 18, 0.8, None, 15)
        ###############################
        self._game_button('Exit the room', 18, 0.9, None, 15)



