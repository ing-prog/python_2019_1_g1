from kivy.app import App  # Импортирует главный класс для запуска формы
# from kivy.uix.label import Label  # Импортирует поле вывода текста(Label)
from kivy.uix.button import Button  # Импортирует кнопку


class MyFirstApp(App):  # Создает форму для приложения

    # Функция, которая запускается при нажатии на кнопку
    def clik(self, args):
        self.button.text = str(int(self.button.text) + 1)  # увеличивает значение функции на единицу

    # Запускает приложения и методы(функции в форме)
    def build(self):  
        self.button = Button(text="0",  # Текст внутри виджета
                             font_size=54,  # Размер шрифта
                             background_color=[0.1, 0.8, 0.1, 1],  # Цвет фона
                             on_press=self.clik)  # Какую функцию запустить при нажатии на кнопку. В данном случае clik
        return self.button


# Запускаем приложение
MyFirstApp().run()

# Проблема в том, что не можем сразу два виджета вернуть