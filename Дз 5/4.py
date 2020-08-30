from googletrans import Translator

translator = Translator()
with open('text_4.txt', 'r', encoding="UTF-8") as text_4:
    with open('text_4a.txt', 'w+', encoding="UTF-8") as text_4a:
        context = text_4.read()
        context_new = translator.translate(context, dest='ru')
        print(context_new.text, file=text_4a)
