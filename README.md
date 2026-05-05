# Convolutional Neural Network using MNIST dataset for Digit Recognition


[![Release](https://img.shields.io/pypi/v/ml-digits-recognition?label=Release&style=flat-square)](https://pypi.org/project/ml-digits-recognition/)
[![CI](https://github.com/MartinBraquet/ml-digits-recognition/actions/workflows/ci.yml/badge.svg)](https://github.com/MartinBraquet/ml-digits-recognition/actions/workflows/ci.yml/badge.svg)
[![CD](https://github.com/MartinBraquet/ml-digits-recognition/actions/workflows/cd.yml/badge.svg)](https://github.com/MartinBraquet/ml-digits-recognition/actions/workflows/cd.yml/badge.svg)
[![Coverage](https://codecov.io/gh/MartinBraquet/ml-digits-recognition/branch/main/graph/badge.svg)](https://codecov.io/gh/MartinBraquet/ml-digits-recognition)
[![Documentation Status](https://readthedocs.org/projects/ml-digits-recognition/badge/?version=latest)](https://ml-digits-recognition.readthedocs.io/en/latest/?badge=latest)
[![Downloads](https://static.pepy.tech/badge/ml-digits-recognition)](https://pepy.tech/project/ml-digits-recognition) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This work proposes an algorithm which detects a digit (from 0 to 9) from an image. Click on the video to test the algorithm in real time.

Image recognition is performed through a convolutional neural network (shown below). The first round reduces the dimension of the input image while keeping its meaningful information (Conv / ReLu / MaxPool / Conv / MaxPool). The second round flattens the 2D tensor and passes it through a classical neural network (multilayer perceptron) to produce 10 values (one associated to each digit). The third round performs a logarithmic softmax on the 10 values to reflect the probability that each digit is rendered on the input image. The last round outputs the digit with the highest of the 10 computed probabilities (maximum likelihood estimator).

It was trained using the MNIST dataset (60k images) across 50 epochs with a batch size of 256, achieving 95% of accuracy on the test dataset.

Official repository: https://github.com/MartinBraquet/ml-digits-recognition.

![Alt Text](https://raw.githubusercontent.com/MartinBraquet/ml-digits-recognition/main/src/ml_digits_recognition/demo.gif)

## Installation from PyPI

```
pip install ml-digits-recognition
```

### Usage

```
from ml_digits_recognition import drawing
drawing.run()
```


## Installation from Source

For basic usage:
```
pip install -e "."
```

For development:
```
pip install -e ".[dev]"
```


## Documentation

Click [here](https://martinbraquet.com/research/#Convolutional_Neural_Network_for_Digit_Recognition) for a full description.

Visualization of the convolutional neural network:

```
nn_visualization.ipynb
```

![](https://raw.githubusercontent.com/MartinBraquet/ml-digits-recognition/main/src/ml_digits_recognition/nn1.png)

![](https://raw.githubusercontent.com/MartinBraquet/ml-digits-recognition/main/src/ml_digits_recognition/nn2.png)

## Training

Train the model and save it as `model.pt`.

```
ml_digits_recognition_training.ipynb
```

Accuracy vs epochs.

![](https://raw.githubusercontent.com/MartinBraquet/ml-digits-recognition/main/src/ml_digits_recognition/accuracy.png)

Loss vs epochs.

![](https://raw.githubusercontent.com/MartinBraquet/ml-digits-recognition/main/src/ml_digits_recognition/loss.png)

## Test

Test in Jupiter Notebook. The model can be loaded from the training above in `model.pt` or from the 
default precise model in `model_precise.pt`.

```
ml_digits_recognition_test.ipynb
```

Test in Python.

```
python src/ml_digits_recognition/drawing.py
```

## Tools

Draw a digit and save it as a PNG file.

```
user_input_drawing.ipynb
```

## CI / CD

Each commit on the `main` branch is subject to a CI test.

A new version is released to PyPI when a tag is created. TODO: Set version in `pyproject.toml` only, then trigger a new PyPI release (and git tag) by updating the version and pushing into `main`. The CD should thus check on each push on main, if the package is more recent than the last tag, then build and deploy new release. This is faster as one only needs to update locally the version in `pyproject.toml` in the same commit as the fixes for the new release. The rest is automated, so it can all be done from a local IDE.
The version can be accessible at other places if desired. For example in `__init__.py`:
```python
import importlib.metadata
__version__ = importlib.metadata.version(__package__)
```

## Issues / Bug reports / Feature requests

Please open an issue.

## Contributions

Contributions are welcome. Please check the outstanding issues and feel free to open a pull request.

### Contributors

[![Contributors](https://contrib.rocks/image?repo=MartinBraquet/ml-digits-recognition)](https://github.com/MartinBraquet/ml-digits-recognition/graphs/contributors)
