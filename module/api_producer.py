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