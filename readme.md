# PyChain

Personal implantation of markov chains in python. Aiming for believable generation
of texts, patterned generation of components to roguelikes and maybe more.

### Usage

```python
import PyChain

with open("/path/to/data.txt") as file:
    text = file.read()
    
# Input text and n-gram size
model = PyChain.Model(text, 2)
    
for i in range(10):
    # N-gram size should fit the models size, max_iter sets a limit on generation
    print(model.generate(2, max_iter=140) + '\n')
```