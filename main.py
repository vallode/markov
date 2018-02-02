import os
import re
import threading
import numpy as np


class Markov:

    def __init__(self):
        with open(os.path.dirname(os.path.realpath(__file__)) + '/Te_Deum.txt') as file:
            self.text = file.read()

        self.length = {}
        self.nodes = {}

    def map_characters(self):
        self.text = re.sub(r'\W', ' ', self.text).lower()

        Node.count = len(self.text.replace(' ', ''))
        Node.stems = len(self.text.split())

        for character in self.text.replace(' ', ''):
            if character in self.nodes:
                self.nodes[character].add()
            else:
                self.nodes[character] = Node(character, 0)

        for word in self.text.split():
            word_length = len(word)
            if word_length in self.length:
                self.length[word_length] += 1
            else:
                self.length[word_length] = 1

            stem = word[0]
            self.nodes[stem].stem()

    def states(self):
        for node in self.nodes.values():
            proceeding = re.findall(r'(?<={}).'.format(node.data()['name']), self.text)

            for character in proceeding:
                node.link(character)

            bigrams = re.findall(r'{}(?! ).?'.format(node.data()['name']), self.text)

            for bigram in bigrams:
                node.bigram(bigram)

    def generate(self, words):
        for x in range(words):
            word = ''
            lengths = list(self.length.keys())

            length_probabilities = list(map(lambda x: x / sum(self.length.values()), self.length.values()))
            word_length = np.random.choice(a=lengths, p=length_probabilities)

            stem_probabilities = []
            stems = []
            for node in markov.nodes:
                stem_probabilities.append(self.nodes[node].data()['stem_weight'])
                stems.append(self.nodes[node].data()['name'])

            stem = np.random.choice(a=stems, p=stem_probabilities)

            node = markov.nodes[stem].data()

            bigrams = list(node['bigrams'].keys())
            bigram_probabilies = list(map(lambda x: x / sum(node['bigrams'].values()), node['bigrams'].values()))

            bigram = np.random.choice(a=bigrams, p=bigram_probabilies)

            state = bigram[1]
            word += bigram

            while True:
                node = markov.nodes[state].data()

                links = list(node['links'].keys())
                link_weights = list(map(lambda x: x / sum(node['links'].values()), node['links'].values()))

                next_state = np.random.choice(a=links, p=link_weights)

                while len(next_state) < word_length and next_state == ' ':
                    next_state = np.random.choice(a=links, p=link_weights)

                if next_state == ' ' or len(word) >= word_length:
                    break
                else:
                    state = next_state
                    word += state

            print(word)


class Node:
    count = 0
    stems = 0

    def __init__(self, character, freq):
        self.name = character
        self.frequency = freq
        self.stem_frequency = 0

        self.weight = 0
        self.stem_weight = 0

        self.bigrams = {}
        self.trigrams = {}
        self.links = {}

    def link(self, character):
        if character in self.links:
            self.links[character] += 1
        else:
            self.links[character] = 1

    def bigram(self, bigram):
        if bigram in self.bigrams:
            self.bigrams[bigram] += 1
        else:
            self.bigrams[bigram] = 1

    def stem(self):
        self.stem_frequency += 1
        self.stem_weight = self.stem_frequency / Node.stems

    def add(self):
        self.frequency += + 1
        self.weight = self.frequency / Node.count

    def data(self):
        return self.__dict__


if __name__ == "__main__":
    markov = Markov()

    markov.map_characters()
    markov.states()
    markov.generate(100)
