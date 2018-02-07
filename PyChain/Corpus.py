import string
from numpy import random
from .Model import Model


class Corpus:
    """
    A corpus made for training the markov chain model
    Takes in a string and outputs a corpus object

    Attributes:
        text: Input string stripped of any punctuation
        model: A model object for the corpus

    Functions:
        generate:
    """

    def __init__(self, data, n):
        self.text = self.strip_text(data)
        self.model = Model(self.text, n)

    def to_words(self):
        """Return a list of words in the corpus"""
        return self.text.split()

    def to_characters(self):
        """Return a list of characters in the corpus"""
        return list(self.text)

    def generate(self, n, init=None, max_iter=100):
        """Generate a length of characters based on the model"""

        return self.model.generate(n, init, max_iter)

    def strip_text(self, data):
        """Remove punctuation from string"""
        cleaned_text = []
        split_data = data.split()

        for word in split_data:
            clean_word = []
            word = word.lower()
            word = list(word)

            for count, character in enumerate(word):

                if character in string.punctuation:
                    continue

                clean_word.append(character)

            clean_word = ''.join(clean_word)
            cleaned_text.append(clean_word)

        cleaned_text = ' '.join(cleaned_text)
        return cleaned_text

    def data(self):
        return self.__dict__
