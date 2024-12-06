TOKEN = '7175559415:AAFfxfwi9OmAKykkv1faAF93OXpdBpjhQy0'


# Текст вопросов:


question0 = 'Привет! 🐾 \nВы находитесь в Телеграм-боте Московского зоопарка. \
Мы приглашаем вас пройти увлекательную викторину, чтобы узнать, какое у вас тотемное животное. \
Это увлекательное путешествие поможет вам лучше понять свои качества и особенности!\nГотовы начать? \
Просто нажмите кнопку "Да", и мы начнем!'
question1 = "Как вы относитесь к ситуации, когда вам нужно провести время наедине?"
question2 = "Когда вы чувствуете себя наиболее энергичным и живым?"
question3 = "Представьте, что у вас есть на выбор три суперспособности. Какую бы вы выбрали?"
question4 = "Если бы вы могли выбрать один из этих видов архитектуры для \
строительства своего дома, что бы вы предпочли?"
question5 = "Представьте, что вы заядлый путешественник. Как бы вы хотели путешествовать?"

text_questions = [value for key, value in globals().items() if key.startswith('question')]                                         #глобальный параметр
print(text_questions)


# Кнопки:


list_answer0 = ["Да, начинаем😃"]

answer1_1 = "Я предпочитаю быть в компании друзей или семьи"
answer1_2 = "Это прекрасно, я наслаждаюсь своим уединением"
list_answer1 = [answer1_1, answer1_2]

answer2_1 = "Когда солнце светит, и вы можете провести время на улице."
answer2_2 = "Ночью, когда город наполняется огнями и звуками."
answer2_3 = "В состоянии полного покоя, когда никто не отвлекает."
list_answer2 = [answer2_1, answer2_2, answer2_3]

answer3_1 = "Никогда не мёрзнуть, но и не греться"
answer3_2 = "длительное время обходиться без еды и воды"
answer3_3 = "Адаптироваться к любым водным условиям"
list_answer3 = [answer3_1, answer3_2, answer3_3]

answer4_1 = "Величественный замок с высокими башнями и просторными залами, \
где можно разместить множество гостей."
answer4_2 = "Уютный домик с маленькими окошками и садиком, в котором можно \
проводить время в тишине и спокойствии."
answer4_3 = "Современный лофт с высокими потолками и открытым пространством, \
где можно реализовать любые творческие идеи."
list_answer4 = [answer4_1, answer4_2, answer4_3]

answer5_1 = "На самолёте)"
answer5_2 = "На корабле"
answer5_3 = "На машине или пешком"
list_answer5 = [answer5_1, answer5_2, answer5_3]

all_list_answers = [value for key, value in globals().items() if key.startswith('list_answer')]                                         #глобальный параметр
print(all_list_answers)


# фотографии:


list_photo_question0 = "https://avatars.mds.yandex.net/i?id=c01f217a6f\
10e87d19b5eb00d2d43321_l-5236639-images-thumbs&n=13"

list_photo_question1 = "https://cdnn21.img.ria.ru/images/07e4/0c/0b/1588855032_0:32:2900:1663_1920x\
0_80_0_0_3012f27285d42fc14e812bccdbfd30c9.jpg"

photo1_question2 = "https://sun9-41.userapi.com/impf/-7SOdpi_PevPbjWFFe2bsTGXv8soYc\
cm2Cw_zA/7rXENx_iF-w.jpg?size=945x614&quality=96&sign=e108d91e38fdcae68458842d5a8dfe\
4c&c_uniq_tag=I5u5Qs4ZqdQ_iDllwegfHG_Ld7Jo5xW_a4IZ9skok00&type=album"
photo2_question2 = "https://dl-asset.cyberlink.com/web/prog/learning-center/html/10049/PDR19-YouTube\
-72_The_Best_Photo_Editing_Software/img/couleur1.jpg"
list_photo_question2 = [photo1_question2, photo2_question2]

photo_variable1_1 = "https://images.prismic.io/incriveisexperiencias/8057e849-4aba-4619-908e-f8f7d\
5bb14d0_fun.jpg?auto=format%2Ccompress&amp;max-w=1600&amp;max-h=838&amp;fit=crop&amp;crop=faces&amp;ar=1.91&amp;tri\
m=auto&amp;ixlib=react-9.0.2"         # день стадо
photo_variable2_1 = "https://i.pinimg.com/originals/b2/62/b6/b262b605c47d5e02f18763591489355f.jpg"
photo_variable2_2 = "https://images.hdqwalls.com/download/cameraman-silhouette-rl-3840x2400.jpg"
list_photo_question3 = [photo_variable1_1, photo_variable2_1, photo_variable2_2]


photo_forSMS1_1 = "https://i.pinimg.com/originals/f5/68/01/f56801dc02d18450fa2e38ca309173b9.jpg"
photo_forSMS1_2 = "https://img.razrisyika.ru/kart/138/1200/549178-homyakov-23.jpg"
photo_forSMS2_2 = "https://lastfm.freetls.fastly.net/i/u/ar0/97b81e650d45b46be60bd4d9416ba216.png"
list_photo_question4 = [photo_forSMS1_1, photo_forSMS1_2, photo_forSMS2_2]

photo_one = "https://get.wallhere.com/photo/birds-animals-branch-wildlife-bird-of-prey-owl-tree-bird-fa\
una-vertebrate-144087.jpg"
photo_two = "https://volyn.com.ua/content/thumbs/1500x1000/t/j5/b5a4zs-dgahirkm6s3yhaqkjzd33yfssgdfej5t.jpg"
photo_three = "https://s1.1zoom.me/b5057/321/Lynx_Three_3_536031_2048x1152.jpg"
list_photo_question5 = [photo_one, photo_two, photo_three]
list_photo_avtor00 = 'https://on-desktop.com/ru/images/wp.php?path=/wps/Animals___Wild_artiodactyls_Deer_and_her_chi\
ld_081738_.jpg&wp=17'
list_photo_avtor01 = 'https://i3.wp.com/i.natgeofe.com/n/578d46cc-05f1-43b1-8401-e9b751616e0d/NationalGeographic_2179\
691_square.jpg?ssl=1'
list_photo_avtor02 = 'https://uhdwallpapers.org/uploads/converted/18/04/04/lynx-at-the-zoo-3840x2400_87448-mm-90.jpg'
list_photo_avtor03 = 'https://s2.best-wallpaper.net/wallpaper/1600x1200/1809/Brown-bear-look-at-creek_1600x1200.jpg'
list_photo_avtor04 = 'https://i.artfile.ru/1440x900_459126_[www.ArtFile.ru].jpg'
list_photo_avtor05 = 'https://www.1zoom.me/big2/171/313323-Lastochka.jpg'
list_photo_avtor06 = 'https://rgo.ru/upload/content_block/images/b07f22977210961dad243f9405c85656/c245e861330c044c10\
cb2f87aaacec88.jpg?itok=-SYF1mBP'
list_photo_avtor07 = 'https://i.pinimg.com/originals/81/1b/4a/811b4a489759740af7fe792a0fa344c5.jpg'
list_photo_avtor08 = 'https://avatars.mds.yandex.net/i?id=445a7575a29a40b9b529456afe0b097c_l-5221896-images-thumbs&n=13'
list_photo_avtor09 = 'https://img.goodfon.ru/original/2400x1600/8/d7/tigrenok-malysh-khishchnik.jpg'
list_photo_avtor10 = 'https://64.media.tumblr.com/cbcd3d4b0928de1d3f72463a25a6b5e1/tumblr_nwvof8uWNq1ugyuu3o1_1280.jpg'
list_photo_avtor11 = 'https://rare-gallery.com/thumbs/111619-deer-new-zeland-mountains.jpg'
list_photo_avtor12 = 'https://wallup.net/wp-content/uploads/2018/10/09/727734-calves-forest-grass-trees-flock.jpg'
list_photo_avtor13 = 'https://www.thesun.co.uk/wp-content/uploads/2018/12/NINTCHDBPICT000453594093.jpg'
list_photo_avtor14 = 'https://photo-1.ru/wp-content/uploads/2017/12/583d3458a6fc9.jpg'
list_photo_avtor15 = 'https://zooclub.ru/attach/4300.jpg'
list_photo_avtor16 = 'https://animals.pibig.info/uploads/posts/2023-09/1695910920_animals-pibig-info-p-zveri-obitayushc\
hie-v-taige-pinterest-64.jpg'
list_photo_avtor17 = 'https://images.hdqwalls.com/download/lynx-5k-z9-2880x1800.jpg'
list_photo_avtor18 = 'https://www.evgenidinev.com/wp-content/uploads/2022/11/horse-11396d.jpg'
list_photo_avtor19 = 'https://lh3.ggpht.com/-oca6wqkHzts/VhVtuVfmHJI/AAAAAAAFxpY/vBD4QARu6JE/s2048/hd-148318-ASCW148\
318.jpg'
list_photo_avtor20 = 'https://blog.humanesociety.org/wp-content/uploads/2017/02/MANGELSEN-PG023_20080510_20120140_339\
897-1.jpg'
list_photo_avtor21 = 'https://animals.pibig.info/uploads/posts/2023-10/1696350641_animals-pibig-info-p-dikii-lesnoi-ka\
ban-instagram-5.jpg'
list_photo_avtor22 = 'https://i.pinimg.com/originals/b8/e6/e8/b8e6e887aa882e4f79a981360574f640.jpg'
list_photo_avtor23 = 'http://www.atc-cz2.it/wp-content/uploads/2018/05/3.jpg'
list_photo_avtor24 = 'https://cdn.shopify.com/s/files/1/1428/7694/files/Earth_Day_-_Celebrating_our_Native_Fauna12_643\
0e5ce-9407-4947-bff1-b9fd4940d95e.jpg'
list_photo_question_avtor1 = [list_photo_avtor00, list_photo_avtor01, list_photo_avtor02]
list_photo_question_avtor2 = [list_photo_avtor03, list_photo_avtor04, list_photo_avtor05]
list_photo_question_avtor3 = [list_photo_avtor06, list_photo_avtor07, list_photo_avtor08]
list_photo_question_avtor4 = [list_photo_avtor09, list_photo_avtor10, list_photo_avtor11]
list_photo_question_avtor5 = [list_photo_avtor12, list_photo_avtor13, list_photo_avtor14]
list_photo_question_avtor6 = [list_photo_avtor15, list_photo_avtor16, list_photo_avtor17]
list_photo_question_avtor7 = [list_photo_avtor18, list_photo_avtor19, list_photo_avtor20]
list_photo_question_avtor8 = [list_photo_avtor21, list_photo_avtor22, list_photo_avtor23]


all_list_photo_questions = [value for key, value in globals().items() if key.startswith('list_photo_question')]                      #глобальный параметр
print(all_list_photo_questions)


# Информация об кнопках:


info_about_button_start = ['нажал "ДА"']
info_about_buttons_question1 = ['стадное', 'не стадное']
info_about_buttons_question2 = ['дневной', 'ночной', 'всегда активен']
info_about_buttons_question3 = ["Тепло и укрытие", "голодание, засухоустойчивость", "Влажная среда и близость воды"]
info_about_buttons_question4 = ['большой', 'маленький', 'средний']
info_about_buttons_question5 = ['Птицы', 'Рептилии Амфибии', 'Млекопитающие']

allInfo_about_buttons = [value for key, value in globals().items() if key.startswith('info_about_button')]                      #глобальный параметр
print(allInfo_about_buttons)







