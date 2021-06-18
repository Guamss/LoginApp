from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
import mysql.connector

cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="gamedata"
    )
mycursor = cnx.cursor()

class LoginApp(Widget):
    username = ObjectProperty(None)
    password = ObjectProperty(None)
    
    def btn(self):
        username = self.username.text
        password = self.password.text
        mycursor.execute("SELECT * FROM User")
        users = mycursor.fetchall()
        print(f"username : {username} password : {password}")
        for user in users:
            if username == user[0] and password == user[1]:
                self.username.text = ""
                self.password.text = ""
           
class MyApp(App):
    def build(self):
        return LoginApp()
    
MyApp().run()