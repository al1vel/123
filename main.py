import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

kivy.require('1.9.0')

MAINLINE = ""


class MainPage(GridLayout):

    def __init__(self, **kwargs):
        super(MainPage, self).__init__(**kwargs)
        self.cols = 1

        self.label1 = Label(text="0")
        self.add_widget(self.label1)

        self.buttonsPanel = GridLayout()
        self.buttonsPanel.cols = 4

        self.b_one = Button(text="1", font_size=30)
        self.b_one.bind(on_press=self.b_one_pressed)
        self.buttonsPanel.add_widget(self.b_one)

        self.b_two = Button(text="2", font_size=30)
        self.b_two.bind(on_press=self.b_two_pressed)
        self.buttonsPanel.add_widget(self.b_two)

        self.b_three = Button(text="3", font_size=30)
        self.b_three.bind(on_press=self.b_three_pressed)
        self.buttonsPanel.add_widget(self.b_three)

        self.b_clear = Button(text="C", font_size=30)
        self.b_clear.bind(on_press=self.b_clear_pressed)
        self.buttonsPanel.add_widget(self.b_clear)

        self.b_four = Button(text="4", font_size=30)
        self.b_four.bind(on_press=self.b_four_pressed)
        self.buttonsPanel.add_widget(self.b_four)

        self.b_five = Button(text="5", font_size=30)
        self.b_five.bind(on_press=self.b_five_pressed)
        self.buttonsPanel.add_widget(self.b_five)

        self.b_six = Button(text="6", font_size=30)
        self.b_six.bind(on_press=self.b_six_pressed)
        self.buttonsPanel.add_widget(self.b_six)

        self.b_plus = Button(text="+", font_size=30)
        self.b_plus.bind(on_press=self.b_plus_pressed)
        self.buttonsPanel.add_widget(self.b_plus)

        self.b_seven = Button(text="7", font_size=30)
        self.b_seven.bind(on_press=self.b_seven_pressed)
        self.buttonsPanel.add_widget(self.b_seven)

        self.b_eight = Button(text="8", font_size=30)
        self.b_eight.bind(on_press=self.b_eight_pressed)
        self.buttonsPanel.add_widget(self.b_eight)

        self.b_nine = Button(text="9", font_size=30)
        self.b_nine.bind(on_press=self.b_nine_pressed)
        self.buttonsPanel.add_widget(self.b_nine)

        self.b_minus = Button(text="-", font_size=30)
        self.b_minus.bind(on_press=self.b_minus_pressed)
        self.buttonsPanel.add_widget(self.b_minus)

        self.b_times = Button(text="*", font_size=30)
        self.b_times.bind(on_press=self.b_times_pressed)
        self.buttonsPanel.add_widget(self.b_times)

        self.b_zero = Button(text="0", font_size=30)
        self.b_zero.bind(on_press=self.b_zero_pressed)
        self.buttonsPanel.add_widget(self.b_zero)

        self.b_division = Button(text="/", font_size=30)
        self.b_division.bind(on_press=self.b_division_pressed)
        self.buttonsPanel.add_widget(self.b_division)

        self.b_result = Button(text="=", font_size=30)
        self.b_result.bind(on_press=self.b_result_pressed)
        self.buttonsPanel.add_widget(self.b_result)

        self.add_widget(self.buttonsPanel)

    def b_one_pressed(self, instance):
        global MAINLINE
        MAINLINE += "1"
        self.label1.text = MAINLINE

    def b_two_pressed(self, instance):
        global MAINLINE
        MAINLINE += "2"
        self.label1.text = MAINLINE

    def b_three_pressed(self, instance):
        global MAINLINE
        MAINLINE += "3"
        self.label1.text = MAINLINE

    def b_four_pressed(self, instance):
        global MAINLINE
        MAINLINE += "4"
        self.label1.text = MAINLINE

    def b_five_pressed(self, instance):
        global MAINLINE
        MAINLINE += "5"
        self.label1.text = MAINLINE

    def b_six_pressed(self, instance):
        global MAINLINE
        MAINLINE += "6"
        self.label1.text = MAINLINE

    def b_seven_pressed(self, instance):
        global MAINLINE
        MAINLINE += "7"
        self.label1.text = MAINLINE

    def b_eight_pressed(self, instance):
        global MAINLINE
        MAINLINE += "8"
        self.label1.text = MAINLINE

    def b_nine_pressed(self, instance):
        global MAINLINE
        MAINLINE += "9"
        self.label1.text = MAINLINE

    def b_zero_pressed(self, instance):
        global MAINLINE
        MAINLINE += "0"
        self.label1.text = MAINLINE

    def b_plus_pressed(self, instance):
        global MAINLINE
        MAINLINE += "+"
        self.label1.text = MAINLINE

    def b_minus_pressed(self, instance):
        global MAINLINE
        MAINLINE += "-"
        self.label1.text = MAINLINE

    def b_times_pressed(self, instance):
        global MAINLINE
        MAINLINE += "*"
        self.label1.text = MAINLINE

    def b_division_pressed(self, instance):
        global MAINLINE
        MAINLINE += "/"
        self.label1.text = MAINLINE

    def b_clear_pressed(self, instance):
        global MAINLINE
        MAINLINE = ""
        self.label1.text = MAINLINE

    def b_result_pressed(self, instance):
        global MAINLINE
        if "+" in MAINLINE:
            numbers = MAINLINE.split("+")
            result = int(numbers[0]) + int(numbers[1])
            self.label1.text = str(result)
        elif "-" in MAINLINE:
            numbers = MAINLINE.split("-")
            result = int(numbers[0]) - int(numbers[1])
            self.label1.text = str(result)
        elif "*" in MAINLINE:
            numbers = MAINLINE.split("*")
            result = int(numbers[0]) * int(numbers[1])
            self.label1.text = str(result)
        elif "/" in MAINLINE:
            numbers = MAINLINE.split("/")
            if numbers[1] == "0":
                self.label1.text = "DIVISION BY ZERO IS UNREAL, SORRY :("
            else:
                result = int(numbers[0]) / int(numbers[1])
                self.label1.text = str(result)
        else:
            self.label1.text = "INCORRECT EQUATION"


class CalcApp(App):
    def build(self):
        return MainPage()


if __name__ == "__main__":
    CalcApp().run()
