import random


class Model(object):
    """A Markov model for a corpus

    Args:
        corpus (str): Text to be modeled into a markov chain
        n (int): State-size to be modeled

    Attributes:
        model (object): Markov chain representation of the corpus as an n-gram model
    """

    def __init__(self, corpus, n=2):
        self.model = self.build_model(corpus.split(), n)

    def build_model(self, corpus, n):
        """dict: Returns a dict of list representing states and their links"""
        model = dict()

        for run in range(len(corpus) - n):
            gram = tuple(corpus[run:run+n])
            next_token = corpus[run+n]

            if gram in model:
                model[gram].append(next_token)
            else:
                model[gram] = [next_token]

            final_gram = tuple(corpus[len(corpus)-n:])
            if final_gram in model:
                model[final_gram].append(None)
            else:
                model[final_gram] = [None]

        return model

    def generate(self, n, init=None, max_iter=100):
        """str: Returns a string composed of generated n-grams"""
        if init is None:
            init = random.choice(list(self.model.keys()))

        output = list(init)
        current = tuple(init)

        for i in range(max_iter):
            if current in self.model:
                possible_tokens = self.model[current]
                next_token = random.choice(possible_tokens)

                if next_token is None:
                    break

                output.append(next_token)
                current = tuple(output[-n:])
            else:
                break

        return ' '.join(output)
