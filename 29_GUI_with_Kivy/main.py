from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout

class AddLocationForm(BoxLayout):
    search_input = ObjectProperty()
    def search_location(self):
        print("The user searched for '{}'".format(self.search_input.text))
        self.search_results.item_strings = [self.search_input.text]

class WeatherApp(App):
    pass

if __name__ == '__main__':
    WeatherApp().run()
