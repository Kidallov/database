from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
class HelloWidget(BoxLayout):
    hello_label = ObjectProperty()
    name_input = ObjectProperty()
    def say_hello(self):
        if self.name_input.text == "":
           self.hello_label.text = 'Привет!'
        else:
           self.hello_label.text = 'Привет, ' + self.name_input.text + "!"
class HelloApp(App):
    def build(self):
        return HelloWidget()
if __name__ == '__main__':
    app = HelloApp()
    app.run()
