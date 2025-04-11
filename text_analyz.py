'''
Дан файл со стихотворением poem.txt.
Необходимо реализовать класс TextAnalizator, включающий в себя методы анализа
текста и записи результата в файлы analyz.txt, analyz.json
1. Сколько всего символов в тексте
2. Сколько букв в тексте (без пробелов и знаков препинания (,.!?))
3. Сколько всего строк в тексте
4. Сколько непустых строк в тексте
5. Сколько всего слов в тексте
6*. Сколько слов в каждой строке
7*. Сколько символов в каждой строке
8. Найти повторяющиеся слова в тексте с указанием количества
9*. Провести частотный анализ букв (частота появления какждой буквы в тексте)
10. Найти все посторонние символы (пробелы и знаки препинания) - какие и сколько
'''

class TextAnalizator:
    def __init__(self, text):
        self.text = text
    def length_symbols_all(self):
        print(f'Всего символов - {len(self.text)}')

    def length_letters(self):
        text1 = self.text.replace('\n', '').replace(',', '').replace('.', '').replace('?', '').replace('!', '')
        print(f'Всего букв - {len(text1)}')
    def splits(self):
        text1 = self.text.splitlines()
        print(f'Всего строк - {len(text1)}')
    def splits_full(self):
        text1 = self.text.splitlines()
        text2 = []
        for i in text1:
            if i != '':
                text2.append(i)

        print(f'Всего full строк - {len(text2)}')

    def words(self):
        text1 = self.text.splitlines()
        text2 = []
        text3 = []
        for i in text1:
            if i != '':
                text2.append(i)
        for k in text2:
            words = k.split(' ')
            text3.extend(words)



        print(f'Всего слов - {len(text3)}')









text = '''
Привет jnjknhj
КА jjj Привет
'''

text1 = TextAnalizator(text)
text1.length_symbols_all()
text1.length_letters()
text1.splits()
text1.splits_full()
text1.words()
