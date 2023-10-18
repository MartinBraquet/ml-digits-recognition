import os
import sys
import json
from urllib.parse import parse_qs
from base64 import b64decode
from io import BytesIO
from PIL import Image
import torch

sys.path.insert(0, os.path.dirname(__file__))

from neural_network import NeuralNetwork, NNTest, get_test_input_from_pil

device = 'cuda' if torch.cuda.is_available() else 'cpu'
model = NeuralNetwork().to(device)
model.load_state_dict(torch.load('model_precise.pt'))
model.eval()
nn_test = NNTest(model)


def app(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain'), ('Access-Control-Allow-Origin', '*')])
    img_str = parse_qs(environ['QUERY_STRING'])['img'][0].replace("data:image/png;base64,", "")
    # print(img_str)
    img = Image.open(BytesIO(b64decode(img_str)))
    test_input_nn = get_test_input_from_pil(img)
    digit = nn_test.classify(test_input_nn)
    print(f'Digit: {digit}')
    return [json.dumps({'digit': digit}).encode()]
