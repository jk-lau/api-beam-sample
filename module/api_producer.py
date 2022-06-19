# Part 1: Build API source with single endpoint
# Expected return: 
# a) Type of an animal: cat (50%) or dog (50%)
# b) Weight of an animal: cat N(10,3) or dog N(7,4)

import random
from flask import Flask, jsonify
app = Flask(__name__)

# Build a get_animal API endpoint
@app.route("/get_animal")
def animal():
    animal_type = ('cat' if random.randint(0, 1) == 0 else 'dog')
    
    if animal_type == 'cat':
        weight = random.gauss(10, 3)
    else:
        weight = random.gauss(7, 4)

    return jsonify({'type': animal_type, 'weight': weight})