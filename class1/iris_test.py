# -*- coding: UTF-8 -*-

import tensorflow as tf
from sklearn import datasets
import matplotlib.pyplot as plt
import numpy as np

# loading data
x_data = datasets.load_iris().data
y_data = datasets.load_iris().target

# shuffle the data
np.random.seed(4396)
np.random.shuffle(x_data)
np.random.seed(4396)
np.random.shuffle(y_data)
tf.random.set_seed(4396)

# split into train_set and test_set
x_train = x_data[:-30]
y_train = y_data[:-30]
x_test = x_data[-30:]
y_test = y_data[-30:]

# transform datatype of x
x_train = tf.cast(x_train, tf.float32)
x_test = tf.cast(x_test, tf.float32)

# from_tensor_slices: match the feature and label and divided into batches
train_db = tf.data.Dataset.from_tensor_slices((x_train, y_train)).batch(32)
test_db = tf.data.Dataset.from_tensor_slices((x_test, y_test)).batch(32)

# generate parameters of nn
# input 4 nodes output 3 nodes
w1 = tf.Variable(tf.random.truncated_normal([4, 3], stddev=0.1, seed=1))
b1 = tf.Variable(tf.random.truncated_normal([3], stddev=0.1, seed=1))

lr = 0.1 # learning rate
train_loss_results = [] # record loss of each epoch
test_acc = []
epoch = 500
loss_all = 0

# training part
for epoch in range(epoch):
    for step, (x_train, y_train) in enumerate(train_db): # loop in batch
        with tf.GradientTape() as tape:
            y = tf.matmul(x_train, w1) + b1
            y = tf.nn.softmax(y)
            y_ = tf.one_hot(y_train, depth=3)
            loss = tf.reduce_mean(tf.square(y_ - y))
            loss_all += loss.numpy()

        # compute grads
        grads = tape.gradient(loss, [w1, b1])

        # update grads
        w1.assign_sub(lr * grads[0])
        b1.assign_sub(lr * grads[1])

    # 每个epoch，打印loss信息
    print("Epoch {}, loss: {}".format(epoch, loss_all/4))
    train_loss_results.append(loss_all / 4)  # 将4个step的loss求平均记录在此变量中
    loss_all = 0  # loss_all归零，为记录下一个epoch的loss做准备

    # test part
    # total_correct: the num of samples which are predicted correctly
    # total_number: the total counts of test samples
    total_correct, total_number = 0, 0
    for x_test, y_test in test_db:
        y = tf.matmul(x_test, w1) + b1
        y = tf.nn.softmax(y)
        pred = tf.argmax(y, axis=1)
        pred = tf.cast(pred, dtype=y_test.dtype)

        correct = tf.cast(tf.equal(pred, y_test), dtype=tf.int32)
        correct = tf.reduce_sum(correct)
        total_correct += int(correct)
        total_number += x_test.shape[0]

    # compute accuracy
    acc = total_correct / total_number
    test_acc.append(acc)
    print("Test_acc:", acc)
    print("----------------------------")

# plot loss curve
plt.title('Loss Function Curve')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.plot(train_loss_results, label="$Loss$")
plt.legend()
plt.show()

# plot Accuracy curve
plt.title("Acc Curve")
plt.xlabel("epoch")
plt.ylabel("acc")
plt.plot(test_acc, label="$Accuracy$")
plt.legend()
plt.show()