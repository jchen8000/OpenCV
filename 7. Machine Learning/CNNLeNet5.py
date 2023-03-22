import tensorflow as tf
import keras
import keras.layers as layers
from keras.models import Sequential
from keras.utils.np_utils import to_categorical
from keras.callbacks import TensorBoard
from keras.datasets import mnist
from sklearn import preprocessing
from sklearn import metrics
import matplotlib.pyplot as plt
import numpy as np

# Load MNIST dataset
np.random.seed(0)
(X_train, y_train), (X_test, y_test) = mnist.load_data()
print("X_train", X_train.shape)
print("y_train", y_train.shape)
print("X_test", X_test.shape)
print("y_test", y_test.shape)

# Normalize the data
scaler = preprocessing.StandardScaler()
X_train = scaler.fit_transform(X_train.reshape((-1, 784)))
X_test = scaler.fit_transform(X_test.reshape((-1, 784)))
X_train = X_train.reshape(X_train.shape[0], 28, 28, 1)
X_test = X_test.reshape(X_test.shape[0], 28, 28, 1)
input_shape = X_train.shape[1:]

# Build LeNet-5
lenet5 = keras.Sequential()
lenet5.add(layers.Conv2D(filters=6, kernel_size=(3, 3), activation='relu', input_shape=input_shape))
lenet5.add(layers.AveragePooling2D())
lenet5.add(layers.Conv2D(filters=16, kernel_size=(3, 3), activation='relu'))
lenet5.add(layers.AveragePooling2D())
lenet5.add(layers.Flatten())
lenet5.add(layers.Dense(units=120, activation='relu'))
lenet5.add(layers.Dense(units=84, activation='relu'))
lenet5.add(layers.Dense(units=10, activation = 'softmax'))
lenet5.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
lenet5.summary()

# Train the CNN model
batch_size = 128
epochs = 100
history = lenet5.fit(X_train, to_categorical(y_train),
                     batch_size = batch_size,
                     epochs = epochs,
                     verbose = 2,
                     validation_data=(X_test, to_categorical(y_test)) )

# Plot history for accuracy and history for loss
fig = plt.figure(1, figsize=(16,6))
plt.subplot(1, 2, 1)
plt.title('Accuracy', fontsize=16)
plt.plot(history.history['accuracy'], label="Trainset", c='blue')
plt.plot(history.history['val_accuracy'], label="Testset", c='blue', ls='--')
plt.ylabel('Accuracy', fontsize=12)
plt.xlabel('Epoch', fontsize=12)
plt.legend(loc='best', fontsize=12)

plt.subplot(1, 2, 2)
plt.plot(history.history['loss'], label="Trainset", c='k')
plt.plot(history.history['val_loss'], label="Testset", c='k', ls='--')
plt.title('Loss', fontsize=16)
plt.ylabel('Loss', fontsize=12)
plt.xlabel('Epoch', fontsize=12)
plt.legend(loc='best', fontsize=12)
plt.savefig("lenet5_on_cifar-10.svg", format="svg", transparent=True, bbox_inches='tight')
plt.show()

# Evaluate LeNet-5
score = lenet5.evaluate(X_test, to_categorical(y_test))
print('Test loss:', score[0])
print('Test accuracy:', score[1])

y_pred = lenet5.predict(X_test)
y_pred = np.argmax(y_pred, axis=1)
a_score = metrics.accuracy_score(y_test, y_pred)
c_matrix = metrics.confusion_matrix(y_test, y_pred)
c_report = metrics.classification_report(y_test, y_pred)
print("Accuracy Score:\n", a_score)
print("Confusion matrix:\n", c_matrix)
print("Classification Report:\n", c_report)