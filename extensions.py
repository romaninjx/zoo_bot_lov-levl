from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import allInfo_about_buttons


class creating_buttons_questions:
    """Класс создаёт заданное количество кнопок для клавиатуры с определёнными параметрами.
    Функция «return_buttons» возвращает готовую клавиатуру."""

    def __init__(self, quantity_buttons: int, list_names_buttons: list, info_about_buttons: list):
        # Количество кнопок; лист с именами кнопок; информация, содержащаяся в кнопке.

        self.keyboard = InlineKeyboardMarkup()  # создаём клавиатуру (оболочка) пустая клавиатура

        # Создаём по отдельности кнопки и добавляем их в клавиатуру
        for number_button in range(quantity_buttons):
            button = InlineKeyboardButton(text=list_names_buttons[number_button],
                                          callback_data=info_about_buttons[number_button][:64])

            self.keyboard.add(button)

    def return_buttons(self):
        """Функция «return_buttons» возвращает готовую клавиатуру."""

        return self.keyboard


class APIException(Exception):   # Класс для обозначения ошибок на стороне пользователя
    """Этот клас нужен для отловли ошибок, которые мог совершить пользователь"""
    pass


def checking_users_activity(list, index):
    if list[0] == allInfo_about_buttons[0][0] and list.count(allInfo_about_buttons[0][0]) == 2:
        list.pop(0)
        raise APIException('Извините, но вы уже начали викторину🙃\nЕсли хотите начать заново, просто нажмите: \
«/start» или напишите мне эту команду в чат😁')

    answers = ['первый', 'второй', 'третий', 'четвёртый', "пятый", "шестой", "седьмой", "восьмой", "девятый", "десятый",
               "одиннадцатый", "двенадцатый", "тринадцатый"]
    if index < 10:
        for i in range(1, 15):
            if (len(list) > i+1) and (list[0] in allInfo_about_buttons[i]):
                list.pop(0)
                raise APIException(f'Извините но вы уже ответили на {answers[i-1]} вопрос🙃\nЕсли хотите начать заново\
, просто нажмите: «/start» или напишите мне эту команду в чат😁')

    if "конец" in list:
        list.remove("конец")
        raise APIException(f'Извините но вы уже закончили викторину🙃 \nЕсли хотите начать заново, просто нажмите: \
«/start» или напишите мне эту команду в чат😁')










