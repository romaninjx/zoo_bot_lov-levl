import telebot
import random
from animals import list_animal
from config import all_list_answers, text_questions, all_list_photo_questions
from extensions import *


class QuizHandler:
    def __init__(self, call, bot: telebot.TeleBot):
        self.call = call
        self.bot = bot  # Сохраним объект бота как атрибут
        self.you_animal = []
        self.question_index = 0
        self.flag_index = 0
        self.copy_you_animal = []
        self.base = []
        self.foods_flag = None
        self.habitat_flag = None
        self.list_cities_flag = None
        self.sms_no_photo = False
        self.stop = False
        self.selection_list = []
        self.randomz = False
        self.save_num = []

    def reset_quiz(self):
        """Сбрасывает состояние викторины."""
        a = len(all_list_answers)
        b = len(allInfo_about_buttons)
        c = len(text_questions)
        if a > 6:
            for i in range(a, 6, -1):
                all_list_answers.pop(i-1)
        if b > 6:
            for i in range(a, 6, -1):
                allInfo_about_buttons.pop(i-1)
        if c > 6:
            for i in range(a, 6, -1):
                text_questions.pop(i-1)
        self.you_animal.clear()
        self.selection_list.clear()

    def send_question(self):
        """Отправляет вопрос с кнопками и фото."""
        print("Индекс перед отправкой смс", self.question_index)
        print(f'количесто доступа количеста ответов {len(all_list_answers)}, текст сообщения {len(text_questions)}\
 количесто фоток {len(all_list_photo_questions)}')
        if (self.question_index >= len(all_list_answers) or
                self.question_index >= len(text_questions) or
                self.question_index >= len(all_list_photo_questions)):
            self.finalize_quiz()


        print("Попытка отправить вопрос...")  # Логируем
        keyboard = creating_buttons_questions(len(all_list_answers[self.question_index]),
                                              all_list_answers[self.question_index],
                                              allInfo_about_buttons[self.question_index]).return_buttons()

        chat_id = self.call.message.chat.id if hasattr(self.call, 'message') else self.call.from_user.id

        if len(self.selection_list) == 2:
            if self.selection_list[0] == 'стадное':
                photo = all_list_photo_questions[2][0]
            else:
                photo = all_list_photo_questions[2][1]

        elif len(self.selection_list) >= 3 and not self.sms_no_photo:
            if self.selection_list[0] == allInfo_about_buttons[self.question_index - 1][0]:
                photo = all_list_photo_questions[self.question_index][0]
            elif self.selection_list[0] == allInfo_about_buttons[self.question_index - 1][1]:
                photo = all_list_photo_questions[self.question_index][1]
            elif self.selection_list[0] == allInfo_about_buttons[self.question_index - 1][2]:
                photo = all_list_photo_questions[self.question_index][2]

        else:
            if self.stop == False:
                photo = all_list_photo_questions[self.question_index]
        if self.stop == False:
                if photo is not None:
                    print(f"Отправка фото: {photo}, ID чата: {chat_id}")  # Логируем
                else:
                    print("Не удалось получить изображение для отправки.")
                    return  # Возвращаемся, если photo не инициализирована
        try:

            if self.stop == False:
                if self.sms_no_photo == False:
                    self.bot.send_photo(chat_id=chat_id,
                                        caption=text_questions[self.question_index],
                                        reply_markup=keyboard,
                                        photo=photo)
                elif self.question_index == 11:
                    self.bot.send_message(chat_id=chat_id, text=text_questions[self.question_index])
                    self.process_response(self.save_num)
                else:
                    if self.sms_no_photo:
                        self.bot.send_message(chat_id=chat_id, text=text_questions[self.question_index],
                                              reply_markup=keyboard)
                        self.sms_no_photo = False

        except Exception as e:
            print(f"Ошибка при отправке фото: {e}")  # Логируем ошибку
            self.bot.send_message(chat_id, f"Ошибка при отправке фото: {e}")

    def handle_response(self, response: str):
        """Обрабатывает ответ пользователя на вопрос."""
        try:
            if (self.question_index >= len(all_list_answers) or
                    self.question_index >= len(text_questions) or
                    self.question_index >= len(all_list_photo_questions)):
                self.finalize_quiz()
                return
            print('индекс за  кодом', self.question_index)
            if self.stop == False:
                self.selection_list.insert(0, response)
                checking_users_activity(self.selection_list, self.question_index)
                self.process_response(response)
                print('индекс внутри кода', self.question_index)

        except APIException as e:
            chat_id = self.call.message.chat.id if hasattr(self.call, 'message') else self.call.from_user.id
            self.bot.send_message(chat_id, f"{e}")
        except Exception as e:
            chat_id = self.call.message.chat.id if hasattr(self.call, 'message') else self.call.from_user.id
            self.bot.send_message(chat_id, f'Не удалось обработать запрос:\n{e}')

    def process_response(self, response):
        """Логика обработки ответа на вопрос."""
        new_you_animal = []
        print(self.question_index)
        if self.question_index == 1:  # Обрабатываем первый вопрос
            if response == allInfo_about_buttons[1][0]:  # Стадное
                self.you_animal = [animal for animal in list_animal if animal.flock]
            elif response == allInfo_about_buttons[1][1]:  # Не стадное
                self.you_animal = [animal for animal in list_animal if not animal.flock]

        elif self.question_index == 0:  # не обрабатываем кнопку да
            pass

        elif self.question_index == 2:  # Обрабатываем второй вопрос

            if response == allInfo_about_buttons[2][0]:  # Дневные
                self.you_animal = [animal for animal in self.you_animal if animal.lifestyle == 'дневной']
            elif response == allInfo_about_buttons[2][1]:  # Ночные
                self.you_animal = [animal for animal in self.you_animal if animal.lifestyle == 'ночной']
            elif response == allInfo_about_buttons[2][2]:  # Всегда активен
                self.you_animal = [animal for animal in self.you_animal if animal.lifestyle == 'всегда активен']

        elif self.question_index == 3:  # Обрабатываем третий вопрос

            if response == "Тепло и укрытие":  # тепло
                self.you_animal = [animal for animal in self.you_animal if animal.survival_factor == "Тепло и укрытие"]
            elif response == "голодание, засухоустойчивость":  # засуха
                self.you_animal = [animal for animal in self.you_animal if
                                   animal.survival_factor == "голодание, засухоустойчивость"]
            elif response == "Влажная среда и близость воды":  # влажная среда
                self.you_animal = [animal for animal in self.you_animal if
                                   animal.survival_factor == "Влажная среда и близость воды"]

        elif self.question_index == 4:  # Обрабатываем четвёртый вопрос

            if response == 'большой':  # Первая опция
                self.you_animal = [animal for animal in self.you_animal if animal.size == 'большой']
            elif response == 'маленький':  # Вторая опция
                self.you_animal = [animal for animal in self.you_animal if animal.size == 'маленький']
            elif response == 'средний':  # Третья опция
                self.you_animal = [animal for animal in self.you_animal if animal.size == 'средний']

        elif self.question_index == 5:  # Обрабатываем пятый вопрос

            if response == 'Птицы':  # Первая опция
                self.you_animal = [animal for animal in self.you_animal if animal.class_ == 'Птицы']
            elif response == allInfo_about_buttons[5][1]:  # Вторая опция
                self.you_animal = [animal for animal in self.you_animal if
                                   (animal.class_ == 'Рептилии') and (animal.class_ == 'Амфибии')]
            elif response == allInfo_about_buttons[5][2]:  # Третья опция
                self.you_animal = [animal for animal in self.you_animal if animal.class_ == 'Млекопитающие']



        elif self.question_index == 6:
            self.save_num = response

        elif self.question_index == 10:
            for animal in self.you_animal:
                if animal.name_animal == self.save_num:
                    new_you_animal.append(animal)
                    self.you_animal = new_you_animal.copy()

                else:
                    self.you_animal = []
        elif 10 > self.question_index > 6 or self.question_index == 11:
            for animal in self.you_animal:
                if (response in animal.food or response in animal.habitat or response in animal.list_cities
                        or response in animal.name_animal):
                    new_you_animal.append(animal)
            self.you_animal = new_you_animal.copy()



        print(f'сохранённые числа:', self.save_num)
        print(len(self.you_animal), [animal.name_animal for animal in self.you_animal])
        print(self.selection_list)
        if len(self.you_animal) != 0:
            self.base = self.you_animal.copy()
        self.question_index += 1
        print("base ", len(self.base), [animal.name_animal for animal in self.base])
        print("копия животных", len(self.copy_you_animal), self.copy_you_animal)
        self.flag_index += 1        # возможно вернуть вниз
        self.finalize_quiz()
        self.send_question()


    def finalize_quiz(self):
        """Завершает викторину и выводит результат."""
        if len(self.you_animal) == 1:
            self.selection_list.insert(0, 'конец')
            self.stop = True
            self.selection_list.insert(0, [animal.name_animal for animal in self.you_animal])
            result_message = f"Ваше тотемное животное: {', '.join([animal.name_animal for animal in self.you_animal])}"
            chat_id = self.call.message.chat.id if hasattr(self.call, 'message') else self.call.from_user.id
            self.bot.send_message(chat_id, result_message)
            message_itog = f'{self.you_animal[0].name_animal} {self.you_animal[0].description}\n'
            self.bot.send_photo(chat_id=chat_id, photo=self.you_animal[0].image, caption=message_itog)
            guardianship = 'Вы можете взять этого \
зверька под опеку!)\nкак это? А вот как)\n\nУ нас есть проект «Возьми животное под опеку» («Клуб друзей») — это одна из \
программ, помогающих зоопарку заботиться о его обитателях. Программа позволяет с помощью пожертвования на любую сумму \
внести свой вклад в развитие зоопарка и сохранение биоразнообразия планеты.\n\nУчастником программы может стать любой \
неравнодушный: и ребёнок, и большая корпорация. Поддержка опекунов помогает зоопарку улучшать условия для животных и \
повышать уровень их благополучия.\nВзять под опеку можно разных обитателей зоопарка, например, слона, льва, суриката \
или фламинго. Это возможность помочь любимому животному или даже реализовать детскую мечту подружиться с настоящим \
диким зверем. \n\nПочётный статус опекуна позволяет круглый год навещать подопечного, быть в курсе событий его жизни и \
самочувствия)\n\nЧтобы по больше узнать о проекте нажми сюда:«/guardianship» а если хотите пройти викторин занава то \
жмите «/start»'
            #keybord = creating_buttons_questions(1, ["Попробовать ещё раз?"], ['start']).return_buttons()

            #self.bot.send_message(chat_id, text=guardianship, reply_markup=keybord)
            print(self.selection_list)

        if len(self.you_animal) == 0 and self.flag_index > 0:
            print("КУКУ ЖИВОТНЫХ НЕТ\nпроизводим востановление")
            self.you_animal = self.base.copy()
            print("животные востановленны:")
            print(len(self.you_animal), [animal.name_animal for animal in self.you_animal])
        quest_index = [i for i in range(6, 100)] #if i % 3 == 0]
        if self.flag_index in quest_index:
            self.create_question_and_buttons()



    def unique_sets(self):
        """ Проверяет уникальность параметров между животными """


        # Проверка уникальности food
        food_sets = [set(animal.food) for animal in self.you_animal]
        if not all(food_set == food_sets[0] for food_set in food_sets):
            self.foods_flag = False
            return self.foods_flag

        # Проверка уникальности habitat
        habitat_sets = [set(animal.habitat) for animal in self.you_animal]
        if not all(habitat_set == habitat_sets[0] for habitat_set in habitat_sets):
            self.habitat_flag = False
            return self.habitat_flag

        # Проверка уникальности list_cities
        cities_sets = [set(animal.list_cities) for animal in self.you_animal]
        if not all(cities_set == cities_sets[0] for cities_set in cities_sets):
            self.list_cities_flag = False
            return self.list_cities_flag

        return True

    def create_question_and_buttons(self):
        if self.question_index == 11:
            question = "Момент"
            text_questions.insert(11, question)
            allInfo_about_buttons.insert(11, ["s"])
            all_list_answers.insert(11, ["s"])

        if  self.question_index == 6 or self.question_index >= 10:
            print("выберите любое число", [animal.name_animal for animal in self.you_animal])
            question = "Выберете любое понравившееся вам число"
            text_questions.append(question)
            allInfo_about_buttons.append([animal.name_animal for animal in self.you_animal])
            all_list_answers.append([str(random.randint(0, 100)) for i in range(len(self.you_animal))])
            self.sms_no_photo = True


        # Генерация вопросов на основе food
        food_set = {food for animal in self.you_animal for food in animal.food}
        if self.question_index == 7:
            question = "Представьте что у вас появится домашний зверёк, чем бы он питался?"
            buttons = list(food_set)
            text_questions.append(question)
            allInfo_about_buttons.append(buttons)
            all_list_answers.append(buttons)

        # Генерация вопросов на основе habitat
        habitat_set = {habitat for animal in self.you_animal for habitat in animal.habitat}
        if self.question_index == 8:
            question = "Если бы вы могли выбрать, где бы вы хотели жить?"
            buttons = list(habitat_set)
            text_questions.append(question)
            allInfo_about_buttons.append(buttons)
            all_list_answers.append(buttons)

        # Генерация вопросов на основе list_cities
        cities_set = {city for animal in self.you_animal for city in animal.list_cities}
        if self.question_index == 9:
            question = "Из данного выбора вы бы где хотели побывать?"
            buttons = list(cities_set)
            text_questions.append(question)
            allInfo_about_buttons.append(buttons)
            all_list_answers.append(buttons)


