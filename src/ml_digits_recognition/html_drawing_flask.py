import torch
from flask import request, Flask, jsonify
from base64 import b64decode
from io import BytesIO
from PIL import Image
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from neural_network import NeuralNetwork, NNTest, get_test_input_from_pil


app = Flask(__name__)

device = 'cuda' if torch.cuda.is_available() else 'cpu'
model = NeuralNetwork().to(device)
model.load_state_dict(torch.load('model_precise.pt'))
model.eval()
nn_test = NNTest(model)


@app.route("/ml_digits_recognition", methods=["GET"])
def html_drawing():
    img_str = request.args['img'].replace("data:image/png;base64,", "")
    img = Image.open(BytesIO(b64decode(img_str)))
    test_input_nn = get_test_input_from_pil(img)
    digit = nn_test.classify(test_input_nn)
    print(digit)
    response = jsonify({'digit': digit})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
