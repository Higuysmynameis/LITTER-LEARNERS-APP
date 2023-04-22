from kivy.lang import Builder
from kivymd.app import MDApp
import mysql.connector
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import ObjectProperty


class FirstScreen(Screen):
    pass


class MenuScreen(Screen):
    email = ObjectProperty(None)
    trash = ObjectProperty(None)
    user = ObjectProperty(None)
    start = ObjectProperty(None)
    database = mysql.connector.Connect(host="localhost", user="root", password="Ransana@2008", database="loginform")6
    cursor = database.cursor()
    cursor.execute("select * from logindata")
    for i in cursor.fetchall():
        print(i[0], i[1], i[2])

    # def logger(self):
    #     self.start.text = f'Welcome {self.user.text}'

    def clear(self):
        self.start.text = "Beatification And Gamification"
        self.user.text = ""
        self.trash.text = ""
        self.email.text = ""

    def send_data(self, email, user, trash):
        self.cursor.execute(f"insert into logindata values('{email.text}', '{user.text}', '{trash.text}')")
        self.database.commit()


class ProfileScreen(Screen):
    pass


class SecondScreen(Screen):
    pass


# sm = ScreenManager()
# sm.add_widget(MenuScreen(name='menu'))
# sm.add_widget(ProfileScreen(name='profile'))


sm = ScreenManager()
sm.add_widget(FirstScreen(name='info'))
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(ProfileScreen(name='profile'))


class MainApp(MDApp):
    def build(self):
        self.title = "Beatification and Gamification"
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file("tt.kv")
    #
    # def logger(self):
    #     self.root.ids.start.text = f'Welcome {self.root.ids.user.text}'
    #
    # def clear(self):
    #     self.root.ids.start.text = "Beatification And Gamification"
    #     self.root.ids.user.text = ""
    #     self.root.ids.trash.text = ""
    #     self.root.ids.email.text = ""
    #
    # def send_data(self, email, user, trash):
    #     self.cursor.execute(f"insert into logindata values('{email.text}', '{user.text}', '{trash.text}')")
    #     self.database.commit()


MainApp().run()
