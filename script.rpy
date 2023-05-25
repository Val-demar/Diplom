# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define b = Character('Бранте', color="#D2B48C")

define r = Character('Роберт', color="#D2B48C")

define s = Character('Стефан', color='#D2B48C')

define t = Character('Тим', color='#D2B48C')

define x = Character ('...', color='#D2B48C')

define slowdissolve = Dissolve(3.0)

define flashbulb = Fade(0.8, 0.0, 0.8, color='#fff')


label start:

    play music "audio/main_sound.mp3"

    scene start_loc
    with slowdissolve

    pause 1.0

    show gg
    with slowdissolve


    b "Меня зовут Бранте, Господин Бранте."

    play sound "audio/str.mp3"

    b "...{w=3.0}...{w=3.0}Но так было не всегда."

    play sound "audio/str.mp3"

    b "Хочешь узнать мою историю?"

    menu:
        "Конечно!":
          jump start_g


    label start_g:

     b "замечательно! Тогда начнем"

    hide gg

    play sound "audio/str.mp3"

    pause 2.0

    scene second_loc
    show fath
    with slowdissolve


    r "Привет сын, я так рад увидеть тебя!"

    play sound "audio/str.mp3"

    r "Ты стал таким взрослым и мужественным. Наверняка тебя мучает куча вопросов, которые ты хочешь задать своему отцу."

    play sound "audio/str.mp3"

    menu:
     "Почему ты так надолго уезжаешь от нас?":
         jump ans1

     "Можешь рассказать о нашей семье?":
         jump ans2

     "Расскажи о нашем государстве?":
         jump ans3

    label ans1:

      r "Так велит мой долг нашей стране. Я работаю судьей и во времена напряжения сословий у меня очень много работы"

      play sound "audio/str.mp3"

      r "Но сейчас у меня много работы в нашем городе и я задержусь надолго"

      play sound "audio/str.mp3"

      jump ansraz1

    label ans2:

      r "Ты уже так вырос...{w=1.0}"

      play sound "audio/str.mp3"

      r "Ты заметил, что наша семья отличается от других. Мы имеем двусословное происхождение, ты и твоя мама были простолюдинами, а я и Стефан имеем благородное происхождение"

      play sound "audio/str.mp3"

      r "Но ты обязательно получишь благородный титул, именно поэтому твой брат так на тебя наседает"

      play sound "audio/laugh_fath.mp3"

      r "Он очень любит тебя и беспокоится за нашу семью. Позже мы тебе все объясним"

      play sound "audio/str.mp3"

      jump ansraz1

    label ans3:

        r "Наше государство Магра самое великое и большое государство в мире. Все благодаря нашему императору Уриэлю Третьему посланнику богов, даровавшему ему свещенный закон об простолюдинах и дворянах"

        play sound "audio/str.mp3"

        r "Попроси у Стефана книгу о становлении Магры, в ней все подробно расписано"

        play sound "audio/str.mp3"

        r "Он будет рад познакомить тебя с законами нашего государства"

        jump ansraz1

    label ansraz1:

        r "Хочешь узнать что то еще?"

        play sound "audio/str.mp3"

    menu:
        "Почему ты так надолго уезжаешь от нас?":
            jump ans1

        "Можешь рассказать о нашей семье?":
            jump ans2

        "Расскажи о нашем государстве?":
            jump ans3

        "Нет, спасибо Отец":
            jump dialog

    label dialog:

        r "Было очень приятно с тобой поговорить сынок, но где же твой брат?"

        play sound "audio/str.mp3"

        r "Я соскучился по нему не меньше, чем по тебе"

        play sound "audio/str.mp3"

        show fath at left
        with move


        show stefan:
            xcenter 0.7

        s "Здравствуй отец. Ты возишься с моим безсословным братом{w=5.0} Это так похоже на тебя"

        play sound "audio/str.mp3"

        s "Оставь нас Бранте, нам нужно поговорить."

        play sound "audio/str.mp3"

        r "Да мальчик мой, пойди поиграй со своими друзьями"

        play sound "audio/str.mp3"

        scene dvor
        with slowdissolve

        show ggmal
        with slowdissolve

        b "Ну и где же Тим?!"

        play sound "audio/str.mp3"

        b "Он всегда ошивается в этом грязном квартале"

        play sound "audio/str.mp3"

        t "Эй господин полукровка, вы потеряли своего слугу?"

        hide ggmal
        with slowdissolve

        pause 1.0

        show tim
        with slowdissolve

        t "Ты чего такой хмурый?"

        play sound "audio/str.mp3"

        t "Стэфан опять читал тебе нотации?"

        play sound "audio/str.mp3"

        hide tim
        with slowdissolve

        show ggmal
        with slowdissolve

        pause 1.5

        play sound "audio/vzdoh.mp3"

        b "Да, для него я всегда все делаю слишком по простолюдински"

        hide ggmal
        with slowdissolve

        show tim
        with dissolve

        play sound "audio/hehe.mp3"

        t "Ха-ха-ха хочешь покажу тебе кое-что супер-простолюдинское?"

        t "Угадай в какой руке!"

        menu:
            "В левой!":
              jump ans4

            "Наверное в правой":
              jump ans5

        label ans4:

            t "Угадал!"

            t "Смотри я стащил у отца трубку и она набита табаком"

            t "Возьми попробуй. Классная штука"

            x "Тим всучивает вам трубку"

            hide tim

            show ggmal at center

            b "Я даже не зн....."

            play sound "audio/punch.mp3"
            with vpunch

            hide ggmal

            show stefan
            with flashbulb

            s "Что ты себе позваляешь?"
        menu:
            "ай":
               jump dialog1

            "Я не виноват!":
                jump dialog1

        label ans5:

            t "Не угадал!"

    label dialog1:

     s "Опять ты позоришь семью"

    return
