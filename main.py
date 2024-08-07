import tkinter as tk
from tkinter import ttk
import os
import json
from tkinter import messagebox

class App:
    
    
    username = ''
    
    total_score = 0
    total_score_text = f'Счет: {total_score}'
    current_points = 0
    current_points_text = f'Текущие очки: {current_points}'
    
    click_upgrades = 0
    click_upgrades_text = f'Улучшения кликов: {click_upgrades}'
    workers = 0
    workers_text = f'Количество работников: {workers}'
    click_modifier = 1
    click_modifier_text = f'Модификатор кликов: {click_modifier}'
    worker_modifier = 1
    worker_modifier_text = f'Модификатор работников: {worker_modifier}'
    
    click_upgrade_cost = 100
    click_upgrade_cost_text = f'Стоимость: {click_upgrade_cost}'
    worker_upgrade_cost = 500
    worker_upgrade_cost_text = f'Стоимость: {worker_upgrade_cost}'
    click_mod_upgrade_cost = 2000
    click_mod_upgrade_cost_text = f'Стоимость: {click_mod_upgrade_cost}'
    worker_mod_upgrade_cost = 2000
    worker_mod_upgrade_cost_text = f'Стоимость: {worker_mod_upgrade_cost}'
    
    worker_clicking_enabled = False
    warn_shown = False
    
    def __init__( self ):
        
        self.root = tk.Tk()
        self.root.geometry( '600x600' )
        self.root.resizable( False, False )
        self.root.title( 'Clickerino v.1.0.0a' )
        self.icon = tk.PhotoImage( file = 'assets/click.png' )
        self.root.iconphoto( True, self.icon )
        # Version 1.0.0 [1 global update, 0 bug fix, 0 new feature] - alpha
        # Initialize Main Menu or Registration Menu for new user
        if os.path.exists( 'data.json' ):
            self.parse_data()
            self.Main_Menu_Frame()
        else:
            self.New_User_Frame()
        # Start App
        self.root.mainloop()
    
    def __del__(self):
        # Save progress on quit
        self.save( 'data.json' , self.game_data )
    
    def save( self, path: str, data: dict ):
        open( path, 'w' ).write( json.dumps( data ) )
    
    def load( self, path: str ):
        self.game_data = json.loads( open( path, 'r' ).read() )
    
    def parse_data( self):
        # Parse loaded data and initialize variables for work
        self.load( 'data.json' )
        self.username = self.game_data['user']
        
        self.total_score = self.game_data['total_score']
        self.total_score_text = f'Счет: {self.total_score}'
        self.current_points = self.game_data['current_points']
        self.current_points_text = f'Текущие очки: {self.current_points}'
        
        self.click_upgrades = self.game_data['click_upgrades']
        self.click_upgrades_text = f'Улучшения кликов: {self.click_upgrades}'
        self.workers = self.game_data['workers']
        self.workers_text = f'Количество работников: {self.workers}'
        
        self.click_modifier = self.game_data['click_modifier']
        self.click_modifier_text = f'Модификатор кликов: {self.click_modifier}'
        self.worker_modifier = self.game_data['workers_modifier']
        self.worker_modifier_text = f'Модификатор работников: {self.worker_modifier}'
        
        self.click_upgrade_cost = self.game_data['click_upgrade_cost']
        self.click_upgrade_cost_text = f'Стоимость: {self.click_upgrade_cost}'
        self.worker_upgrade_cost = self.game_data['worker_upgrade_cost']
        self.worker_upgrade_cost_text = f'Стоимость: {self.worker_upgrade_cost}'
        self.click_mod_upgrade_cost = self.game_data['click_mod_upgrade_cost']
        self.click_mod_upgrade_cost_text = f'Стоимость: {self.click_mod_upgrade_cost}'
        self.worker_mod_upgrade_cost = self.game_data['worker_mod_upgrade_cost']
        self.worker_mod_upgrade_cost_text = f'Стоимость: {self.worker_mod_upgrade_cost}'
    
    def create_new_data( self, username: str ):
        self.game_data = {
            'user': f'{username}',
            'total_score': 0,
            'current_points': 0,
            'click_upgrades': 0,
            'workers': 0,
            'click_modifier': 1,
            'workers_modifier': 1,
            'click_upgrade_cost': 100,
            'worker_upgrade_cost': 500,
            'click_mod_upgrade_cost': 2000,
            'worker_mod_upgrade_cost': 2000
        }
        self.save( 'data.json' , self.game_data )
    
    def Switch_Frame( self, frame: tk.Frame, call_func_frame: object ):
        # Change frames
        if callable( call_func_frame ):
            frame.destroy()
            call_func_frame()
        else:
            # If object is not callable - raise error
            raise Exception( f'[ERROR] : {call_func_frame} : is not callable' )
            
    
    def Main_Menu_Frame( self ):
        # Just a formal structure
        self.main_menu_frame = tk.Frame( master = self.root )
        self.main_menu_frame.pack( expand = True, fill = tk.BOTH )
        
        self.button_play = tk.Button( master = self.main_menu_frame, text = 'продолжить', command = lambda: self.Switch_Frame( self.main_menu_frame, self.Play_Scene ) )
        self.button_play.place( relx = 0.1, rely = 0.5, anchor = 'w' )
    
    def New_User_Frame( self ):
        
        self.new_user_frame = tk.Frame( master = self.root )
        self.new_user_frame.pack( expand = True, fill = tk.BOTH )
        
        def confirm():
            
            username = self.user_input.get()
            # User name can't be empty ! - Actually can, but i want so ;)
            # Later make display user name
            if username != '':
                self.create_new_data( username )
                self.Switch_Frame( self.new_user_frame, self.Play_Scene )
                
            else:
                messagebox.showerror( 'ошибка', 'имя пользователя не может быть пустым' )
        
        self.user_label = tk.Label( master = self.new_user_frame, text = 'введите свой никнейм' )
        self.user_label.place( relx = 0.1, rely = 0.35, anchor = 'w' )
        
        self.user_input = ttk.Entry( master = self.new_user_frame )
        self.user_input.place( relx = 0.1, rely = 0.4, anchor = 'w' )
        
        self.button_continue = tk.Button( master = self.new_user_frame, text = 'продолжить', command = confirm )
        self.button_continue.place( relx = 0.1, rely = 0.5, anchor = 'w' )
    
    def Play_Scene( self ):
        
        self.play_scene_frame = tk.Frame( master = self.root )
        self.play_scene_frame.pack( expand = True, fill = tk.BOTH )
        
        def click(event: tk.Event):
            # Clicks handler
            self.current_points += int(1+self.click_upgrades * self.click_modifier) 
            self.total_score += int(1+self.click_upgrades * self.click_modifier)
            self.current_points_text = f'Текущие очки: {self.current_points}'
            self.total_score_text = f'Счет: {self.total_score}'
            self.label_points['text'] = self.current_points_text
            self.label_score['text'] = self.total_score_text
            self.game_data['current_points'] = self.current_points
            self.game_data['total_score'] = self.total_score
        
        def worker_clicks():
            self.current_points += int(self.workers * self.worker_modifier)
            self.current_points_text = f'Текущие очки: {self.current_points}'
            self.total_score += int(self.workers * self.worker_modifier)
            self.total_score_text = f'Счет: {self.total_score}'
            self.label_score['text'] = self.total_score_text
            self.game_data['total_score'] = self.total_score
            self.game_data['current_points'] = self.current_points
            self.label_points['text'] = self.current_points_text
            self.root.after( 1000, worker_clicks )
        
        def reset_warn():
            self.warn_shown = False
        
        def shop():
            # Checks for shop window and if no results make one.
            if not any(isinstance(x, tk.Toplevel) for x in self.root.winfo_children()):
                self.shop_window = tk.Toplevel( master = self.root )
                self.shop_window.title( 'Clickerino [МАГАЗИН]' )
                self.shop_window.geometry( '400x600' )
                self.shop_window.resizable( False, False )
                
                def shop_handler(command:int):
                    if command == 0:
                        if self.current_points >= self.click_upgrade_cost:
                            self.current_points -= int(self.click_upgrade_cost)
                            self.game_data['current_points'] = self.current_points
                            self.current_points_text = f'Текущие очки: {self.current_points}'
                            self.label_points['text'] = self.current_points_text
                            self.click_upgrade_cost += int(self.click_upgrade_cost * 0.5)
                            self.game_data['click_upgrade_cost'] = self.click_upgrade_cost
                            self.click_upgrade_cost_text = f'Стоимость: {self.click_upgrade_cost}'
                            self.click_upgrade_cost_label['text'] = self.click_upgrade_cost_text
                            self.click_upgrades += 1
                            self.game_data['click_upgrades'] = self.click_upgrades
                            self.click_upgrades_text = f'Улучшения кликов: {self.click_upgrades}'
                            self.click_upgrade_label['text'] = self.click_upgrades_text
                        else:
                            if self.warn_shown == False:
                                messagebox.showwarning( 'ошибка', 'недостаточно очков' )
                                self.warn_shown = True
                                self.root.after(5000, reset_warn)
                    if command == 1:
                        if self.current_points >= self.worker_upgrade_cost:
                            self.current_points -= int(self.worker_upgrade_cost)
                            self.game_data['current_points'] = self.current_points
                            self.current_points_text = f'Текущие очки: {self.current_points}'
                            self.label_points['text'] = self.current_points_text
                            self.worker_upgrade_cost += int(self.worker_upgrade_cost * 0.5)
                            self.game_data['worker_upgrade_cost'] = self.worker_upgrade_cost
                            self.worker_upgrade_cost_text = f'Стоимость: {self.worker_upgrade_cost}'
                            self.worker_upgrade_cost_label['text'] = self.worker_upgrade_cost_text
                            self.workers += 1
                            self.game_data['workers'] = self.workers
                            self.workers_text = f'Количество работников: {self.workers}'
                            self.worker_upgrade_label['text'] = self.workers_text
                            if self.worker_clicking_enabled == False:
                                self.worker_clicking_enabled = True
                                self.root.after( 1000, worker_clicks )
                        else:
                            if self.warn_shown == False:
                                messagebox.showwarning( 'ошибка', 'недостаточно очков' )
                                self.warn_shown = True
                                self.root.after(5000, reset_warn)
                    if command == 2:
                        if self.current_points >= self.click_mod_upgrade_cost:
                            self.current_points -= int(self.click_mod_upgrade_cost)
                            self.game_data['current_points'] = self.current_points
                            self.current_points_text = f'Текущие очки: {self.current_points}'
                            self.label_points['text'] = self.current_points_text
                            self.click_mod_upgrade_cost += int(self.click_mod_upgrade_cost * 0.5)
                            self.game_data['click_mod_upgrade_cost'] = self.click_mod_upgrade_cost
                            self.click_mod_upgrade_cost_text = f'Стоимость: {self.click_mod_upgrade_cost}'
                            self.click_mod_upgrade_cost_label['text'] = self.click_mod_upgrade_cost_text
                            self.click_modifier += 1
                            self.game_data['click_modifier'] = self.click_modifier
                            self.click_modifier_text = f'Модификатор кликов: {self.click_modifier}'
                            self.click_mod_upgrade_label['text'] = self.click_modifier_text
                        else:
                            if self.warn_shown == False:
                                messagebox.showwarning( 'ошибка', 'недостаточно очков' )
                                self.warn_shown = True
                                self.root.after(5000, reset_warn)
                    if command == 3:
                        if self.current_points >= self.worker_mod_upgrade_cost:
                            self.current_points -= int(self.worker_mod_upgrade_cost)
                            self.game_data['current_points'] = self.current_points
                            self.current_points_text = f'Текущие очки: {self.current_points}'
                            self.label_points['text'] = self.current_points_text
                            self.worker_mod_upgrade_cost += int(self.worker_mod_upgrade_cost * 0.5)
                            self.game_data['worker_mod_upgrade_cost'] = self.worker_mod_upgrade_cost
                            self.worker_mod_upgrade_cost_text = f'Стоимость: {self.worker_mod_upgrade_cost}'
                            self.worker_mod_upgrade_cost_label['text'] = self.worker_mod_upgrade_cost_text
                            self.worker_modifier += 1
                            self.game_data['worker_modifier'] = self.worker_modifier
                            self.worker_modifier_text = f'Модификатор работников: {self.worker_modifier}'
                            self.worker_mod_upgrade_label['text'] = self.worker_modifier_text
                        else:
                            if self.warn_shown == False:
                                messagebox.showwarning( 'ошибка', 'недостаточно очков' )
                                self.warn_shown = True
                                self.root.after(5000, reset_warn)
                
                self.click_upgrade_label = tk.Label( master = self.shop_window, text = self.click_upgrades_text )
                self.click_upgrade_label.place( relheight = 0.05, relwidth = 0.4, relx = 0.05, rely = 0.05, anchor='nw')
                self.click_upgrade_cost_label = tk.Label( master = self.shop_window, text = self.click_upgrade_cost_text )
                self.click_upgrade_cost_label.place( relheight = 0.05, relwidth = 0.35, relx = 0.45, rely = 0.05, anchor='nw' )
                self.buy_click_upgrade = tk.Button( master = self.shop_window, text = 'Купить', command = lambda: shop_handler(0) )
                self.buy_click_upgrade.place( relheight = 0.05, relwidth = 0.2, relx = 0.79, rely = 0.05, anchor='nw' )
                
                self.worker_upgrade_label = tk.Label( master = self.shop_window, text = self.workers_text )
                self.worker_upgrade_label.place( relheight = 0.05, relwidth = 0.4, relx = 0.05, rely = 0.1, anchor='nw')
                self.worker_upgrade_cost_label = tk.Label( master = self.shop_window, text = self.worker_upgrade_cost_text )
                self.worker_upgrade_cost_label.place( relheight = 0.05, relwidth = 0.35, relx = 0.45, rely = 0.1, anchor='nw' )
                self.buy_worker_upgrade = tk.Button( master = self.shop_window, text = 'Купить', command = lambda: shop_handler(1) )
                self.buy_worker_upgrade.place( relheight = 0.05, relwidth = 0.2, relx = 0.79, rely = 0.1, anchor='nw' )
                
                self.click_mod_upgrade_label = tk.Label( master = self.shop_window, text = self.click_modifier_text )
                self.click_mod_upgrade_label.place( relheight = 0.05, relwidth = 0.4, relx = 0.05, rely = 0.15, anchor='nw')
                self.click_mod_upgrade_cost_label = tk.Label( master = self.shop_window, text = self.click_mod_upgrade_cost_text )
                self.click_mod_upgrade_cost_label.place( relheight = 0.05, relwidth = 0.35, relx = 0.45, rely = 0.15, anchor='nw' )
                self.buy_click_mod_upgrade = tk.Button( master = self.shop_window, text = 'Купить', command = lambda: shop_handler(2) )
                self.buy_click_mod_upgrade.place( relheight = 0.05, relwidth = 0.2, relx = 0.79, rely = 0.15, anchor='nw' )
                
                self.worker_mod_upgrade_label = tk.Label( master = self.shop_window, text = self.worker_modifier_text )
                self.worker_mod_upgrade_label.place( relheight = 0.05, relwidth = 0.4, relx = 0.05, rely = 0.2, anchor='nw')
                self.worker_mod_upgrade_cost_label = tk.Label( master = self.shop_window, text = self.worker_mod_upgrade_cost_text )
                self.worker_mod_upgrade_cost_label.place( relheight = 0.05, relwidth = 0.35, relx = 0.45, rely = 0.2, anchor='nw' )
                self.buy_worker_mod_upgrade = tk.Button( master = self.shop_window, text = 'Купить', command = lambda: shop_handler(3) )
                self.buy_worker_mod_upgrade.place( relheight = 0.05, relwidth = 0.2, relx = 0.79, rely = 0.2, anchor='nw' )
                
            else:
                pass
        
        self.label_score = tk.Label( master = self.play_scene_frame, text = self.total_score_text )
        self.label_score.place( relheight = 0.05, relwidth = 0.3, relx = 0.1, rely = 0.01, anchor = 'nw' )
        
        self.label_points = tk.Label( master = self.play_scene_frame, text = self.current_points_text )
        self.label_points.place( relheight = 0.05, relwidth = 0.3, relx = 0.5, rely = 0.01, anchor = 'nw' )
        
        self.button_clicker = tk.Label( master = self.play_scene_frame, text = 'жмяк' )
        self.button_clicker.place( relheight = 0.8, relwidth = 0.8, relx = 0.1, rely = 0.1, anchor = 'nw' )
        self.button_clicker.bind( '<Button-1>', click) # XXX: Click handler binds there !
        
        self.button_shop = tk.Button( master = self.play_scene_frame, text = 'магазин', command = shop )
        self.button_shop.place( relheigh = 0.05, relwidth = 0.1, relx = 0.85, rely = 0.035, anchor='nw' )
        
        if self.workers > 0:
            if self.worker_clicking_enabled == False:
                self.worker_clicking_enabled = True
                self.root.after(1000, worker_clicks)


if __name__ == '__main__':
    App()