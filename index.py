from imagesReader import getImagesWithLabels
import tensorflow as tf; print(tf.reduce_sum(tf.random.normal([1000, 1000])))

trainLabelsFile = open("train-labels.idx1-ubyte", "rb")
trainImagesFile = open("train-images.idx3-ubyte", "rb")
testLabelsFile = open("t10k-labels.idx1-ubyte", "rb")
testImagesFile = open("t10k-images.idx3-ubyte", "rb")

data = getImagesWithLabels(trainLabelsFile, trainImagesFile)
# print([d.label for d in data])