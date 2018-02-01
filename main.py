import os
import re
import random
import numpy as np


class Markov:

    def __init__(self):
        with open(os.path.dirname(os.path.realpath(__file__)) + '/text.txt') as file:
            self.text = file.read()

        self.length = {}
        self.letters = {}
        self.stems = {}
        self.bigrams = {}
        self.trigrams = {}
        self.count = 0

    def map_characters(self):
        self.text = re.sub(r'[.,;:*%$#@!?><\[\]\n]', ' ', self.text).lower()

        for character in self.text:
            if character in self.letters or character == ' ':
                continue
            else:
                self.letters[character] = {}
                self.bigrams[character] = {}

        for letter in re.sub(r'\B.| ', '', self.text).lower():
            if letter in self.stems:
                continue
            else:
                self.stems[letter] = 0

        for word in re.findall(r'\w+', self.text):
            if len(word) not in self.length:
                self.length[len(word)] = 1
            else:
                self.length[len(word)] += 1

    def states(self):
        for letter in self.letters:
            pairs = re.findall(r'({}.?)'.format(letter), self.text)

            for bigram in pairs:
                if bigram[-1] != ' ':
                    if bigram not in self.bigrams[letter]:
                        self.bigrams[letter][bigram] = 1
                    else:
                        self.bigrams[letter][bigram] += 1

                    if bigram not in self.trigrams:
                        self.trigrams[bigram] = {}

                if bigram[-1] not in self.letters[letter]:
                    self.letters[letter][bigram[-1]] = 0
                else:
                    self.letters[letter][bigram[-1]] += 1

        for letter in self.stems:
            expression = re.compile(r'{}'.format(letter))
            stems = re.sub(r'\B.| ', '', self.text).lower()

            pairs = expression.findall(stems)

            for character in pairs:
                if character not in self.stems:
                    self.stems[letter] = 1
                else:
                    self.stems[letter] += 1

        for bigram in self.trigrams:
            pairs = re.findall(r'({}.?)'.format(bigram), self.text)

            for trigram in pairs:
                if trigram[-1] != ' ':
                    if trigram not in self.trigrams[bigram]:
                        self.trigrams[bigram][trigram] = 1
                    else:
                        self.trigrams[bigram][trigram] += 1

    def generate(self, words):
        for x in range(words):
            lengths = list(self.length.keys())

            length_probabilities = list(map(lambda x: x / sum(self.length.values()), self.length.values()))
            length = np.random.choice(lengths, p=length_probabilities)

            stems = list(self.stems.keys())

            stem_probabilities = list(map(lambda x: x / sum(self.stems.values()), self.stems.values()))
            stem = np.random.choice(stems, p=stem_probabilities)

            # print('Word stem: ', stem)

            bigram_probabilies = list(map(lambda x: x / sum(self.bigrams[stem].values()), self.bigrams[stem].values()))
            bigram = np.random.choice(list(self.bigrams[stem].keys()), p=bigram_probabilies)

            # print('Stem bigram: ', bigram)

            state = bigram
            word = ''

            while True:
                # print('Current state: ', state)
                word += state
                # print('Word: ', word)

                if len(state) > 1 and state[-1] != ' ':
                    state = state[-1]

                weighed_probabilities = list(map(lambda x: x / sum(self.letters[state].values()), self.letters[state].values()))
                characters = list(self.letters[state].keys())
                next_character = np.random.choice(characters, p=weighed_probabilities)

                while len(word) < 4 and next_character == ' ':
                    next_character = np.random.choice(characters, p=weighed_probabilities)

                if state == next_character:
                    bigram = state + next_character

                    trigram_probabilies = list(map(lambda x: x / sum(self.trigrams[bigram].values()), self.trigrams[bigram].values()))
                    trigram = np.random.choice(list(self.trigrams[bigram].keys()), p=trigram_probabilies)
                    # print('Found equals: ' + state, next_character)
                    # print('Trigram: ' + trigram)
                    state = trigram[-1]
                else:
                    if next_character == ' ' or len(word) >= length:
                        break
                    else:
                        state = next_character

            print(word)


if __name__ == "__main__":
    markov = Markov()

    markov.map_characters()
    markov.states()
    print(markov.length)
    markov.generate(100)