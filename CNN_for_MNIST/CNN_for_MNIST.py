#! /usr/bin/env python3
# _*_ coding: utf-8 _*_

'''
This py is for learning CNN for MNIST
According from URL:
http://www.leiphone.com/news/201807/VzeOS2ef2wXqkA6V.html

以tensorflow为后台技术, 基于keras的简单2D卷积神经网络CNN模型
1. 准备数据
2. 创建模型并编译
3. 训练模型并评估
4. 将模型存盘以便下次使用
'''

import numpy as np
import keras
from keras.datasets import mnist
from keras import backend as K
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Dropout, Flatten, Dense
import matplotlib.pyplot as plt

class CCnnMnist:
    '''
    class for CNN for MNIST
    '''

    def __init__(self):
        '''
        initialize
        '''

        # datasets
        self.x_train = np.array([])
        self.y_train = np.array([])
        self.x_test  = np.array([])
        self.y_test  = np.array([])
    
        self.img_rows = 28
        self.img_cols = 28
        self.input_shape = (0, 0, 0)
    
        self.num_category = 10          # set number of categoriess
        self.model = Sequential()       # model building

        # training value
        self.batch_size = 128
        self.num_epoch = 10


    def loadMnistDataset(self):
        '''
        this function using for loading MNIST dataset from internet
        everytime loading data won't be so easy...
        '''
        # https://s3.amazonaws.com/img-datasets/mnist.npz is blocked
        # (self.x_train, self.y_train), (self.x_test, self.y_test) = mnist.load_data()

        # load mnist.npz from local path
        path = './mnist.npz'
        f = np.load(path)
        self.x_train, self.y_train = f['x_train'], f['y_train']
        self.x_test, self.y_test = f['x_test'], f['y_test']
        f.close()

    def displayMnistDataSet(self):
        '''
        this function try to display the mnit picture and digit number
        '''

        fig = plt.figure()
        for i in range(9):
            plt.subplot(3, 3, i + 1)
            plt.tight_layout()
            plt.imshow(self.x_train[i], cmap='gray', interpolation='none')
            plt.title("Digit: {}".format(self.y_train[i]))
            plt.xticks([])
            plt.yticks([])
        fig


    def reshaping(self):
        '''
        this function using for reshaping picture
        '''

        # this assumes our data format
        # for 3D data, "channels_last" assumes (conv_dim1, conv_dim2, comv_dim3, channels) while
        # "channels_first" assumes (channels, conv_dim1, conv_dim2, conv_dim3).
        if K.image_data_format() == 'channels_first':
            self.x_train = self.x_train.reshape(self.x_train.shape[0], 1, self.img_rows, self.img_cols)
            self.x_test  = self.x_test.reshape(self.x_test.shape[0], 1, self.img_rows, self.img_cols)
            self.input_shape  = (1, self.img_rows, self.img_cols)
        else:
            self.x_train = self.x_train.reshape(self.x_train.shape[0], self.img_rows, self.img_cols, 1)
            self.x_test  = self.x_test.reshape(self.x_test.shape[0], self.img_rows, self.img_cols, 1)
            self.input_shape  = (self.img_rows, self.img_cols, 1)
            
        # more reshaping
        self.x_train = self.x_train.astype('float32')
        self.x_test = self.x_test.astype('float32')
        self.x_train /= 255
        self.x_test /= 255

        print('x_train shape:', self.x_train.shape) # x_train shape: (60000, 28, 28, 1)
        print('x_test  shape:', self.x_test.shape)  # x_test  shape: (10000, 28, 28, 1)


    def categories(self):
        '''
        this function is using to modify digit number to category
        '''

        # convert class vectors to binary class matrices
        self.y_train = keras.utils.to_categorical(self.y_train, self.num_category)
        self.y_test  = keras.utils.to_categorical(self.y_test, self.num_category)


    def modelBuild(self):
        '''
        this function is using to make the CNN model building
        '''

        # model building
        # model = Sequential()

        # convolutional layer with rectified linear unit activation
        # 32 convolution filters used each of size 3*3
        self.model.add(Conv2D(filters=32, kernel_size=(3, 3), activation='relu', input_shape=self.input_shape))

        # 64 convolution filters used each of size 3*3
        self.model.add(Conv2D(filters=64, kernel_size=(3, 3), activation='relu'))

        # choose the best features via pooling
        self.model.add(MaxPooling2D(pool_size=(2, 2)))

        # randomly turn neurons on and off to improve convergence
        self.model.add(Dropout(0.25))

        # flatten since too many dimensions, we only want a classification output
        self.model.add(Flatten())

        # fully connected to get all relevant data
        self.model.add(Dense(128, activation='relu'))

        # one more dropout for converagence
        self.model.add(Dropout(0.5))

        # output a softmax to squash the matrix info output probabilities
        self.model.add(Dense(self.num_category, activation='softmax'))

        # adaptive learning rate (adaDelta) is a popular form of gradient descent rivaled only by adam and adagrad
        # categorical ce since we have multiple classes (10)
        self.model.compile(loss=keras.losses.categorical_crossentropy, optimizer=keras.optimizers.Adadelta(), metrics=['accuracy'])

        # Output model summary information
        self.model.summary()


    def training(self):
        '''
        training the model
        '''

        # model training
        self.model_log = self.model.fit(self.x_train, \
                            self.y_train, \
                            batch_size=self.batch_size, \
                            epochs=self.num_epoch, \
                            verbose=1, \
                            validation_data=(self.x_test, self.y_test))


    def displayTrainingResult(self):
        '''
        display the model training result
        '''

        score = self.model.evaluate(self.x_test, self.y_test, verbose=0)
        print('Test loss:', score[0])       # Test loss: 0.0296396646054
        print('Test accuracy:', score[1])   # Test accuracy: 0.9904

        # plotting the metrics
        # accuracy
        fig = plt.figure()
        plt.subplot(2, 1, 1)
        plt.plot(self.model_log.history['acc'])
        plt.plot(self.model_log.history['val_acc'])
        plt.title('model accuracy')
        plt.ylabel('accuracy')
        plt.xlabel('epoch')
        plt.legend(['train', 'test'], loc='lower right')

        # loss
        plt.subplot(2, 1, 2)
        plt.plot(self.model_log.history['loss'])
        plt.plot(self.model_log.history['val_loss'])
        plt.title('model loss')
        plt.ylabel('loss')
        plt.xlabel('epoch')
        plt.legend(['train', 'test'], loc='upper right')

        plt.tight_layout()

        fig


    def saveModelToFile(self):
        '''
        save model and training result to file
        '''

        # save the model
        # serialize model to JSON
        model_digit_json = self.model.to_json()

        with open('model_digit.json', 'w') as json_file:
            json_file.write(model_digit_json)

        # serialize weights to HDF5
        self.model.save_weights('model_digit.h5')

        print('Save model to file (model_digit.json and model_digit.h5) finished.')


def main():
    '''
    main function for CNN MNIST
    '''
    
    cnn_for_mnist = CCnnMnist()

    # 1. load MNIST dataset    
    cnn_for_mnist.loadMnistDataset()

    # 2. display MNIST datasets
    cnn_for_mnist.displayMnistDataSet()

    # 3. reshape the datasets
    cnn_for_mnist.reshaping()

    # 4. convert to binary class matrices
    cnn_for_mnist.categories()

    # 5. model building
    cnn_for_mnist.modelBuild()

    # 6. model training
    #cnn_for_mnist.training()

    # 7. display training result
    #cnn_for_mnist.displayTrainingResult()

    # 8. save model and weight to file
    #cnn_for_mnist.saveModelToFile()


if __name__ == '__main__':
    main()

#EOF
