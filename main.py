import os
import PyChain

if __name__ == "__main__":
    with open(os.path.dirname(os.path.realpath(__file__)) + '/data/Jabber.txt') as file:
        text = file.read()

    model = PyChain.Corpus(text, 2)

    for i in range(100):
        print(model.generate(2, max_iter=140) + '\n')
