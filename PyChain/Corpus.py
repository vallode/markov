from .Model import Model
from .Utility import strip_text


class Corpus(object):
    """Data object used to generate markov chains

    Higher n-gram sizes provide generation closer to the original text

    Args:
        data (str): Input for generating the markov chain
        n (int): Size of n-gram

    Attributes:
        data: (str): Input stripped of any special characters
        model (Object): A markov model of state-size `n`"""
    def __init__(self, data, n=2):
        self.data = strip_text(data)
        self.model = Model(self.data, n)

    def get_words(self):
        """list: Returns a list of words in the corpus"""
        return self.data.split()

    def get_characters(self):
        """list: Returns a list of characters in the corpus"""
        return list(self.data)

    def generate(self, n, init=None, max_iter=100):
        """Generate a length of characters based on the model"""

        return self.model.generate(n, init, max_iter)

    def data(self):
        return self.__dict__
