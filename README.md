# Convolutional Neural Network using MNIST dataset for Digit Recognition

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
