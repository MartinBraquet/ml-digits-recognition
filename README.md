# Convolutional Neural Network using MNIST dataset for Digit Recognition

Official repository: https://github.com/MartinBraquet/ml-digits-recognition.

Test online: https://martinbraquet.com/index.php/solo_page_digits_recognition.

![Alt Text](https://github.com/MartinBraquet/ml-digits-recognition/blob/main/src/demo.gif)

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

Convolutional neural network visualization.

```
nn_visualization.ipynb
```

![Alt Text](https://github.com/MartinBraquet/ml-digits-recognition/blob/main/src/nn1.png)

![Alt Text](https://github.com/MartinBraquet/ml-digits-recognition/blob/main/src/nn2.png)

## Training

Train the model and save it as `model.pt`.

```
ml_digits_recognition_training.ipynb
```

Accuracy vs epochs.

![Alt Text](https://github.com/MartinBraquet/ml-digits-recognition/blob/main/src/accuracy.png)

Loss vs epochs.

![Alt Text](https://github.com/MartinBraquet/ml-digits-recognition/blob/main/src/loss.png)

## Test

Test in Jupiter Notebook. The model can be loaded from the training above in `model.pt` or from the 
default precise model in `model_precise.pt`.

```
ml_digits_recognition_test.ipynb
```

Test in Python.

```
python drawing.py
```

## Tools

Draw a digit and save it as a PNG file.

```
user_input_drawing.ipynb
```
