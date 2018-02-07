import os
import PyChain

if __name__ == "__main__":
    with open(os.path.dirname(os.path.realpath(__file__)) + '/data/Usernames.txt') as file:
        text = file.read()

    model = PyChain.Corpus(text, 3)

    for i in range(100):
        print(model.generate(3))
        print('')

