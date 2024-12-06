import telebot

from config import TOKEN
from quiz_handler import QuizHandler

bot = telebot.TeleBot(TOKEN)
quiz_handlers = {}      # id пользователей


@bot.message_handler(commands=['start'])
def start(message: telebot.types.Message):
    user_id = message.from_user.id
    quiz_handlers[user_id] = QuizHandler(message, bot)
    quiz_handlers[user_id].reset_quiz()
    quiz_handlers[user_id].send_question()


@bot.callback_query_handler(func=lambda call: True)  # Единый обработчик для всех обратных вызовов
def handle_quiz_response(call):
    user_id = call.from_user.id
    try:
        quiz_handlers[user_id].handle_response(call.data)

    except KeyError:
        print(f"пользователь {user_id} не найден в quiz_handlers.")
        bot.answer_callback_query(call.id, text="Произошла ошибка. Пожалуйста, перезапустите тест.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        bot.answer_callback_query(call.id, text="Произошла ошибка. Пожалуйста, перезапустите тест.")

@bot.message_handler(commands=['guardianship'])
def guardianship(message: telebot.types.Message):
    text = ('ознакомится с программой «[Возьми животное под опеку]» можно нажав на ссылку:\
https://moscowzoo.ru/my-zoo/become-a-guardian/')
    bot.send_message(message.chat.id, text, parse_mode='Markdown')

#@bot.callback_query_handler(func=lambda call: call.data == 'restart')
#def restart_handler(call):
    #user_id = call.from_user.id
    #quiz_handlers[user_id] = QuizHandler(user_id, bot)
    #quiz_handlers[user_id].reset_quiz()
    #quiz_handlers[user_id].send_question()


bot.polling()

