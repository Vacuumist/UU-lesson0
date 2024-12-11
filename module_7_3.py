class WordsFinder:
    def __init__(self, *files):
        self.file_mames = files

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_mames:
            words = []
            with open(file_name, encoding='utf-8') as file:
                for line in file:
                    line = line.lower()
                    for punct in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                        line = line.replace(punct, ' ')
                    words.extend(line.split())
            all_words.update({file_name:words})
        return all_words

    def find(self, word):
        result = {}
        for name, words in self.get_all_words().items():
            for i in range(len(words)):
                if words[i] == word.lower():
                    result.update({name:i + 1})
                    break
        return result

    def count(self, word):
        result = {}
        for name, words in self.get_all_words().items():
            cnt = 0
            for i in range(len(words)):
                if words[i] == word.lower():
                    cnt += 1
            if cnt != 0:
                result.update({name:cnt})
        return result


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего

finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))