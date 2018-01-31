let data = {
    lorem: '',
    characters: {},
    sorted_characters: [],
    chances: [],
    init: function() {
        this.lorem = document.getElementById('lorem').innerText.match(/(.)/g);

        for (let i = 0; i < this.lorem.length; i++) {
            if (this.characters[this.lorem[i]] === undefined) {
                this.characters[this.lorem[i]] = 0;
            }
            this.characters[this.lorem[i]] += 1;
        }

        for (let key in this.characters){
            if (this.characters.hasOwnProperty(key)) {
                if (key.match(/[., ]/g)) {
                    continue
                }
                this.sorted_characters.push([key, this.characters[key]]);
            }
        }

        this.sorted_characters.sort((a, b) => {
            return b[1] - a[1];
        });

        for (let character in this.sorted_characters) {
            add_letter(
                this.sorted_characters[character][0],
                this.sorted_characters[character][1],
                this.lorem.length - this.lorem.join('').match(/[., ]/g).length
            );
            let chance = this.sorted_characters[character][1] / (this.lorem.length - this.lorem.join('').match(/[., ]/g).length);
            this.chances.push(chance);
        }
    },

    map_chances: function () {
        this.counter = 0;
        this.mapped_chances = [];
        for (let i = 0; i < this.sorted_characters.length; i++) {
            for (let x = 0; x < this.chances[i] * 100; x++) {
                this.mapped_chances.push(this.sorted_characters[i])
            }
        }
    },

    generate_word: function () {
        this.map_chances();
        let text = document.getElementById('value');
        text.value = '';

        let length = Math.floor(Math.random() * 10) + 4;

        for (let i = 0; i < length; i++) {
            text.value += this.mapped_chances[Math.floor(Math.random() * this.mapped_chances.length)][0].toLowerCase();
        }
    },

    generate_latin: function () {
        this.map = new Map();

        let counter = 0;
        for (let letter of this.lorem) {
            if (letter.match(/[., ;]/g)) {
                counter += 1;
                continue
            }
            if (this.lorem[counter + 1].toLowerCase().match(/[.,;]/g)) {
                counter += 1;
                continue
            }
            if (this.map.get(letter.toLowerCase()) === undefined) {
                this.map.set(letter.toLowerCase(), [
                    this.lorem[counter + 1].toLowerCase()
                ])
            } else {

                this.map.get(letter.toLowerCase()).push(this.lorem[counter + 1].toLowerCase())
            }
            counter += 1;
        }

        let characters = Array.from(this.map.keys());
        console.log('Characters: ', characters.length);
        console.log('Map: ', this.map.size);

        let current_index = this.map.get(characters[Math.floor(Math.random() * characters.length)]);
        let word = '';

        let length = Math.floor(Math.random() * (characters.length - 3 + 1) + 3);

        for (let i = 0; i < 20; i++) {
            console.log(current_index)
            let letter = random_letter(current_index);

            console.log(letter);

            word += letter;
            if (this.map.get(letter) === undefined) {
                break
            } else {
                current_index = this.map.get(letter);
            }

        }

        let text = document.getElementById('value');
        text.value = word;
    }
};

function add_letter(character, count, length) {
    let container = document.createElement('div');
    let symbol = document.createElement('div');
    let data = document.createElement('div');

    let symbol_char = document.createElement('h3');

    let iterations = document.createElement('p');
    let chances = document.createElement('p');
    let percentage = count / length * 100;

    container.className = 'container';
    symbol.className = 'symbol';
    data.className = 'data';
    symbol_char.innerText = character;

    iterations.innerText = '#: ' + count;

    chances.innerText = 'Chance: ' + percentage.toFixed(5) + '%';

    container.appendChild(symbol);
    symbol.appendChild(symbol_char);
    container.appendChild(data);
    data.appendChild(iterations);
    data.appendChild(chances);
    document.getElementById('data').appendChild(container);
}

function generate_word() {
    let text = document.getElementById('value');
    text.value = '';

    let length = Math.floor(Math.random() * 10) + 4;

    for (let i = 0; i < length; i++) {
        text.value += dice_chances[Math.floor(Math.random() * dice_chances.length)];
    }
}

function random_letter(char) {
    return char[Math.floor(Math.random() * char.length)];
}

document.addEventListener("DOMContentLoaded", e => data.init());