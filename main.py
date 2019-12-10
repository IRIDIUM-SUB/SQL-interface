'''
@Description:
@Date: 2019-12-10 21:49:31
@Author: I-Hsien
@LastEditors: I-Hsien
@LastEditTime: 2019-12-11 00:20:52
'''
from kivy.app import App
from kivy.config import Config
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.image import AsyncImage
Builder.load_file('layout.kv')
class ScreenManager(ScreenManager):
    pass

class HomeScreen(Screen):
    pass

class LoginScreen(Screen):
    pass

class TestApp(App):
    def build(self):
        #Config.set('graphics', 'width', '200')
        #Config.set('graphics', 'height', '200')#Remove in mobile?
        return ScreenManager()

TestApp().run()
