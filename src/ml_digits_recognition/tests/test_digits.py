import os
import unittest

from PIL import Image

from ml_digits_recognition.neural_network import get_test_input_from_pil, load_nn_test


class TestDigit(unittest.TestCase):
    def test_one(self):
        curr_dir = os.path.dirname(os.path.realpath(__file__))
        img = Image.open(os.path.join(curr_dir, 'data', '0.png'))
        tensor = get_test_input_from_pil(img)
        nn = load_nn_test()
        result = nn.classify(tensor)
        self.assertEqual(result, 0)
