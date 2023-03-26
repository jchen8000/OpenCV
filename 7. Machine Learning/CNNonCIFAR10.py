import tensorflow as tf
import keras
from keras.datasets import cifar10
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.utils import to_categorical
from sklearn import preprocessing
from sklearn import metrics
import matplotlib.pyplot as plt
import numpy as np

def label_names():
    return ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

def plot_random_100_images(data, label, prediction = None, prediction_provided = False):
    _, img_height, img_width, img_channels = data.shape
    _, axarr = plt.subplots(10,10,figsize=(16,16))
    plt.subplots_adjust(wspace=0.1, hspace=0.5)
    for i in range(10):
        for j in range(10):
           index = np.random.randint(data.shape[0])
           groundtruth_lable = label_names()[np.argmax(label[index])]
           if prediction_provided == True:
              predicted_lable = label_names()[np.argmax(prediction[index])]

           axarr[i,j].imshow(data[index].reshape((img_height, img_width, img_channels), order = 'F'), cmap="binary", interpolation="nearest")
           axarr[i,j].axis('off')
           titleStr = groundtruth_lable
           if prediction_provided == True:
              titleStr = titleStr + "\nP:" + predicted_lable
           axarr[i,j].set_title(titleStr)
    plt.show()

def plot_training_result(history):
    fig = plt.figure(1, figsize=(16, 6))
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
    # plt.savefig("cnn_on_cifar-10.svg", format="svg", transparent=True, bbox_inches='tight')
    plt.show()

if __name__ == "__main__":
    # Load CIFAR10 Dataset
    (X_train, y_train), (X_test, y_test) = cifar10.load_data()
    print("X_train", X_train.shape)
    print("y_train", y_train.shape)
    print("X_test", X_test.shape)
    print("y_test", y_test.shape)

    # Display random CIFAR10 data samples
    input_shape = X_train.shape[1:]
    plot_random_100_images(X_train,  to_categorical(y_train))

    # Build the CNN model
    _, height, width, channels = X_train.shape
    n_inputs = height * width
    num_classes = 10
    batch_size = 128
    epochs = 100
    activation = 'relu'

    # Initialising the CNN
    cnn_model = Sequential()

    # 1 - First Convolution and Pooling layer
    cnn_model.add(
        Conv2D(128, kernel_size=(3, 3), input_shape=input_shape, strides=(1, 1), padding="same", activation=activation))
    cnn_model.add(MaxPooling2D(pool_size=(2, 2)))

    # 2 - Second Convolution and Pooling layer
    cnn_model.add(Conv2D(64, kernel_size=(3, 3), strides=(1, 1), padding="same", activation=activation))
    cnn_model.add(MaxPooling2D(pool_size=(2, 2)))
    cnn_model.add(Dropout(0.25))

    cnn_model.add(Conv2D(32, kernel_size=(3, 3), strides=(1, 1), padding="same", activation=activation))
    cnn_model.add(MaxPooling2D(pool_size=(2, 2)))
    cnn_model.add(Dropout(0.25))

    # 3 - Flattening
    cnn_model.add(Flatten())

    # 4 - Full connection
    cnn_model.add(Dense(units=256, activation=activation))
    cnn_model.add(Dropout(0.5))
    cnn_model.add(Dense(units=128, activation=activation))
    cnn_model.add(Dropout(0.5))
    cnn_model.add(Dense(units=num_classes, activation='softmax'))

    # 5 - Compiling the CNN
    cnn_model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    cnn_model.summary()

    # Normalize the images.
    scaler = preprocessing.StandardScaler()
    X_train = scaler.fit_transform(X_train.reshape(-1, X_train.shape[-1])).reshape(X_train.shape)
    X_test = scaler.transform(X_test.reshape(-1, X_test.shape[-1])).reshape(X_test.shape)

    # Train the CNN model
    history = cnn_model.fit(X_train, to_categorical(y_train),
                            batch_size=batch_size,
                            epochs=epochs,
                            verbose=1,
                            validation_data=(X_test, to_categorical(y_test)))

    # summarize history for accuracy and history for loss
    plot_training_result(history)

    # Save the model
    # cnn_model.save('cnn_on_cifar-10.h5')
    cnn_model.save('cnn_on_cifar-10')
    # Evaluation
    score = cnn_model.evaluate(X_test, to_categorical(y_test), verbose=1)
    print('Test loss:', score[0])
    print('Test accuracy:', score[1])

    y_pred = cnn_model.predict(X_test)
    y_pred = np.argmax(y_pred, axis=1)

    a_score = metrics.accuracy_score(y_test, y_pred)
    c_matrix = metrics.confusion_matrix(y_test, y_pred)
    c_report = metrics.classification_report(y_test, y_pred)
    print("Accuracy Score:\n", a_score)
    print("Confusion matrix:\n", c_matrix)
    print("Classification Report:\n", c_report)
