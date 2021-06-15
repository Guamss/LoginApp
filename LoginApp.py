from kivy.app import App
from kivy.config import Config
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
import mysql.connector
from mysql.connector import cursor

cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="gamedata"
    )
mycursor = cnx.cursor()

class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        
        self.cols = 1
        
        self.inside= GridLayout()
        self.inside.cols = 2
        self.title = "Login"
        
        self.inside.add_widget(Label(text="Username :", font_size="60px"))
        self.username = TextInput(multiline=False)
        self.inside.add_widget(self.username)

        self.inside.add_widget(Label(text="Password :", font_size="60px"))
        self.password = TextInput(multiline=False)
        self.inside.add_widget(self.password)
        
        self.add_widget(self.inside)
        
        self.login = Button(text="Login", font_size="60px")
        self.login.bind(on_press=self.pressed)
        self.add_widget(self.login)
        self.contentpopup = Button(text="Close popup")
        self.error = Popup(title="Error ! It seems you spelled something wrong...",
            content=self.contentpopup)
        self.contentpopup.bind(on_press=self.error.dismiss)
        
    def pressed(self, instance):
        username = self.username.text
        password = self.password.text
        mycursor.execute("SELECT * FROM User")
        users = mycursor.fetchall()
        #BOULE FOR NON COMPLETE ! UNIQUEMENT LE IF MARCHE LE ELIF
        #N'EST PAS ENCORE FINIT ! (Uniquement une connexion avec les 
        #bons identifiants est fonctionnelle)
        for user in users:
            if username == user[0] and password == user[1]:
                print("Vous êtes connecté!")
                self.username.text = ""
                self.password.text = ""
            elif username != user[0] and password != user[1]:
                self.error.open()
            
        
           
class LoginApp(App):
    def build(self):
        return MyGrid()

Config.set("graphics", "width", 700)
Config.set("graphics", "height", 720)
    
LoginApp().run()