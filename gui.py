##FIKA APP GUI made with Kivy 

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.config import Config
from kivy.app import App
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout

class ATTAFika(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6,0.9)
        self.window.pos_hint = {"center_x": 0.5, "center_y":0.5}
        self.icon = 'AttaLogo.ico'
        self.title = 'ATTA Fika v0.0.1'
       

        #Header Image
        self.window.add_widget(Image(source="header.png",size_hint = (1.5,1.5)))

        # #Generate Pairings Button
        # self.button = Button(text="Generate Pairings", size_hint = (1,0.5))
        # self.button.bind(on_press=self.callback)
        # self.window.add_widget(self.button)

        self.welcome = Label(text="This Week's Pairings:")
        self.window.add_widget(self.welcome)

        layout = GridLayout(cols=1, padding=5, spacing=5,
                size_hint=(None, None), width=500)

        # when we add children to the grid layout, its size doesn't change at
        # all. we need to ensure that the height will be the minimum required
        # to contain all the childs. (otherwise, we'll child outside the
        # bounding box of the childs)
        layout.bind(minimum_height=layout.setter('height'))

        # add button into that grid
        for i in range(30):
            btn = Button(text="person" + str(i) + "@attabotics.com + " + "person" + str(i+20) + "@attabotics.com", size=(580, 40),
                         size_hint=(None, None))
            layout.add_widget(btn)

        # create a scroll view, with a size < size of the grid
        list = ScrollView(size_hint=(None, None), size=(600, 200),
                pos_hint={'center_x': .5, 'center_y': .5}, do_scroll_x=False)
        list.add_widget(layout)

        self.window.add_widget(list)
    
        #Generate Pairings Button
        self.button2 = Button(text="Send Email Invite To Pairings", size_hint = (1,0.5))
        self.button2.bind(on_press=self.callback)
        self.window.add_widget(self.button2)

        #Set window size
        Config.set('graphics', 'width', '1000')
        Config.set('graphics', 'height', '750')
        Config.set('graphics', 'resizable', False)
        Config.write()

        return self.window


    def callback(self, instance):
        self.welcome.text = "Emails SENT"
        

if __name__ == "__main__":
    ATTAFika().run()