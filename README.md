# Convolutional Neural Network using MNIST dataset for Digit Recognition


[![Release](https://img.shields.io/pypi/v/ml-digits-recognition?label=Release&style=flat-square)](https://pypi.org/project/ml-digits-recognition/)
[![CI](https://github.com/MartinBraquet/ml-digits-recognition/actions/workflows/ci.yml/badge.svg)](https://github.com/MartinBraquet/ml-digits-recognition/actions/workflows/ci.yml/badge.svg)
[![CD](https://github.com/MartinBraquet/ml-digits-recognition/actions/workflows/cd.yml/badge.svg)](https://github.com/MartinBraquet/ml-digits-recognition/actions/workflows/cd.yml/badge.svg)
[![Coverage](https://codecov.io/gh/MartinBraquet/ml-digits-recognition/branch/main/graph/badge.svg)](https://codecov.io/gh/MartinBraquet/ml-digits-recognition)
[![Documentation Status](https://readthedocs.org/projects/ml-digits-recognition/badge/?version=latest)](https://ml-digits-recognition.readthedocs.io/en/latest/?badge=latest)
[![Downloads](https://static.pepy.tech/badge/ml-digits-recognition)](https://pepy.tech/project/ml-digits-recognition) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Official repository: https://github.com/MartinBraquet/ml-digits-recognition.

Test online: https://martinbraquet.com/index.php/solo_page_digits_recognition.

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

```
pip install -r requirements.txt
```

## Documentation

Click [here](https://martinbraquet.com/index.php/research/#Convolutional_Neural_Network_using_MNIST_Dataset_for_Digit_Recognition) for a full description.

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

## Issues / Bug reports / Feature requests

Please open an issue.

## Contributions

Contributions are welcome. Please check the outstanding issues and feel free to open a pull request.

### Contributors

[![Contributors](https://contrib.rocks/image?repo=MartinBraquet/ml-digits-recognition)](https://github.com/MartinBraquet/ml-digits-recognition/graphs/contributors)
