from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty


class userInterFace(BoxLayout):
    result = StringProperty("0")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.input_value = " "

    def on_press_button(self, instance):
        if instance.text == "=":
            try:
                self.result = str(eval(self.input_value))
            except Exception as e:
                self.result = "Error occured"
        elif instance.text == "AC":
            self.input_value = ""
            self.result = "0"
        else:
            self.input_value += instance.text
            self.result = self.input_value


class FatihamCalculator(App):
    pass


if __name__ == "__main__":
    FatihamCalculator().run()
