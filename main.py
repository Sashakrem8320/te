from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        self.label = Label(text="Введите текст:")
        layout.add_widget(self.label)

        self.text_input = TextInput(multiline=False)
        layout.add_widget(self.text_input)

        button = Button(text="Нажми меня!")
        button.bind(on_press=self.update_label)
        layout.add_widget(button)

        return layout

    def update_label(self, instance):
        self.label.text = f"Вы ввели: {self.text_input.text}"

if __name__ == '__main__':
    MyApp().run()
