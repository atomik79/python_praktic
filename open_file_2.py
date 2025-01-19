class WordsFinder:
    def __init__(self,*files):
        self.files = files

    def get_all_words(self):
        all_words = {}
        sim_vol = ',', '.', '=', '!', '?', ';', ':', ' - '
        words = []
        for name_files in self.files:
            with open(name_files, "r", encoding="utf-8") as file:
                for line in file:
                    line = line.lower().split()
                    for znak in line:
                        if not znak in sim_vol:
                            words += znak.split()
            all_words[name_files] = words
        return all_words

    def find(self, word):
        result = {}
        all_words = self.get_all_words()
        for name_files, words in all_words.items():
            if word.lower() in words:
                result[name_files] = words.index(word.lower()) + 1

        return result

    def count(self, word):
        result = {}
        #count = 0
        all_words = self.get_all_words()
        for name_files, words in all_words.items():
            result[name_files] = words.count(word.lower())

        return result



find_file = WordsFinder('test_file.txt')
find_file2 = WordsFinder('Mother_Goose_Monday’s_Child.txt')

print(find_file.get_all_words())
print(find_file.find('TEXT'))
print(find_file.count('teXT'))

print(find_file2.get_all_words())
print(find_file2.find('Child'))
print(find_file2.count('Child'))