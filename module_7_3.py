import re
from operator import index
from re import search


class WordsFinder:
    def __init__(self, *file_name):
        self.file_name = []
        for i in file_name:
            self.file_name.append(i)

    def get_all_words(self):
        all_words = {}
        dont_char = [',', '.', '=', '!', '?', ';', ':', ' - ', '\n']
        for i in self.file_name:
            text_file = ''
            with open(i,'r', encoding='utf-8') as f_n:
                for line in f_n:
                    for j in dont_char:
                        line = line.replace(j,'')
                    text_file = text_file + line+' '
            all_words[i] = text_file.lower().split()
        return all_words

    def find(self, word):
        for name, words in self.get_all_words().items():
            search_first = int(words.index(word.lower()))
            if  search_first > 0:
                return {name: search_first+1}

    def count(self, word):
        for name, words in self.get_all_words().items():
            search_first = int(words.count(word.lower()))
            if search_first > 0:
                return {name: search_first}

#Основная программа
finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего