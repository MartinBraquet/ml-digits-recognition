import os

import torch
import torchvision.transforms.functional as fn
from torch import nn
from torchvision.transforms import ToTensor


class NeuralNetwork(nn.Module):
    def __init__(self):
        super().__init__()
        self.cnn1 = nn.Sequential(
            nn.Conv2d(in_channels=1, out_channels=1, kernel_size=(3, 3)),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=(2, 2), stride=2),
            nn.Conv2d(in_channels=1, out_channels=1, kernel_size=(5, 5)),
            nn.MaxPool2d(kernel_size=(2, 2), stride=2),
            nn.Flatten(),
            nn.Linear(16, 120),
            nn.ReLU(),
            nn.Linear(120, 84),
            nn.ReLU(),
            nn.Linear(84, 10),
            nn.LogSoftmax(dim=1)
        )

    def forward(self, x):
        return self.cnn1(x)


class NNTest:
    def __init__(self, model):
        self.model = model

    def classify(self, x):
        return torch.argmax(self.model(x)).item()


def get_test_input_from_pil(img):
    test_input = ToTensor()(img)
    if test_input.shape[0] == 4:
        test_input = test_input[None, 3, :, :]
    non_zero = (test_input != 0).nonzero()
    h_min = non_zero[:, 1].min() if len(non_zero) > 0 else 0
    h_max = non_zero[:, 1].max() if len(non_zero) > 0 else test_input.shape[1]
    w_min = non_zero[:, 2].min() if len(non_zero) > 0 else 0
    w_max = non_zero[:, 2].max() if len(non_zero) > 0 else test_input.shape[2]
    w_d = w_max - w_min
    h_d = h_max - h_min
    h_avg = h_min + h_d / 2
    w_avg = w_min + w_d / 2
    h_tot = test_input.shape[1]
    w_tot = test_input.shape[2]
    if h_max - h_min < w_max - w_min:
        test_input_nn = test_input[:, max(0, int(h_avg - w_d / 2)):min(h_tot, int(h_avg + w_d / 2)), w_min:w_max]
    else:
        test_input_nn = test_input[:, h_min:h_max, max(0, int(w_avg - h_d / 2)):min(w_tot, int(w_avg + h_d / 2))]
    test_input_nn = fn.resize(test_input_nn, size=[20, 20])
    test_input_nn = fn.pad(test_input_nn, padding=[4, 4])
    return test_input_nn


def load_nn_test():
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    model = NeuralNetwork().to(device)
    path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'model_precise.pt')
    model.load_state_dict(torch.load(path))
    model.eval()
    return NNTest(model)
