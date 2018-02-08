import os
import PyChain

if __name__ == "__main__":
    with open(os.path.dirname(os.path.realpath(__file__)) + '/data/Seuss.txt') as file:
        text = file.read()

    model = PyChain.Corpus(text, 1)

    for i in range(100):
        print(model.generate(1, max_iter=4) + '\n')
