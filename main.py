'''
@Description:
@Date: 2019-12-10 21:49:31
@Author: I-Hsien
@LastEditors: I-Hsien
@LastEditTime: 2019-12-10 21:59:23
'''
from kivy.app import App
from kivy.uix.button import Button

class TestApp(App):
    def build(self):
        return Button(text='Hello World')

TestApp().run()