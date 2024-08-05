class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        for name_ in self.file_names:
            self.all_words = {}
            self.value = []
            with open(name_, encoding = 'utf-8') as file:
                for self.line in file:
                    self.line = self.line.lower()
                    symbols_to_remove = [',', '.', '=', '!', '?', ';', ':', ' - ']
                    for i in self.line:
                        if i in symbols_to_remove:
                            self.line = self.line.replace(i, '')
                    self.line = self.line.split()
                    #print(self.line)
                    self.value += self.line
            self.all_words = {f'{name_}': self.value}
            return self.all_words

    def find(self, word):
        self.word = word
        self.finding_word = {}
        self.position = []
        for i in self.value:
            if i == word.lower():
                self.position = self.value.index(i) + 1
            self.finding_word = {f'{self.file_names}': self.position}
        return self.finding_word

    def count(self, word):
        self.counting_word = {}
        self.quantity = 0
        for i in self.value:
            if i == word.lower():
                self.quantity += 1
            self.counting_word = {f'{self.file_names}': self.quantity}
        return self.counting_word

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))

finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
print(finder1.get_all_words())
print(finder1.find('captain'))
print(finder1.count('captain'))

finder3 = WordsFinder('Rudyard Kipling - If.txt',)

print(finder3.get_all_words())
print(finder3.find('if'))
print(finder3.count('if'))

