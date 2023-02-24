# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word


    def match(self, word_list):
        anagrams_list = []
        sorted_main = sorted([letter for letter in self.word])
        print(sorted_main)
        for word in word_list:
            sorted_list_word = sorted([letter for letter in word])
            print(sorted_list_word)
            if sorted_main == sorted_list_word:
                anagrams_list.append(word)
        return anagrams_list

