# Convolutional Neural Network using MNIST dataset for Digit Recognition

Official repository: https://github.com/MartinBraquet/ml-digits-recognition.

![Alt Text](https://github.com/MartinBraquet/ml-digits-recognition/blob/main/demo.gif)

## Installation

```
pip install -r requirements.txt
```

## Documentation

Convolutional neural network visualization.

```
nn_visualization.ipynb
```

![Alt Text](https://github.com/MartinBraquet/ml-digits-recognition/blob/main/nn1.png)

![Alt Text](https://github.com/MartinBraquet/ml-digits-recognition/blob/main/nn2.png)

## Training

Train the model and save it as `model.pt`.

```
ml_digits_recognition_training.ipynb
```

Accuracy vs epochs.

![Alt Text](https://github.com/MartinBraquet/ml-digits-recognition/blob/main/accuracy.png)

Loss vs epochs.

![Alt Text](https://github.com/MartinBraquet/ml-digits-recognition/blob/main/loss.png)

## Test

Test in Jupiter Notebook. The model can be loaded from the training above in `model.pt` or from the 
default precise model in `model_precise.pt`.

```
ml_digits_recognition_test.ipynb
```

Test in Python.

```
python user_input_drawing.py
```

## Tools

Draw a digit and save it as a PNG file.

```
user_input_drawing.ipynb
```
