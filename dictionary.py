import PyDictionary


class Dictionary:
    """From the GUI takes a list of word(s), finds them in the PyDictionary module,
     gives them back with their meaning"""

    def __init__(self):
        self._dictionary_results = []  # Stores the meaning of the given words
        self.dictionary = PyDictionary.PyDictionary()  # Dictionary object
        self.words_list = []  # Stores the entry words
        self.keys = []  # Types of the current word
        self.values = []  # Meanings of the current word
        self.index = 0  # Variable for the length of the meaning text

    def input(self, words_list):
        """Takes the entry input, and makes a list from the words"""
        self.words_list = words_list.split(' ')  # List of the GUI words
        for i in self.words_list:
            self._dictionary_results.append(self.dictionary.meaning(i))

    def word_by_word(self, num):
        """Finds the meaning of the given words"""
        if self._dictionary_results[num] is None:  # If the given word is unknown
            self.keys = ""
            self.values = "Unknown word"
        else:
            self.values = []
            self.keys = ', '.join(self._dictionary_results[num].keys())  # Types of the word
            for j in range(len(list(self._dictionary_results[num].values()))):
                for i in range(len(list(self._dictionary_results[num].values())[j])):
                    # Meanings of the current word, list form
                    self.values.append(list(self._dictionary_results[num].values())[j][i].capitalize())
            self.values = "; ".join(self.values)  # Meanings of the word, string form
        if len(self.values) > 650:  # If the length of the string is too long, shortens it
            self.index = self.values[600:].index(";")
            self.values = self.values[:600 + self.index]

    def reset(self):
        """If the clear button is pressed this function resets the necessary variables"""
        self._dictionary_results = []
        self.values = []
        self.keys = []
        self.words_list = []
